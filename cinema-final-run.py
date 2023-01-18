#!/usr/bin/env python
# coding: utf-8

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import date 
from datetime import timedelta
from time import sleep
import os


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def GetDailyMovieList(url, classname, chrome_path = 'driver/chromedriver'):
    titles = []
    
    options = Options()
    options.headless = True
    
    chrome_path = '/opt/homebrew/lib/node_modules/chromedriver/lib/chromedriver/chromedriver'

    #driver = webdriver.Chrome(chrome_path)
    driver = webdriver.Chrome(chrome_path, options=options)
    driver.get(url)
    sleep(10)
    
    #a = driver.find_elements_by_class_name(classname)
    a = driver.find_elements(By.CLASS_NAME, classname)
    for element in a:
        titles.append(element.text)
    driver.close()
    return titles


classname='qb-movie-name'
#cinema_location = bonarka
span = 7

url = 'https://www.cinema-city.pl/kina/bonarka/1090#/buy-tickets-by-cinema?in-cinema=1090&at='+str(date.today())+'&view-mode=list'
url2 = 'https://www.cinema-city.pl/kina/bonarka/1090#/buy-tickets-by-cinema?in-cinema=1090&at='+str(date.today()+timedelta(days=span))+'&view-mode=list'

first = GetDailyMovieList(url, classname)
second = GetDailyMovieList(url2, classname)

outs = [ x for x in first if not x in second]
ins = [ x for x in second if not x in first]


for out in outs:
    notify("Out this week", out)
# for _in in ins:
#     notify("In this week", _in)

