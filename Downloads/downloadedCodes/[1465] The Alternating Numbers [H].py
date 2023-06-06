"""
####  The Alternating Numbers  ####

In this challenge, you have to establish if an integer num is Alternating. To be Alternating, num must be positive and every digit in its sequence must have a different parity than its next and its previous digit.
Given an integer num, implement a function that returns True is num is an Alternating number, or False if it's not.


[Examples]

___
is_alternating(123) ➞ True
# 1 is odd, 2 is even, 3 is odd

is_alternating(67) ➞ True
# 6 is even, 7 is odd

is_alternating(2380) ➞ False
# 2 is even, 3 is odd, 8 is even, 0 is even

is_alternating(75) ➞ False
# 7 is odd, 5 is odd
_____



[Notes]

___
*) A single-digit number is trivially considered Alternating, given the absence of neighboring digits.
*) The first digit has to be compared only to its next neighbor, and the last digit has to be compared only to its previous neighbor.
*) Every non-positive integer must be treated as False.
___



[numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to check a previous index when iterating through a for loop?
https://stackoverflow.com/questions/24149725/how-can-i-check-a-previous-index-when-iterating-through-a-for-loop-python/24149791
I have a list that is somewhat random. I want to iterate through it and do something like this. Obviously, item_5_indexes_ago is not valid python. What should I substit …
_________

"""
#Your code should go here:

