import psutil
import time
import os, subprocess
import requests

def send_line(message):
    url = 'https://notify-api.line.me/api/notify'
    access_token = 'TOKEN'
    headers = {'Authorization': 'Bearer ' + access_token}
    message = message
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

def procname():
    for process in psutil.process_iter():
        if "notepad.exe" in process.name():
            p = process.pid
            proc = psutil.Process(p)
            pname = proc.name()
            status = proc.status()
            return p, pname, status

send_lists = []

while True:
    print(procname())
    time.sleep(3)
    if procname() not in send_lists:
        send_line(str(procname()) + 'Started!!')
        send_lists.append(procname())

    if procname() is None:
        send_line(str(procname()) + "Process Down")

        time.sleep(10)
        subprocess.Popen('notepad')
        continue
