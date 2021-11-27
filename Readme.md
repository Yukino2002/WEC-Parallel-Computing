<h1><b>WEC-Systems-Parallel-Computing-Assignment:</b></h1>
<h2><b>Solution:</b></h2>



</br><b>Task 1:</b> Finding sum of array</br></br>
One can implement the following task using multiple methods. I solved it in Python by using the multiprocessing module available.

</br>In the main function, I initialised an array. The user needs to enter the elements of the array.

I decided to split the process of adding all the elements of the array into 8 independent processes. Each process would calculate the sum of some part of the array independently, and then finally display the total sum by adding their independently calculated sums.

To implement this, I declared a variable 'arr_sum' using the multiprocessing.Value() function which gives us a ctype object from shared memory to be used by multiple processes. Shared memory is memory that might be accessed simultaneously by more than one processes with an intent to share data among them. In the .Value("data_type", initial_value) call, we pass in the type of variable(int or float), and also an initial value.

</br>I sliced the array into 8 subarrays, and defined a function '__sum(arr, arr_sum)'. The first argument took the different subarrays, and the second was the variable we declared to store the total sum of all the prrocesses.

Using a loop, I used the multiprocessing.Process() function to initiate all the processes. The .Process(target, args) took two arguments, the function that the process needed to execute and the arguments, that the target function needed to be executed.

I also appended all the process details in a list, and started all of them by using the .start() function.

</br>All the processes, now started computing the sum of their subarray independently using the inbuilt sum() function in python, and added it to 'arr_sum'.

Then I used another loop to join all the processes back to the main process after their execution. The .join() stops the main program from running the next set of commands until all the processes join back.

</br>Finally, I displayed total sum of the array calculated through multiprocessing.



</br></br><b>Task 2:</b> Parallel program for finding shortest distance for all nodes from a given node in an unweighted graph:</br></br>
The shortest path of all the nodes from a particular node is calculated using BFS or Breadth First Search. It was evident that the original BFS algorithm had to be modified someway to initialise multiple processes to solve the question parallelly. But if I tried to implement multiprocessing on the entire algorithm, it would show error, as too many processes would get opened at once. So, I tried applying multiprocessing on every level of BFS. For every node in a particular level, I calculated the number of its unvisited neighbours and appended them to another list.

</br>Ex: nodes(n) = 6, edges(e) = 4, e = {(0, 1), (0, 2), (1, 5), (2, 3), (2, 4)}, source(s) = 0
The consecutive levels would be as follows:
</br>-> [0]
</br>-> [1, 2]
</br>-> [[5], [3, 4]] -> [5, 3, 4]
</br> Now, we have a list of lists returned to us by the 'Neighbours' function. This is basically, our next level, so we can just make it into one single list, flatten it out in a way. We are replacing our level with the next set of unvisited neighbours everytime.

</br>We applied the idea of multiprocessing to find the next level of unvisited neighbours for every level. We used the pool.map() to do so. The .Pool() function declares a pool class, where we need to specify how many processes we want to simultaneously run. We then map the pool class varaible to the function we want to execute parallelly, and pass the list of arguments required to execute the function. The most effective part about .Pool() is that we do not need to explicitly declare all the processes, the pool class automatically does that, we just need to specify the maximum number of processes to be opened.

</br>The shortest distance can be easily calculated because that aspect of the solution is no different from the regular BFS algorithm, i.e., Distance[node] = Distance[parent] + 1. We also do not need to worry about mulitple traversals as we use the Visited array to store whether they have already been visited or not.

</br>Finally, I print the list of shortest distance of all the nodes from the source. (All other nodes with distance zero apart from the source, are inaccessible. They can't be reached because they are not connected)