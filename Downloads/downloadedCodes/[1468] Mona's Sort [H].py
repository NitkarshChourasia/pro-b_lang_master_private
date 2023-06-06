"""
####  Mona's Sort  ####

Mona has created a method to sort a list in ascending order.
Starting from the left of the list, she compares numbers by pairs. If the first pair is ordered [smaller number, larger number], she moves on. If the first pair is ordered [larger number, smaller number], she swaps the two integers before moving on to the next pair. She repeats this process until she reaches the end of the list.
Then, she moves back to the beginning of the list and repeats this process until the entire list is sorted.
If the unsorted list is: [3, 9, 7, 4], she will perform the following steps (note Swaps here refers to cumulative swaps):

Sorting the list [3, 9, 7, 4] takes her 3 swaps. Write a function that takes in an unsorted list and returns the number of swaps it takes for the list to be sorted according to Mona's algorithm.


[Examples]

___
number_of_swaps([5, 4, 3]) ➞ 3

number_of_swaps([1, 3, 4, 5]) ➞ 0

number_of_swaps([5, 4, 3, 2]) ➞ 6
_____



[Notes]

N/A


[loops] [scope] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
Python While Loops
https://www.w3schools.com/python/python_while_loops.asp
While loops are used and restrictions are set such that the loop keeps recurring until it reaches a desired checkpoint
_________

"""
#Your code should go here:

