from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import requests , time

def send_line(*args):
    url = 'https://notify-api.line.me/api/notify'
    access_token = 'MyToken'
    headers = {'Authorization': 'Bearer ' + access_token}
    message = args
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

send_lists = []
today = datetime.today().strftime("%Y/%m/%d")

while True:
    url = "https://hazard.yahoo.co.jp/article/covid19tokyo"
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    dashBoard = soup.select('div.dashBoard > dl.dashBoard__main > div')

    corona = []

    for i in dashBoard:
        corona.append(i)

    if corona[1].text not in send_lists:
        send_line("{} \n {}".format(today,corona[1].text))
        send_lists.append(corona[1].text)
    
    print(send_lists)
    driver.close()
    time.sleep(60 * 30)
