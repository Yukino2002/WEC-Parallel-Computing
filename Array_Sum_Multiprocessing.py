import multiprocessing
import time

def __sum(arr, arr_sum):
    arr_sum.value += sum(arr)

if __name__ == '__main__':
    arr = [x for x in range(10)]
    n = len(arr)

    arr_sum = multiprocessing.Value("d", 0.0, lock = False)
    arr_sum.value = 0

    processes = []
    
    k = 8

    m = n
    n = (n//k)*k + k

    st = time.time()

    for i in range(k):
        p = multiprocessing.Process(target = __sum, args = [arr[i*(n//k): min(m, (i+1)*(n//k))], arr_sum])
        processes.append(p)

        p.start()
        print(p.pid)

    for p in processes:
        p.join()

    ed = time.time()
    print()
    print(arr_sum.value, ed-st)