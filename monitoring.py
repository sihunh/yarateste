# 디렉터리가 아닐때 해당 파일 읽어옴
# hashlib함수를 이용해서 md5로 암호화후(해시값 검사를 위함) virustotal api넘김
# hash 검증후 file result 결과 받고 데이터 추출
# 만약 다른방법 쓸거면 yara를 악성코드 탐지룰 추가후 검사
# 20220920 예상치 못한 오류 ;; 파일 다운로드시 tmp파일생성후 파일 다운로드 진행이 되어 tmp파일명으로 인식하여 재대로 이루어지지 않음 

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
from firebase_upload import *

url = "http://www.virustotal.com/api/v3/search?query="
file_hash = ""

def stag(event, Fname, full_name): 
        print(full_name)
        f = open(full_name,'rb')
        data = f.read()
        f.close()
        stg_rt = stg(full_name) # 스테가노그래피 검사
        print('file : ', full_name, end='')
        if stg_rt > 1:
            print('\nSteganography Detect\t' , 'number of file : ', stg_rt )
        else:
            print("\nSteganography Not Detect")

        file_hash = hashlib.md5(data).hexdigest()

        response =requests.get(url+file_hash, headers=headers)
        json_data=response.json()

        firebase_upload(json_data,'FILE_scan_rt', Fname) # db업로드 :: json_dt, colletion_name, file_name

        with open(file_scan_path + Fname + '.json','w') as outfile:
            json.dump(json_data, outfile)
        print ("Create result file")

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
            if Extension != '.tmp' and '.zip':
                stag(event, Fname ,event.src_path)
            else:
                time.sleep(5) # 다운로드 시간 맞추기 우째야할지 고민 해야함 1. 파일 크기로 예측 2. 완료 시그널
                wDir = "C:/test_download/"
                file_time = [] 
                for f_name in os.listdir(wDir):
                    written_time = os.path.getctime(wDir + f_name)
                    file_time.append((f_name, written_time))
                sorted_file_lst = sorted(file_time, key=lambda x: x[1], reverse=True)
                recent_file = sorted_file_lst[0]
                recent_file_name = recent_file[0]
                stag(event,recent_file_name ,wDir + recent_file_name)

    def on_deleted(self, event): #파일, 디렉터리가 삭제되면 실행
        print(event)

'''
    def on_modified(self, event): #파일, 디렉터리가 수정되면 실행
        print(event)
'''

def monitoring():
    w = Target()
    w.daemon = True
    w.run()