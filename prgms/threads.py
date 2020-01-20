# By default main thread is there

from threading import *
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1=hello()
t2=hi()
t1.start()
t2.start()

# After completing t1 and t2 joining / complete execution then allowed to execute Main thread
t1.join()
t2.join()

print("Bye")  #Its executed  by Main thread