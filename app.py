import time 
import threading 
alive = True

def breath():
    while alive:
        print('heart beating ... ')
        time.sleep(1)

def live():
    while alive:
        print('struggle ... ')
        time.sleep(2)

breath_t = threading.Thread(target=breath); breath_t.daemon =True 
live_t = threading.Thread(target=live); live_t.daemon = True
breath_t.start()
live_t.start()
input()