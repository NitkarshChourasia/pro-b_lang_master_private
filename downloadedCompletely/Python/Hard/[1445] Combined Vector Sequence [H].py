"""
####  Combined Vector Sequence  ####

The goal is to test if a consecutive sequence is formed. A consecutive sequence is defined as sequence of incrementing numbers (e.g. 1, 2, 3 or 5, 6, 7, 8). The twist is that you have to consider the combination of vectors as shown.
___
[3 5 1 -5 ]  =>  [3+4  5+3  1+8  15-5]  =  [7 8 9 10]  =>  true
[4 3 8 15]
_____

Also important is that the vectors can be of different sizes, where excess numbers in the longer one will be paired with 0s from the other one.
___
[2 2 2  ]  =>  [2+5  2+6  2+7  10+0]  = [ 7 8 9 10]  =>  true
[5 6 7 10]
_____



[Notes]

___
*) Each array has at least two elements.
*) Try the harder version.
___



[arrays] [logic] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to Find the Sum of Two Lists
https://www.kite.com/python/answers/how-to-find-the-sum-of-two-lists-in-python
Adding two lists results in a new list where each element is the sum of the elements in the corresponding positions of the two lists. For example, [1, 2, 3] + [4, 5, 6] …
_________
_________
Check if List Contains Consecutive Numbers
https://www.geeksforgeeks.org/python-check-if-list-contains-consecutive-numbers/
Given a list of numbers, write a Python program to check if the list contains consecutive integers.
_________
_________
Itertools.zip_longest() Method
https://www.geeksforgeeks.org/python-itertools-zip_longest/
This iterator falls under the category of Terminating Iterators. It prints the values of iterables alternatively in sequence. If one of the iterables is printed fully, …
_________

"""
#Your code should go here:

