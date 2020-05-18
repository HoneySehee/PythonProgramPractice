from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

url = "https://hazard.yahoo.co.jp/article/covid19tokyo"

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

dashBoard = soup.select('.dashBoard')

for i in dashBoard:
    kosin = (i.select_one('.notes__item.notes__item--right').text)
    jokyo = (i.select_one('.dashBoard__main').text)

driver.close()

url = 'https://notify-api.line.me/api/notify'
access_token = 'LINE TOKEN'
headers = {'Authorization': 'Bearer ' + access_token}

message = kosin, jokyo
data = {'message': message}
r = requests.post(url, headers=headers, params=data,)
