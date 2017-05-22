import os
import threading
import queue

l="""
https://hitomi.la/galleries/98765432.html
https://hitomi.la/galleries/98765431.html
"""

q=queue.Queue()
for i in set(l.split()):
    q.put(i)

class GalDownThread(threading.Thread):
    def __init__ (self):
        threading.Thread.__init__(self)
    def run (self):
        while True:
            try:
                nya = q.get_nowait()
            except:
                print("no more element in the queue. exit. thread.")
                break
            else:
                os.system("gallery-dl " + nya)
                continue

th_box = [ GalDownThread() for __ in range (10) ]
for i in th_box:
    i.start()
for i in th_box:
    i.join()
