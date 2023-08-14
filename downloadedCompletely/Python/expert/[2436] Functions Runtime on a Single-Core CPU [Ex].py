"""
####  Functions Runtime on a Single-Core CPU  ####

There are n functions to be executed on a single processor. They have id = range(n), from 0 to n - 1. The processor decides how to queue the functions for execution. In the end, there is a log of when a particular function started to run and when it was finished. There are two events: "s"-start, "e"-end. The log entries have the following format, a tuple: (function_id, event, time_stamp).
The total picture can be complicated. For example f1 started, then f2 started, which means f1 becomes idle while f2 runs. When f2 finishes, immediately f1 continues running until the end. The running functions are put into a stack (first in last out). The end event can only happen for the top function in the stack. Then the next function, below the top, continues to run. The start event can happen at any point, meaning that the running function stops execution while the new function runs. It is also possible that some functions are recursive in nature, so f1 starts, f1 starts again, f1 finishes which is a second instance, f1 first instance finishes. If the stack is not empty, the processor is running.
Develop a solution to compute all functions runtime given n number of functions and the log entries list.


[Examples]

___
functions_runtime(1, [(0, "s", 0), (0, "e", 1)]) ➞ [1]
# f0 started at 0, f0 finished at 1 -> total runtime for one function is 1 – 0 = 1

functions_runtime(2, [(0, "s", 0), (0, "e", 3), (1, "s", 5), (0, "s", 6), (0, "e", 8), (1, "e", 9)]) ➞ [5, 2]
# (0, "s", 0), (0, "e", 3) -> f0 runs for 3 seconds
# (0, "s", 6), (0, "e", 8) -> f0 runs for 2 seconds
# f1 runs from 5 to 6 -> 1 second
# f1 runs from 8 to 9 -> 1 second
# Thus in total f0 ran for 5 seconds, f1 ran for 2 seconds

functions_runtime(2, [(0, "s", 0), (1, "s", 2), (1, "e", 6), (0, "e", 7)]) ➞ [3, 4]
# f0 runs in intervals (0, 2), (6, 7) -> 3 seconds in total
# f1 runs in interval (2, 6) -> 4 seconds
_____



[Notes]

N/A


[algorithms] [control_flow] [data_structures] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Stack in Python
https://www.geeksforgeeks.org/stack-in-python/
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and a …
_________

"""
#Your code should go here:

