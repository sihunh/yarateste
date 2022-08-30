import yara
import os
import sys
from D_alert import * 
from url_scan import *
from data import *

def pt_search(target_path, c ,change_url):
    sys.stdout = open(log_file + str(c) + ".txt", 'w', encoding='utf-8')

    filenames = os.listdir(yara_rules_path)
    matchnum = 0
    filenum = 0
    for filename in filenames:
        full_name = os.path.join(yara_rules_path, filename)
        ext = os.path.splitext(full_name)
        if ext[1] == '.yar':
            filenum+=1
            print(full_name)
            try:
                rules = yara.compile(filepath=full_name)
                match = rules.match(target_path)
            except yara.libyara_wrapper.YaraSyntaxError:
                print("*syntax Error*")
                continue
            except UnicodeDecodeError:
                print("*unicode decode error*")
                continue
            if len(match):
                matchnum = len(match['main'][0]['strings'])
                print("Detect num : ", matchnum)

                for i in match['main'][0]['strings']:
                    print("Detect : ", i)
            else:
                print("No Detect")
    print("file num : ", filenum)
    sys.stdout.close()
    if matchnum: 
       d_alert()
       scan_url(change_url, c)
        
    