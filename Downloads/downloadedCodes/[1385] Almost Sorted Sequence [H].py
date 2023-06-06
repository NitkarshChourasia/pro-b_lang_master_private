"""
####  Almost Sorted Sequence  ####

An almost-sorted sequence is a sequence that is strictly increasing or strictly decreasing if you remove a single element from the list (no more, no less). Write a function that returns True if a list is almost-sorted, and False otherwise.
For example, if you remove 80 from the first example, it is perfectly sorted in ascending order. Similarly, if you remove 7 from the second example, it is perfectly sorted in descending order.


[Examples]

___
almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41] ) ➞ True

almost_sorted([6, 5, 4, 7, 3]) ➞ True

almost_sorted([6, 4, 2, 0]) ➞ False
// Sequence is already sorted.

almost_sorted([7, 8, 9, 3, 10, 11, 12, 2]) ➞ False
// Requires removal of more than 1 item.
_____



[Notes]

___
*) Completely sorted lists should return False.
*) Lists will always be > 3 in length (to remove ambiguity).
*) Numbers in each input list will be unique - don't worry about "ties".
___



[arrays] [sorting] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Counting the Frequencies in a List Using Dictionary
https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/
Given an unsorted list of some elements(may or may not be integers), Find the frequency of each distinct element in the list using a dictionary.
_________
_________
Counter
https://pymotw.com/2/collections/counter.html
Is a container that keeps track of how many times equivalent values are added. It can be used to implement the same algorithms for which bag or multiset data structures …
_________
_________
Using the Python zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________

"""
#Your code should go here:

