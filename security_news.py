from bs4 import BeautifulSoup
from selenium import webdriver
import requests

def send_line(*args):
    url = 'https://notify-api.line.me/api/notify'
    access_token = ''
    headers = {'Authorization': 'Bearer ' + access_token}
    message = args
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

link = "https://www.boannews.com/"
url = "https://www.boannews.com/media/o_list.asp"
driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

atag = soup.select("div#main_HitNews > ul > li")

for li in atag[0:5]:
    title = li.select("a")[0].text
    links = li.select("a")[0]['href']

    send_line(title + '\n' + '{}'.format(link) + links)

driver.close()
