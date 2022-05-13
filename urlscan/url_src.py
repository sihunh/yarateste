import sys
import requests
from data import * 

def url_src(change_url, c):
    sys.stdout = open(src_file + str(c) + src_ext, 'w', encoding='utf-8')
    htmls = requests.get(change_url) 
    print(htmls.text)
    sys.stdout.close()