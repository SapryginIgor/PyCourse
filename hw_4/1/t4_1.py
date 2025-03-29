import time
from threading import Thread
from multiprocessing import Process

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1)+fib(n-2)


N = 30
threads = []
processes = []


for _ in range(10):
    threads.append(Thread(target=fib, args=(N,)))
    processes.append(Process(target=fib, args=(N,)))

thread_start = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
thread_total_time = time.time() - thread_start

processes_start = time.time()
for p in processes:
    p.start()
for p in processes:
    p.join()
process_total_time = time.time() - processes_start

print("THREAD TOTAL TIME: ", thread_total_time)
print("VS")
print("PROCESS TOTAL TIME: ", process_total_time)

