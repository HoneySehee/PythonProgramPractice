from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os
import time
import requests

def send_line(message):
    url = 'https://notify-api.line.me/api/notify'
    access_token = '8menQ9ILfMC7HK8a2MSN8fJCsX9AJETyJj38ryVs6iS'
    headers = {'Authorization': 'Bearer ' + access_token}
    message = message
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

target_dir = 'D:\\text'

print("감시중..")

class FileChangeHandler(FileSystemEventHandler):
     def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
         
        send_line(filepath + '\n'+'\n' + 'Create!!!')

     def on_modified(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('{} changed'.format(filename))

     def on_deleted(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('{} deleted'.format(filename))

     def on_moved(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('{} moved'.format(filename))

if __name__ == "__main__":
     event_handler = FileChangeHandler()
     observer = Observer()
     observer.schedule(event_handler, target_dir, recursive=True)
     observer.start()
     # 처리가 종료되지 않게 슬립걸고 무한루프
     try:
         while True:
             time.sleep(0.1)
     except KeyboardInterrupt:
         print("The End!")
         observer.stop()
     observer.join()
