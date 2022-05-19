import os
import time
from data import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from D_alert import *

class Target:
    watchDir = download_dir
    #watchDir에 감시하려는 디렉토리를 명시

    def __init__(self):
        self.observer = Observer()   #observer객체를 만듦

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDir, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1) # 1초마다 감시
        except:
            self.observer.stop()
            print("Error")
            self.observer.join()

class Handler(FileSystemEventHandler):
#FileSystemEventHandler 클래스를 상속받음.
#오버라이드

    def on_created(self, event): #파일, 디렉터리가 생성되면 실행
        d_alert()

def monitoring():
    w = Target()
    w.run()