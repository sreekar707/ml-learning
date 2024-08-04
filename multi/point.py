import threading
import time

def numbers():
    for i in range(5):
        time.sleep(2)
        print(f"the numbers are {i}")
        
    
def letters():  
    for letter in "abcde":
        time.sleep(2)
        print(f"the letters are {letter}")
        

t1=threading.Thread(target=numbers)
t2=threading.Thread(target=letters)
        
t=time.time()
t1.start()
t2.start()
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)