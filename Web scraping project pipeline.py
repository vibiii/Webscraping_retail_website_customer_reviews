# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:03:54 2020

@author: virrginie.broly
"""

import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
import pymysql
from sqlalchemy import create_engine
import re

url = input('Input the url: ')
headers = input('input your headers: ')

def acquire():
    
    def offre(str1):
        if 'offre' not in str1:
            return str1
        
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    shampoo_lst= [i['href'] for i in soup.select('h5>a')].pop()
    final_shampoo = list(filter(offre, shampoo_lst))
    
    Comment_answer_rating=[]
    Category=[]
    Brand=[]
    Product=[]
    
    for u in final_shampoo:
        los=[]
        i=1
        k=0
        while k==0:
            url = f'{u}?iPage={i}'
            html = requests.get(url, headers=headers).content
            soup = BeautifulSoup(html, 'lxml')
            if soup.select('#idTab9999 p') in los:
                break
            reviews_no_answer = [i.text.strip() for i in soup.select('div.gsrReviewLine:not(:has(blockquote))')]
            rating_no_answer = [i['content'] for i in soup.select("div.gsrReviewLine:not(:has(blockquote)) meta[itemprop='ratingValue']")]
            no_answer_final =[[reviews_no_answer[i], '',rating_no_answer[i]] for i in range(len(reviews_no_answer))]
            reviews_answer = [i.text.strip().split('(Lire tous ses avis)') for i in soup.select('div.gsrReviewLine:has(blockquote)')]
            rating_answer = [i['content'] for i in soup.select("div.gsrReviewLine:has(blockquote) meta[itemprop='ratingValue']")]
            answer_final =[[reviews_answer[i][0], reviews_answer[i][1],rating_answer[i]] for i in range(len(reviews_answer))]
            comment_answer_rating = answer_final+no_answer_final
            Comment_answer_rating.extend(comment_answer_rating)
            brand = ['' if len(soup.select('.col-sm-8>a'))==0 else soup.select('.col-sm-8>a')[0].text.strip() for j in range(len(comment_answer_rating))]
            Brand.extend(brand)
            product = [i.text.strip() for i in soup.select('.col-sm-8>h2') for j in range(len(comment_answer_rating))]
            Product.extend(product)
            category = [soup.select('ol.breadcrumb.clearfix>span>li:nth-child(5)')[0].text.strip() for j in range(len(comment_answer_rating))]
            Category.extend(category)
            los.append(soup.select('#idTab9999 p'))
            print(i)
            i+=1
            time.sleep(4)
            
    df=pd.DataFrame()
    df['Category'] = [i for i in Category]
    df['Brand'] = [i for i in Brand]
    df['Product'] = [i for i in Product]
    df['Review']= [i[0] for i in Comment_answer_rating]
    df['Answer']= [i[1] for i in Comment_answer_rating]
    df['Rating']= [i[2] for i in Comment_answer_rating]
    return df
    
    
def wrangle(bio):
    bio['Date'] = pd.to_datetime(bio['Review'].apply(lambda x: '_'.join(re.compile(r'\d{2}/\d{2}/\d{4}').findall(x))))
    bio['Year']=bio['Date'].dt.to_period('Y')
    bio['Has_answer'] = bio['Answer'].apply(lambda x : 1 if x!='' else 0)
    bio['Review'] =bio['Review'].apply(lambda x : re.split(r'Le\d{2}/\d{2}/\d{4}', x)[0].strip())
    bio['Review']= bio['Review'].apply(lambda x : re.sub('\s+', ' ', x).strip())
    return bio


def to_sql(df):
    username= 'random_name'
    host = 'db4free.net'
    password = 'IronHack'
    database_name = 'iron_database'
    engine =create_engine(f"""mysql+pymysql://{username}:{password}@{host}/{database_name}""")
    df.to_sql('data_bio', engine, index = False)
    return bio = pd.read_sql_query('SELECT * FROM data_bio',engine)

def analyze(bio):
    result1 =bio.groupby('Rating').agg({'Rating' : 'count', 'Has_answer': 'sum'})
    result1.rename(columns = {'Rating':'Total_reviews'}, inplace = True)
    result1['Proportion_answered']=result1['Has_answer']/result1['Total_reviews']
    result2 =bio.groupby(['Rating', 'Year']).agg({'Rating' : 'count', 'Has_answer': 'sum'})
    result2.rename(columns = {'Rating':'Total_reviews'}, inplace = True)
    result2['Proportion_answered']=result2['Has_answer']/result2['Total_reviews']
    return result1, result2

def report(result1, result2):
    result1.to_csv('C:\\Users\\virrginie.broly\\Documents\\4.Training\\Ironhack\\dataV2-labs\\module-1\\result1.csv', index = True)
    result2.to_csv('C:\\Users\\virrginie.broly\\Documents\\4.Training\\Ironhack\\dataV2-labs\\module-1\\result2.csv', index = True)
    
if __name__=='__main__':
    data = acquire()
    cleaned = wrangle(data)
    data_saved = to_sql(cleaned)
    results = analyze(data_saved)
    report(results)