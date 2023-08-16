"""
####  The ECG Sequence  ####

In the ECG Sequence (that always starts with the numbers 1 and 2), every number that succeeds is the smallest not already present in the sequence and that shares a factor (excluding 1) with its preceding number. Every number in the ECG Sequence (besides 1 and 2) has a different index from its natural index in a normal numeric sequence. See the example below to establish the ECG Sequence Index of number 3.
___
# Find the smallest number that is not in sequence...
# This number shares a factor with the preceding?

SEQUENCE = [1, 2]

3 = no factors shared with 2
4 = shares factor 2 with number 2

SEQUENCE = [1, 2, 4]

3 = no factors shared with 4
5 = no factors shared with 4
6 = shares factor 2 with number 4

SEQUENCE = [1, 2, 4, 6]

3 = shares factor 3 with number 6

SEQUENCE = [1, 2, 4, 6, 3]

Number 3 is at index 4 in the ECG Sequence.
_____

Given an integer n implement a function that returns its ECG Sequence Index.


[Examples]

___
ecg_seq_index(3) ➞ 4

ecg_seq_index(5) ➞ 9

ecg_seq_index(7) ➞ 13
_____



[Notes]

___
*) ECG is the acronym for the electrocardiogram: if you try to graphically represent the trend of the sequence, a similar scheme appears.
*) Curiosity: every odd prime p in the sequence is preceded by 2p and followed by 3p.
___



[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
gcd() in Python
https://www.geeksforgeeks.org/gcd-in-python/
The Highest Common Factor (HCF) , also called gcd, can be computed in python using a single function offered by math module and hence can make tasks easier in many situ …
_________
_________
List append() Method
https://www.programiz.com/python-programming/methods/list/append
Adds an item to the end of the list. In this tutorial, we will learn about the Python append() method in detail with the help of examples.
_________
_________
List index() Method
https://www.programiz.com/python-programming/methods/list/index
Returns the index of the specified element in the list.
_________
_________
Thinking Recursively in Python
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________

"""
#Your code should go here:

