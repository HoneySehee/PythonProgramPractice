from bs4 import BeautifulSoup
from selenium import webdriver
import requests , time

def send_line(*args):
    url = 'https://notify-api.line.me/api/notify'
    access_token = 'TOKEN'
    headers = {'Authorization': 'Bearer ' + access_token}
    message = args
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

send_lists = []

while True:
    url = "https://hazard.yahoo.co.jp/article/covid19tokyo"
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    dashBoard = soup.select('.dashBoard')

    for i in dashBoard:
        item = (i.select('.notes__item')[1].text)
        title = (i.select_one('.dashBoard__title').text)
        main = (i.select('.dashBoard__main')[0].text)
        
        driver.close()
        print(item)
        
        if item not in send_lists:
            send_line(item + '\n', title + '\n', main + '\n')
            send_lists.append(item)

    time.sleep(3600)
