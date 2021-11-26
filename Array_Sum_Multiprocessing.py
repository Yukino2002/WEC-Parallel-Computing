import multiprocessing

# __sum is used to calculate the sum of the different array slices
# we pass all the different parts of the array independently
def __sum(arr, arr_sum):
    arr_sum.value += sum(arr)

if __name__ == '__main__':
    arr = [x for x in range(101)]
    n = len(arr)

    # multiprocessing library has .Value("data_type", initial_value, lock) function for sharing data between processes
    arr_sum = multiprocessing.Value("i", 0, lock = False)

    # initialising a list to store the details of all the processes we opened
    processes = []
    # the number of process we want to run independently
    num_processes = 8

    m = n
    # to get the nearest multiple of num_processes, so that we do not miss any elements of the array
    n = (n//num_processes)*num_processes + num_processes

    for i in range(num_processes):
        # multiprocessing.process(target, args) -> target = function to be executed by the process, args = arguments to be passed in target
        p = multiprocessing.Process(target = __sum, args = [arr[i*(n//num_processes): min(m, (i+1)*(n//num_processes))], arr_sum])
        processes.append(p)

        # .start() begins the execution of the process
        p.start()

    for p in processes:
        # while executing other processes, our main function would continue to run, so to stop that from happening
        # we use .join() which stops the current program till the other processes join
        p.join()

    # displlaying the details of the processes and the sum of the array
    print(processes, "\n")
    print(arr_sum.value)