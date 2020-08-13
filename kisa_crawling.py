from bs4 import BeautifulSoup
import requests

link = "https://www.krcert.or.kr"
r = requests.get("https://www.krcert.or.kr/data/secNoticeList.do")
bs = BeautifulSoup(r.text, "lxml")

trs = bs.select("table.basicList.default > tbody > tr")

for tr in trs:
    tds = tr.select("td")
    title = tds[1].select("a")[0].text
    date = tds[4].text
    links = tds[1].select("a")[0]['href']

    url = 'https://notify-api.line.me/api/notify'
    access_token = 'TOKEN'
    headers = {'Authorization': 'Bearer ' + access_token}

    message = title + '\n' + date + '\n' + '{}'.format(link) + links
    data = {'message': message}
    r = requests.post(url, headers=headers, params=data,)
