<h1><b>WEC-Systems-Parallel-Computing-Assignment:</b></h1>
<h2><b>Solution:</b></h2>



</br><b>Basic Task:</b> Finding sum of array</br></br>
One can implement the following task using multiple methods. I solved it in Python by using the multiprocessing module available.

</br>In the main function, I initialised an array, whose size can be changed. For this task I took it as 101 and stored all the elements from 0-100 in it.

I decided to split the process of adding all the elements of the array into 8 independent processes. Each process would calculate the sum of some part of the array independently, and then finally display the total sum by adding their independently calculated sums.

To implement this, I declared a variable 'arr_sum' using the multiprocessing.Value() function which gives us a ctype object from shared memory to be used by multiple processes. Shared memory is memory that might be accessed simultaneously by more than one processes with an intent to share data among them. In the .Value("data_type", initial_value) call, we pass in the type of variable(int or float), and also an initial value.

</br>I sliced the array into 8 subarrays, and defined a function '__sum(arr, arr_sum)'. The first argument took the different subarrays, and the second was the variable we declared to store the total sum of all the prrocesses.

Using a loop, I used the multiprocessing.Process() function to initiate all the processes. The .Process(target, args) took two arguments, the function that the process needed to execute and the arguments, that the target function needed to be executed.

I also appended all the process details in a list, and started all of them by using the .start() function.

</br>All the processes, now started computing the sum of their subarray independently using the inbuilt sum() function in python, and added it to 'arr_sum'.

Then I used another loop to join all the processes back to the main process after their execution. The .join() stops the main program from running the next set of commands until all the processes join back.

</br>Finally, I displayed the details for all the 8 processes used, and the total sum of the array calculated through multiprocessing.



