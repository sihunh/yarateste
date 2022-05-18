from yara_scan import *
from url_src import *
from data import *
from re import search
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from monitoring import *

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=\\test_profile")

change_url = 'https://google.com'
b_siteurl = ''
c=0

driver = webdriver.Chrome(driver_path, chrome_options=options)
driver.implicitly_wait(3)

# url에 접근한다.
driver.get(change_url)
monitoring() # dir 모니터링 시작
while(1): # url이 변경되면 다시 받아옴
    if(change_url != driver.current_url):
        driver.implicitly_wait(3)
        change_url = driver.current_url
        url_src(change_url,c)
        pt_search(src_file + str(c) + src_ext, c, change_url, b_siteurl)
        c+=1
        if c == 50: c=0 #50개 채우면 다시 0부터 덮어씌움
        