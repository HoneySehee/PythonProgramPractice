from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os
import time
import requests

target_dir = 'D:\\text'

class FileChangeHandler(FileSystemEventHandler):
     def on_created(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)

         #Line API
         url = 'https://notify-api.line.me/api/notify'
         access_token = '라인토큰'
         headers = {'Authorization': 'Bearer ' + access_token}

         message = filepath + '\n'+'\n' + 'Create!!!'
         payload = {'message': message}
         r = requests.post(url, headers=headers, params=payload,)

     def on_modified(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s changed' % filename)

     def on_deleted(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s deleted' % filename)

     def on_moved(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s moved' % filename)

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
