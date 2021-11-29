<h1><b>WEC-Systems-Parallel-Computing-Assignment:</b></h1>
<h1><b>Solution:</b></h1>

</br><h4>One can implement the following tasks using multiple methods. I solved it in Python by using the multiprocessing module available.</h4>

</br><h2><b>Task 1: Finding sum of array</b></h2>

</br><h3><b>Slicing the array:</h3></b></br>

I decided to split the process of adding all the elements of the array into 8 independent processes. Each process would calculate the sum of some part of the array independently, and then finally display the total sum by adding their independently calculated sums. One can also divide it into more than 8 processes, but due to the overhead of creating so many processes, the execution time will increase.

</br><h3><b>Defining the variables and functions:</b></h3></br>

To implement this, I declared a variable 'arr_sum' using the multiprocessing.Value() function which gives us a ctype object from shared memory to be used by multiple processes. Shared memory is memory that might be accessed simultaneously by more than one processes with an intent to share data among them. In the .Value("data_type", initial_value) call, we pass in the type of variable(int or float), and also an initial value.

</br>I sliced the array into 8 subarrays, and defined a function '__sum(arr, arr_sum, lock)'. The first argument took the different subarrays, the second was the variable we declared to store the total sum of all the prrocesses and lock is discussed below.

</br><h3><b>Initialising processes parallelly:</b></h3></br>

Using a loop, I used the multiprocessing.Process() function to initiate all the processes. The .Process(target, args) took two arguments, the function that the process needed to execute and the arguments, that the target function needed to be executed.

I also appended all the process details in a list, and started all of them parallelly using .start() function.

</br><h3><b>Calculating the sum:</b></h3></br>

All the processes, now started computing the sum of their subarray independently using the inbuilt sum() function in python. To update the total sum in 'arr_sum' in the shared memory, I also used locks to prevent race condition. Race condition occurs when multiple processes try to change the same data or variable at the same time. This can result in unpredictable outputs. We use lock.acquire() and lock.release() to place and remove the lock respectively, once a lock is placed it cannot be accessed by another process till the lock is removed.

Then I used another loop to join all the processes back to the main process after their execution. The .join() stops the main program from running the next set of commands until all the processes join back.

</br><h3>Finally, I displayed total sum of the array calculated through multiprocessing.</h3>


</br><h2><b>Task 2: Finding shortest distance for all nodes from a given node in an unweighted graph</b></h2>

</br><h3><b>The modified BFS algorithm:</h3></b></br>

The shortest path of all the nodes from a particular node is calculated using BFS or Breadth First Search. It was evident that the original BFS algorithm had to be modified someway to initialise multiple processes to solve the question through multiprocessing. But if I tried to implement multiprocessing on the entire algorithm, it would fail to run, as too many processes would be opened at once. So, I tried to apply the idea of running processes parallelly on every level of BFS. For every node in a particular level, I calculated the number of its unvisited neighbours and appended them to another list.

</br>Ex: nodes(n) = 6, edges(e) = 4, e = {(0, 1), (0, 2), (1, 5), (2, 3), (2, 4)}, source(s) = 0
The consecutive levels would be as follows:
</br>-> [0]
</br>-> [1, 2]
</br>-> [[5], [3, 4]] -> [5, 3, 4]
</br> Now, we have a list of lists returned to us by the 'Neighbours' function. This is basically, our next level, so we can just make it into one single list. We are replacing our current level with the next set of unvisited neighbours every iteration.

</br><h3><b>Using the Pool() function:</h3></b></br>

We applied the idea of multiprocessing to find the next level of unvisited neighbours for every level. We used the pool.map() to do so. The .Pool() function declares a pool class, where we need to specify how many processes we want to simultaneously run. We then map the pool class varaible to the function we want to execute parallelly, and pass the list of arguments required to execute the function. Process() allocates all the tasks in the memory while Pool() allocates only currently executing processes in memory. We also don't need to explicitly declare all the processes in Pool() function, just specify the maximum number of processes we want to run at once.

</br><h3><b>Working of the algorithm:</h3></b></br>

The shortest distance can be easily calculated because that aspect of the solution is no different from the regular BFS algorithm, i.e., Distance[node] = Distance[parent] + 1. We also do not need to worry about mulitple traversals as we use the 'Visited' array to store whether they have already been visited or not.

</br>After running the program, the user only needs to enter the number of nodes, edges and the edges data set. We need to pass the source from where we want to calculate all the distances.

</br>Finally, I print the list of shortest distances of all the nodes from the source. (All other nodes with distance zero apart from the source, are inaccessible. Meaning, they can not be reached because they are not connected)

</br></br><h3>From the results obtained, we can see that our bfs algorithm using multiprocessing is slower compared to the serial bfs code we designed.</h3>