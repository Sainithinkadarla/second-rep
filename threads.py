import _thread
import time
def method(tname,d):
    c=0
    while c<=5:
        time.sleep(d)
        print("method is running by",tname)
        c+=1
_thread.start_new_thread(method,("thread 1",2,))
_thread.start_new_thread(method,("thread 2",3,))
