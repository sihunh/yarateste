import yara
import os
import sys
from D_alert import * 
from url_scan import *
from data import *
import random

def pt_search(target_path, c ,change_url):
    file_path= log_file + str(c) + ".json"
    sys.stdout = open(file_path, 'w', encoding='utf-8')

    filenames = os.listdir(yara_rules_path)
    matchnum = 0
    filenum = 0
    print('{')
    for filename in filenames:
        full_name = os.path.join(yara_rules_path, filename)
        ext = os.path.splitext(full_name)
        if ext[1] == '.yar':
            filenum+=1
            print('"'+full_name[6:] + '"',end="")
            try:
                rules = yara.compile(filepath=full_name)
                match = rules.match(target_path)
            except yara.libyara_wrapper.YaraSyntaxError:
                print(":  \"*syntax Error* \",")
                continue
            except UnicodeDecodeError:
                print(":  \"*unicode decode error* \",")
                continue
            if len(match):
                matchnum = len(match['main'][0]['strings'])
                print(":{")
                count = 0
                for i in match['main'][0]['strings']:
                    i = json.dumps(i)
                    print("\"Detect{0}\": {1},".format(count,i))
                    count+=1
                print("\"Detect num\" : {}".format(matchnum))
                print("},")
            else:
                print(": \"No Detect\",")
    print("\"file num\" : {}".format(filenum))
    print('}')
    sys.stdout.close()

    if matchnum: 
       d_alert()
       scan_url(change_url, c)
    
    try:
        f = open(file_path)
        json_data = json.load(f)
        f.close()
    except Exception as e:
        print(f'FILE EXCEPTION: {str(e)}')

    firebase_upload(json_data,'yara_scan', str(c)) # db업로드 :: json_data, colletion_name, file_name
    