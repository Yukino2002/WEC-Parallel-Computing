import multiprocessing
import time

# __sum is used to calculate the sum of the different array slices
# we pass the sum of all the different parts of the array independently
def __sum(arr, arr_sum, lock):
    temp_sum = sum(arr)
    lock.acquire()
    arr_sum.value += temp_sum
    lock.release()

if __name__ == '__main__':

    arr = list(map(int, input().split()))
    n = len(arr)
    # multiprocessing library has .Value("data_type", initial_value) function for sharing data between processes
    arr_sum = multiprocessing.Value("i", 0)

    # lock so that more than one process do not access the same variable simultaneously
    lock = multiprocessing.Lock()
    
    processes = []
    # the number of process we want to run independently
    num_processes = 8

    m = n
    # to get the nearest multiple of num_processes, so that we do not miss any elements of the array
    n = (n//num_processes)*num_processes + num_processes

    st = time.time()

    for i in range(num_processes):
        # multiprocessing.process(target, args) -> target = function to be executed by the process, args = arguments to be passed in target
        p = multiprocessing.Process(target = __sum, args = [arr[i*(n//num_processes): min(m, (i+1)*(n//num_processes))], arr_sum, lock])
        processes.append(p)

        # .start() begins the execution of the process
        p.start()

    for p in processes:
        # while executing other processes, our main function would continue to run, so to stop that from happening
        # we use .join() which stops the current program till the other processes join
        p.join()

    ed = time.time()
    
    print(arr_sum.value)
    print(ed - st)