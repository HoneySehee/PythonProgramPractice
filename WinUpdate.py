import os,requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def send_line(args):
    url = 'https://notify-api.line.me/api/notify'
    access_token = '54BkwrXunHMpeuOhpkXDTQrPwNtsUW7oiZew05RoKBR'
    headers = {'Authorization': 'Bearer ' + access_token}
    message = args
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

url = "https://portal.msrc.microsoft.com/ko-kr/security-guidance"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get(url)

updates = driver.find_elements_by_class_name("ng-scope.tbody-striped")

send_line(updates[0].text)
send_line(updates[1].text)
send_line(updates[2].text)
send_line(updates[3].text)
send_line(updates[4].text)

driver.close()