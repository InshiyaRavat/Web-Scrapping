from bs4 import BeautifulSoup
import time
import requests
import datetime
import smtplib
import csv

def check_price():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    page = requests.get('https://www.amazon.in/s?k=television&crid=2TJUMWYJAM2JT&sprefix=television%2Caps%2C206&ref=nb_sb_noss_1',headers = headers)

    soup1 = BeautifulSoup(page.content,'lxml') #used html_parser
    soup2 = BeautifulSoup(soup1.prettify(),'lxml')

    titles = soup2.find_all(class_='a-size-medium a-color-base a-text-normal')
    prices = soup2.find_all(class_="a-price-whole")
    print(titles)
    print(prices)

    
    for title,price in zip(titles,prices):
        today = datetime.date.today()
        data = [title.text.strip(),price.text.strip(),today]

        with open('amazonTitleAndPrice3.csv','a+',newline='',encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)

if __name__== '__main__':
    # while(True):
        check_price()
        # time.sleep(5)

