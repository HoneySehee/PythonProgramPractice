from bs4 import BeautifulSoup
import requests,time

def send_line(*args):
    url = 'https://notify-api.line.me/api/notify'
    access_token = 'MYTOKEN'
    headers = {'Authorization': 'Bearer ' + access_token}
    message = args
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)


url = "https://finance.naver.com/marketindex/exchangeList.nhn"
r = requests.get(url)
bs = BeautifulSoup(r.text, "lxml")


trs = bs.select("table.tbl_exchange > tbody > tr")

exchange = {}
dictlist = []
dictlists = []

for tr in trs:
    tds = tr.select("td")
    name = tds[0].text.strip()
    money = tds[1].text.strip()
    exchange[name] = money

for key,value in dict.items(exchange):
    temp = [key,value]
    dictlist.append(temp)

while True:
    time.sleep(5)
    if dictlist[2] not in dictlists:
        send_line(dictlist[2],"원")
        dictlists.append(dictlist[2])
