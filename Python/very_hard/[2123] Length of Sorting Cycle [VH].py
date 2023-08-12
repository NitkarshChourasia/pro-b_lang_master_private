"""
####  Length of Sorting Cycle  ####

Given an element in a list, write a function to determine the length of a particular element's sorting cycle. Given one element in the list, a sorting cycle is the number of swaps it takes so that the last displaced swapped item is back in its correct order.
What is the length of 9's sorting cycle?
___
[1, 9, 8, 4, 7, 2, 6, 3, 5]
[1, 5, 8, 4, 7, 2, 6, 3, 9]  # 9 swaps with 5; 9 is in its correct spot.
[1, 7, 8, 4, 5, 2, 6, 3, 9]  # 5 replaces 7; 5 is in its correct spot.
[1, 6, 8, 4, 5, 2, 7, 3, 9]  # 7 replaces 6; 7 is in its correct spot.
[1, 2, 8, 4, 5, 6, 7, 3, 9]  # 6 replaces 2; 6 is in its correct spot and 2 is in it's correct spot - done!
_____

9's cycle is of length 4. Notice how every number included in the swap (9, 5, 7, 6, and 2) are all in their rightful places. This is because each of these numbers are in the same sorting cycle.
Here is another example. Using the same list above, what is the length of 8's sorting cycle?
___
[1, 9, 8, 4, 7, 2, 6, 3, 5]
[1, 9, 3, 4, 7, 2, 6, 8, 5] # 8 replaces 3; 8 and 3 are both in their correct spots.
_____

8's cycle is of length 1.


[Examples]

___
cycle_length([1, 5, 4, 3, 2, 6], 4) ➞ 1

cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 7) ➞ 7

cycle_length([43, 81, 88, 93, 17, 32, 19, 11], 93) ➞ 5

cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 1) ➞ 0
_____



[Notes]

___
*) Output 0 if the element is already in its correct order (see example #4).
*) If this question is confusing, think about it in this way:
Normally, swapping two numbers to place the first number in the correct order does not place the second number in its correct order. In other words, it's a single-party beneficial sort.
The sorting cycle ends when a swap leads to a mutually beneficial sort, e.g. swapping two numbers leads the first AND the second number to be put to their rightful places.
*) This question is tricky — see the Comments for a hint if you're stuck.
___



[language_fundamentals] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
sorted() Function
https://www.w3schools.com/python/ref_func_sorted.asp
Returns a sorted list of the specified iterable object. You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numeri …
_________
_________
index() Method
https://www.w3schools.com/python/ref_list_index.asp
Returns the position at the first occurrence of the specified value.
_________
_________
Program to Find Shortest Cycle Length Holding Target in Python
https://www.tutorialspoint.com/program-to-find-shortest-cycle-length-holding-target-in-python
Suppose we have adjacency list of a directed graph, where each list at index i is represented connected nodes from node i. We also have a target value. We have to find …
_________
_________
Find n-length Cycles in Python
https://stackoverflow.com/questions/29518527/find-n-length-cycles-in-python
I'm new to Python, and have spent a while without programming so would very much appreciate your help. I have to look for all n-length cycles in a given data-structure …
_________

"""
#Your code should go here:

