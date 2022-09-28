from multiprocessing import Process
from PWC import *
from monitoring import *

if __name__ == '__main__':
    p = Process(target=PWC)
    p1 = Process(target=monitoring)
    p.start()
    p1.start()
   
   