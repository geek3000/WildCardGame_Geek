import threading as t
import time
class A(t.Thread):
    def start(self):
        while True:
            print("Ask")
            time.sleep(1)

a = A()
a.start()
i=0
while i<6:
    print("ppppp")
    i+=1
