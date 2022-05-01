# 1. 웹 code 추출 해서 yara로 패턴탐지 로그는 50개로 rotate
# 2. 타이포스쿼팅 공격 방지 
# 3. url 블랙리스트

from re import search
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import sys
import yara
import os
from selenium import webdriver

yara_rules_path = "rules\\webshells" 
driver_path = "chromedriver_100.exe" 
change_url = 'https://google.com'
src_file = "websrc\\websrc_"
log_file = "logs\\log_"
src_ext = ".txt"
c=0

def file_src():
    sys.stdout = open(src_file + str(c) + src_ext, 'w', encoding='utf-8')
    htmls = requests.get(change_url) 
    print(htmls.text)
    sys.stdout.close()

def pt_search(target_path):
    sys.stdout = open(log_file + str(c) + ".txt", 'w', encoding='utf-8')

    filenames = os.listdir(yara_rules_path)
    filenum = 0
    for filename in filenames:
        full_name = os.path.join(yara_rules_path, filename)
        ext = os.path.splitext(full_name)
        if ext[1] == '.yar':
            filenum=filenum+1
            print(full_name)
            try:
                rules = yara.compile(filepath=full_name)
                match = rules.match(target_path)
            except yara.libyara_wrapper.YaraSyntaxError:
                print("[*]syntax Error[*]")
                continue
            except UnicodeDecodeError:
                print("[*]unicode decode error[*]")
                continue
            if len(match):
                matchnum = len(match['main'][0]['strings'])
                print("Detect num : ", matchnum)

                for i in match['main'][0]['strings']:
                    print("Detection : ", i)
            else:
                print("No Detect")
        print("file num : ", filenum)
    sys.stdout.close()

driver = webdriver.Chrome(driver_path)
driver.implicitly_wait(3)

# url에 접근한다.
driver.get(change_url)
while(1): # url이 변경되면 다시 받아옴
    if(change_url != driver.current_url):
        driver.implicitly_wait(3)
        change_url = driver.current_url
        #file_src()
        sys.stdout = open(src_file + str(c) + src_ext, 'w', encoding='utf-8')
        htmls = requests.get(change_url) 
        print(htmls.text)
        sys.stdout.close()
        pt_search(src_file + str(c) + src_ext)
        c+=1
        if c == 50: c=0 #50개 채우면 다시 0부터 덮어씌움