<<<<<<< HEAD
# selenium, yara, chromedrivermanger, bs4
from yara_scan import *
from url_src import *
from data import *
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

def PWC():

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=\\test_profile")
    
    service = ChromeService(executable_path=ChromeDriverManager().install()) # 크롬 드라이버 자동으로 받아옴
    change_url = 'https://google.com'
    c=0

    driver = webdriver.Chrome(service=service, chrome_options=options)
    driver.implicitly_wait(3)
    # url에 접근한다.
    driver.get(change_url)

    while(1): # url이 변경되면 다시 받아옴
        if(change_url != driver.current_url):
            driver.implicitly_wait(3)
            change_url = driver.current_url
            url_src(change_url,c)
            pt_search(src_file + str(c) + src_ext, c, change_url)
            c+=1
            if c == 50: c=0 #50개 채우면 다시 0부터 덮어씌움
=======
from yara_scan import *
from url_src import *
from data import *
from re import search
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

def PWC():

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=\\test_profile")
    
    service = ChromeService(executable_path=driver_path)
    change_url = 'https://google.com'
    c=0

    driver = webdriver.Chrome(service=service, chrome_options=options)
    driver.implicitly_wait(3)
    # url에 접근한다.
    driver.get(change_url)

    while(1): # url이 변경되면 다시 받아옴
        if(change_url != driver.current_url):
            driver.implicitly_wait(3)
            change_url = driver.current_url
            url_src(change_url,c)
            pt_search(src_file + str(c) + src_ext, c, change_url)
            c+=1
            if c == 50: c=0 #50개 채우면 다시 0부터 덮어씌움
>>>>>>> 802554d90f9aa68f63f58425fc10c040e174b89e
            