# report랑 scan 따로 구현 해야함 report를 받아와야함 검사 시간 1분 소요 된다고 하니 스레드로 돌려야할듯함
# url 뒤에 붙는거는 인식을 못함 값들 예 google.com/~~ 이뒤에값 인식을 못함
import json
import requests
from data import *
import threading
import time
import base64

headers = {
        "Accept": "application/json",
        "x-apikey": "458e61cec8e8163ea8ffff08a8d97a4770dd10df103e5e276c0fcab773b82f9c",
        "Content-Type": "application/x-www-form-urlencoded"
}
class Worker(threading.Thread):
    def __init__(self, change_url, c, before_url):
        super().__init__()
        self.change_url = str(change_url)   
        self.c = c          
        self.before_url= before_url
    
    def run(self):
        if "www" in self.change_url:
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
        
        if self.before_url == sitename:
            return self.before_url

        url = "https://www.virustotal.com/api/v3/urls"
        report_url = "https://www.virustotal.com/api/v3/urls/" + sitename_base64[2:length-1]
        payload = "url=" + sitename
        
        response = requests.post(url, data=payload, headers=headers)
        if(response.status_code == 200):
            time.sleep(30)
            report_response = requests.get(report_url, headers=headers)
            json_data=report_response.json()
            with open(url_scan_path + sitename + "_" + str(self.c) + url_ext, 'w') as outfile:
                json.dump(json_data, outfile)
            return sitename
        else:
            print("Error")

def scan_url(change_url, c, before_url):
    t1 = Worker(change_url, c, before_url)
    t1.start()
    

 

