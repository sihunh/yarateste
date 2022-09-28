from multiprocessing import Process
from PWC import *
from monitoring import *

def browser():
    p = Process(target=PWC)
    p1 = Process(target=monitoring)
    p.start()
    p1.start()
   
   