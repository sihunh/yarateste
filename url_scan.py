# report랑 scan 따로 구현 해야함 report를 받아와야함 검사 시간 1분 소요 된다고 하니 스레드로 돌려야할듯함
# url 뒤에 붙는거는 인식을 못함 값들 예 google.com/~~ 이뒤에값 인식을 못함
import json
import requests
from data import *
import threading
import time
import base64
import os


class Worker(threading.Thread):
    def __init__(self, change_url, c):
        super().__init__()
        self.change_url = str(change_url)            
        self.filenames = os.listdir(url_scan_path)
    def run(self):
        if "//" in self.change_url:
            i = self.change_url.find("//")
            l = self.change_url.index('/', i+2)
            sitename = self.change_url[i+2:l]
            if "www" in sitename:
                i = self.change_url.find("www")
                l = self.change_url.index('/', i+4)
                sitename = self.change_url[i+4:l]
            try:
                sitename_bytes = sitename.encode('ascii')
                sitename_base64 = base64.b64encode(sitename_bytes)
                sitename_base64 = str(sitename_base64)
                length = len(sitename_base64)
            except Exception:
                print("Not Encoding")
        
        if  sitename not in self.filenames:
            url = "https://www.virustotal.com/api/v3/urls"
            report_url = "https://www.virustotal.com/api/v3/urls/" + sitename_base64[2:length-1]
            payload = "url=" + sitename
            
            response = requests.post(url, data=payload, headers=headers)
            if(response.status_code == 200):
                time.sleep(3)
                report_response = requests.get(report_url, headers=headers)
                json_data=report_response.json()
                with open(url_scan_path + sitename + url_ext, 'w') as outfile:
                    json.dump(json_data, outfile)
            else:
                print("Error")

def scan_url(change_url, c):
    t1 = Worker(change_url, c)
    t1.setDaemon(True)
    t1.start()
    

 

