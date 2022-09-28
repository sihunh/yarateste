from socket import *
import time

def scan():
    
    port=[80, 20, 21, 22, 23, 25, 53, 5357, 110, 123, 161, 443, 1433, 3306, 1521, 8080, 135, 139, 137, 138, 445, 514, 8443, 3389, 8090, 42, 70, 79, 88, 118, 156, 220]
    start = 0
    end = len(port)
    try:
        target = input('Enter the ip or url : ')
        t_IP = gethostbyname(target)

        print ('Starting scan on host: ', t_IP)

        startTime = time.time()

        s = socket(AF_INET, SOCK_STREAM)
        for i in range(start,end,1):
            conn = s.connect_ex((t_IP, port[i]))
            if(conn == 0):
                print('Port %d IS OPEN!' % (port[i]))
            s.close()

        print('Time taken:', time.time() - startTime)
    except: 
        print('에러')
