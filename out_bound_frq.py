import time
import os
import collections
import re

def out_bound_freq():
    for i in range(0,100): 
        os.system('netstat -n >> ../out_bound.txt') # netstat 명령어 써서 현재 outbound 하는 패킷 가져와서 텍스트로 저장

    time.sleep(1)
    ipnPort = re.findall(r'\d+[.]\d+[.]\d+[.]\d+[:]\d+', open("../out_bound.txt").read().lower()) # 위에서 가져온거 ip만 읽음

    print("OUT BOUND ADRR"+'\t\t'+"FREQ") 
    for x, y in collections.Counter(ipnPort).most_common(): # x는 주소 찾고 y는 갯수
        if str(x).rpartition(':')[0] == '127.0.0.1': # localhost이면 패스
            pass
        else:
            print(str(x)+'\t'+str(y))
