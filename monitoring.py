# 디렉터리가 아닐때 해당 파일 읽어옴
# hashlib함수를 이용해서 md5로 암호화후(해시값 검사를 위함) virustotal api넘김
# hash 검증후 file result 결과 받고 데이터 추출
# 만약 다른방법 쓸거면 yara를 악성코드 탐지룰 추가후 검사

import os
import time
from data import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from D_alert import *
import requests
import hashlib
import json
from stg import *

url = "http://www.virustotal.com/api/v3/search?query="
file_hash = ""


class Target:
    watchDir = download_dir
    #watchDir에 감시하려는 디렉토리를 명시한다.

    def __init__(self):
        print ("Observe start")
        self.observer = Observer()   #observer객체를 만듦

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDir, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1) # 1초마다 감시
        except KeyboardInterrupt as e: #"ctrl + c"
            print ("Observe Stop")
            self.observer.stop() 

class Handler(FileSystemEventHandler):
#FileSystemEventHandler 클래스를 상속받음.
    def on_created(self, event): #파일, 디렉터리가 생성되면 실행
        if event.is_directory == False:
            Fname, Extension = os.path.splitext(os.path.basename(event.src_path))
            f = open(event.src_path,'rb')
            data = f.read()
            f.close()
            stg_rt = stg(event.src_path) # 스테가노그래피 검사
            print('file : ', event.src_path, end='')
            if stg_rt > 1:
                print('\nSteganography Detect\t' , 'number of file : ', stg_rt )
            else:
                print("\nSteganography Not Detect")

            file_hash = hashlib.md5(data).hexdigest()

        response =requests.get(url+file_hash, headers=headers)
        json_data=response.json()

        with open(file_scan_path + Fname + '.json','w') as outfile:
            json.dump(json_data, outfile)
        print ("Create result file")

'''
    def on_deleted(self, event): #파일, 디렉터리가 삭제되면 실행
        print(event)

    def on_modified(self, event): #파일, 디렉터리가 수정되면 실행
        print(event)
'''

def monitoring():
    w = Target()
    w.daemon = True
    w.run()