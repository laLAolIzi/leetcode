import threading
import time
import copy
from queue import Queue

def job(l, q):
    res = sum(l)
    q.put(res)
    def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l),q),name=T%i%i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == __main__:
    l = list(range(1000000))