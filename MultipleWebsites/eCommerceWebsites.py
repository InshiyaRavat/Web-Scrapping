from bs4 import BeautifulSoup
import time
import requests
import datetime
import smtplib
import csv

details = [
    {
        'name' : 'Amazon',
        'url': 'https://www.amazon.in/s?k=television',
        'title_class': 'a-size-medium a-color-base a-text-normal',
        'price_class': 'a-price-whole'
    },
    {
        'name' : 'Flipkart',
        'url': 'https://www.flipkart.com/search?q=telivision',
        'title_class': '_4rR01T',
        'price_class': '_30jeq3 _1_WHN1'
    },
    {
        'name' : 'Snapdeal',
        'url': 'https://www.snapdeal.com/search?keyword=mobile',
        'title_class': 'product-title',
        'price_class': 'lfloat product-price'
    }
]

def check_price():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    for i in range(len(details)):
        page = requests.get(details[i]['url'], headers=headers)

        soup1 = BeautifulSoup(page.content, 'lxml')
        soup2 = BeautifulSoup(soup1.prettify(), 'lxml')

        titles = soup2.find_all(class_=details[i]['title_class'])
        prices = soup2.find_all(class_=details[i]['price_class'])
        print(f'#########{details[i]["name"]}############')
        print(titles)
        print(prices)
        if titles and prices:
            for title, price in zip(titles, prices):
                today = datetime.date.today()
                data = [title.text.strip(), price.text.strip(), today]

                with open('multipleWebsiteScrap.csv', 'a+', newline='', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)

if __name__ == '__main__':
    check_price()
    # time.sleep(5)
