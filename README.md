# Webscraping the customer reviews of a retail website in order to assess the quality of the customer service
Web scraping is the process of automatically extracting data from websites and saving that data collected into a dataset allowing you to use that data to extract information. It’s one of the most efficient ways to get data from the web. Some practices inlcude

* Research for web content or business intelligence
* Pricing for travel booker sites/price comparison sites
* Finding sales leads/conducting market research by crawling public data sources
* Sending product data from an e-commerce site to another online vendor

## Purpose
In this project I will create a pipeline that will web scrap an organic cosmetic seller using Python, Pandas, and BeautifulSoup. 
I will collect data regarding the reviews made by customers on the various products and the answers provided by the customer service to these reviews.
Using this dataset, I will make a general analysis on the performance of the customer service looking at the proportion of customer reviews answered by the customer service according to the rating given by the customer to the considered product. We consider that the lowest the rating, the highest should be the proportion of answered comments because adressing unsatisfied customers should be the main objective of the customer service team.

## Getting started
The website is Mademoiselle Bio :
* https://www.mademoiselle-bio.com/

## Examining the website

There are two major techniqes used in web scraping. Using HTML to target web page tags, or using an API to extract data. In this case, I will use HTML tags and BeautifulSoup library to target key web page tags, and retrieve the specific information.

BeautifulSoup will get the URL and the element tags of that web page, and extract the elements you specify. Using this, I am able to collect :
* Category : the category of the product (shampoo, conitioner, etc...)
* Brand
* Product name
* Rating given by each customer who write a review
* Review written by each customer
* Answer from the customer service (if there is one)

I am creating a function that will take as an input the url entered by the user corresponding to the page that lists all the products the user wants to scrap.
The function will :
* Remove the "promotional offers" in order to keep only the "real products"
* Loop in the pages of each product in order to collect the requested data 
* Sometimes in the products pages, there are several pages of customer reviews, as a consequence the function will loop in all those pages in order to collect the whole reviews

![picture alt](https://github.com/vibiii/Webscraping_retail_website_customer_reviews/blob/master/Images/Func_acquire.JPG)

Once I have scrapped all the data requested I create a dataframe 
![picture alt](https://github.com/vibiii/Webscraping_retail_website_customer_reviews/blob/master/Images/Scrapped_df.JPG)

## Cleaning The Data & Creating the Dataset

In this case, we have no that much of cleaning since the information collected is already rather clean.
I will mainly use the information collected in order to create new columns that will be useful for my analysis :
* Date : date of the customer review : after the scrapping this information is included in the review column so I need to extract it
* Year
* Has answer : column that will be 1 if the customer service has answered the customer review and 0 if not

![picture alt](https://github.com/vibiii/Webscraping_retail_website_customer_reviews/blob/master/Images/Func_wrangle.JPG)

## Analyzing the data

I create 2 results dataframe that will provide :
* The proportion of cutomers reviews answered by the customer service according the rating given (from 1 to 5 stars)
* The same but taking into account the year in order to see the evolution of the performance of the customer service department over time

![picture alt](https://github.com/vibiii/Webscraping_retail_website_customer_reviews/blob/master/Images/Func_analyze.JPG)

These results have been exported to csv and I used excel in order to make the final graph

![picture alt](https://github.com/vibiii/Webscraping_retail_website_customer_reviews/blob/master/Images/Result%201.JPG)
![picture alt](https://github.com/vibiii/Webscraping_retail_website_customer_reviews/blob/master/Images/Result_2.JPG)
![picture alt](https://github.com/vibiii/Webscraping_retail_website_customer_reviews/blob/master/Images/Result_3.JPG)

## Storytelling of the data in a presentation

For this project, Ironhack tasked me in presenting my project in a real life senario to simulate the process of collecting, cleaning, and presenting my analysis. For this project I assume my client was Mademoiselle Bio looking to assess the performance of it's customer service.

The presentation is as a powerpoint that can be found in this repository as "Webscrapping_presentation.ppt"

## Built with

* Python - The programming language used
* Pandas - library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language
* BeautifulSoup - Python library for pulling data out of HTML and XML files
* Excel
