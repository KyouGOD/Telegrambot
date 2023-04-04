import random
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import fake_useragent
import requests, time, sched, cfscrape, cloudscraper
from bs4 import BeautifulSoup
from requests_html import HTMLSession

scraper = cloudscraper.create_scraper()
session = HTMLSession()
print(scraper.get(session))
session.
response = scraper.get('https://ru.investing.com/currencies/usd-rub')
session_response = session.get('https://ru.investing.com/currencies/usd-rub')

#print(response.content)
print(session_response.html.html)
'''

scraper = cloudscraper.create_scraper()
url = "https://ru.investing.com/currencies/usd-rub"
session = HTMLSession()
print(session)


def Parse():
    page = scraper.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text,"html.parser")
    course = soup.find(attrs={"data-test": "instrument-price-last"}).contents[0]
    print(course)
'''
'''
while(True):
    Parse()
    time.sleep(10)

    '''
'''
    block = soup.find(attrs={"data-rowkey": "FX_IDC:USDRUB"}).find("td", class_="cell-TKkxf89L right-TKkxf89L").contents[0]
    print(block)

scheduler = sched.scheduler(time.time, time.sleep)


def call_repeatedly(interval, func, *args):
    scheduler.enter(interval, 1, call_repeatedly, (interval, func, *args))
    func(*args)

call_repeatedly(90, Parse)
scheduler.run()
