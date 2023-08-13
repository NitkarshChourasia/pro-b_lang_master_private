"""
####  Recaman's Sequence  ####

Starting from zero, the n'th term a(n) is the previous term minus n (i.e. a(n) = a(n-1) - n) but only if this is both positive and has not been previousely generated. If the conditions don't hold then a(n) = a(n-1) + n.
Create a function that takes a number n as an argument and returns a list with the first n numbers in the Recaman's Sequence, as well as a list with the duplicate numbers in such list. The list of duplicates must contain the duplicate numbers ordered by their appearance order in the Recaman's Sequence.

___
recaman(20) ➞ "---> Recaman's sequence: [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43, 62]
---> Duplicates for n = 20: []"

recaman(100) ➞ "---> Recaman's sequence: [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43, 62, 42, 63, 41, 18, 42, 17, 43, 16, 44, 15, 45, 14, 46, 79, 113, 78, 114, 77, 39, 78, 38, 79, 37, 80, 36, 81, 35, 82, 34, 83, 33, 84, 32, 85, 31, 86, 30, 87, 29, 88, 28, 89, 27, 90, 26, 91, 157, 224, 156, 225, 155, 226, 154, 227, 153, 228, 152, 75, 153, 74, 154, 73, 155, 72, 156, 71, 157, 70, 158, 69, 159, 68, 160, 67, 161, 66, 162, 65, 163, 64]
---> Duplicates for n = 100: [42, 43, 78, 79, 153, 154, 155, 156, 157]"
_____



[Notes]

N/A


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Python List –15 Things You MUST Know
https://www.askpython.com/python/list/python-list
Python List is a mutable sequence. We can create a List by placing elements inside a square bracket. The list elements are separated using a comma. We can create nested …
_________
_________
Python String Formatting Best Practices
https://realpython.com/python-string-formatting/
Learn the four main approaches to string formatting in Python, as well as their strengths and weaknesses. You'll also get a simple rule of thumb for how to pick the bes …
_________
_________
Recamán's Sequence
https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence
A well known sequence defined by a recurrence relation, because its elements are related to the previous elements in a straightforward way, they are often defined using …
_________

"""
#Your code should go here:

