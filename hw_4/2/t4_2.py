

import time
import math
import os
from functools import partial
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from tqdm import tqdm


def exec_integrate(xy, f, n_iter):
    x = xy[0]
    y = xy[1]
    return single_integrate(f, x, y, n_iter)

def closure(f, n_iter):
    return partial(exec_integrate, f=f, n_iter=n_iter)

def single_integrate(f, a, b, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc

def integrate(f, a, b, executor_class, n_jobs=1, n_iter=10000000):
    executor = executor_class(n_jobs)
    slices = [[a+(b-a)*i/n_jobs, a+(b-a)*(i+1)/n_jobs] for i in range(n_jobs)]

    result = sum(executor.map(closure(f, n_iter//n_jobs), slices))
    return result

eps = 1e-6
num_workers = range(1, os.cpu_count()+1)
file = open("results2.txt", 'w')
for workers in tqdm(num_workers):

    thread_start = time.time()
    thread_result = integrate(math.cos, 0, math.pi/2, ThreadPoolExecutor, workers)
    thread_time = time.time() - thread_start

    process_start = time.time()
    process_result = integrate(math.cos, 0, math.pi/2, ProcessPoolExecutor, workers)
    process_time = time.time() - process_start

    file.write("-------------------\n")
    file.write("NUM WORKERS: {}\n".format(workers))
    file.write("THREAD TOTAL TIME: {}\n".format(thread_time))
    file.write("VS\n")
    file.write("PROCESS TOTAL TIME: {}\n".format(process_time))

    
    assert abs(thread_result-single_integrate(math.cos,0, math.pi/2)) < eps
    assert abs(thread_result-process_result) < eps





    
