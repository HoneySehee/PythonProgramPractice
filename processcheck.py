import psutil
import time
import os
import requests

def procname():
    for process in psutil.process_iter():
        if "notepad.exe" in process.name():
            p = process.pid
            proc = psutil.Process(p)
            pname = proc.name()
            status = proc.status()
            return p, pname, status
while True:
    print(procname())
    time.sleep(10)
    if procname() is None:
        #Line API
        url = 'https://notify-api.line.me/api/notify'
        access_token = '8menQ9ILfMC7HK8a2MSN8fJCsX9AJETyJj38ryVs6iS'
        headers = {'Authorization': 'Bearer ' + access_token}

        message = 'Process Down!!'
        payload = {'message': message}
        r = requests.post(url, headers=headers, params=payload,)
        continue