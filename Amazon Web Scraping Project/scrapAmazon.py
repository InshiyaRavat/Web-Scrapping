from bs4 import BeautifulSoup
import time
import requests
import datetime
import smtplib
import csv

def check_price():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    page = requests.get('https://www.amazon.in/LG-inches-Ultra-Smart-65UR7500PSC/dp/B0C834YC4Z/ref=sr_1_1_sspa?crid=2TJUMWYJAM2JT&keywords=television&qid=1705670312&sprefix=television%2Caps%2C206&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1',headers = headers)

    soup1 = BeautifulSoup(page.content,'lxml') #used html_parser
    soup2 = BeautifulSoup(soup1.prettify(),'lxml')

    title = soup2.find(id='productTitle').get_text().strip()
    price = soup2.find(class_="a-price-whole").get_text().strip()
    print(title)
    print(price)

    today = datetime.date.today()

    data = [title,price,today]

    with open('amazonTitleAndPrice.csv','a+',newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

if __name__== '__main__':
    while(True):
        check_price()
        time.sleep(5)

