import _thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{threadName} ke {count}")

_thread.start_new_thread(print_time,("Thread A",2))
_thread.start_new_thread(print_time,("Thread B",4))

while 1:
    pass