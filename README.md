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


            
