import multiprocessing
import time
import numpy as np
import random

def thread_sum(arr, arr_sum):
    arr_sum.value += sum(arr)
   # print(p.pid)

if __name__ == '__main__':
    arr = []
    for i in range(10000000):
        arr.append(random.randint(0, 10000))
    n = len(arr)

    arr_sum = multiprocessing.Value("d", 0.0, lock = False)
    arr_sum.value = 0

    processes = []
    # for i in range(4):
    n = len(arr)
    
    k = 8
    m = n
    n = (n//k)*k + k
    st = time.time()
    for i in range(k):
        p = multiprocessing.Process(target = thread_sum, args = [arr[i*(n//k): min(m, (i+1)*(n//k))],arr_sum])
        processes.append(p)

        p.start()

    for p in processes:
        p.join()

    ed = time.time()
    print(arr_sum.value, ed-st)

    st = time.time()

    sm = 0
    for i in arr:
        sm+=i
    ed = time.time()
    print(sm,ed - st)