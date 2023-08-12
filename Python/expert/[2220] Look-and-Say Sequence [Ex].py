"""
####  Look-and-Say Sequence  ####

Create a function that takes in two positive integers start and n and returns a list of the first n terms of the look-and-say sequence starting at the given start.
Each term of the look-and-say sequence (except for the first term) is created from the previous term using the following process.
Start with a term in the sequence (for example, 111312211):
___
111312211
_____

Split it into subsequences of consecutive repeating digits:
___
111 3 1 22 11
_____

Count the number of digits in each subsequence:
___
three 1, one 3, one 1, two 2, two 1
_____

Turn everything into digits:
___
3 1, 1 3, 1 1, 2 2, 2 1
_____

Now combine everything into one number:
___
3113112221
_____

So 3113112221 is the next term in the sequence after 111312211.


[Examples]

___
look_and_say(1, 7) ➞ [1, 11, 21, 1211, 111221, 312211, 13112221]

look_and_say(123, 4) ➞ [123, 111213, 31121113, 1321123113]

look_and_say(70, 5) ➞ [70, 1710, 11171110, 31173110, 132117132110]
_____



[Notes]

Your output should be a list of integers.


[numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python 3 List Methods & Functions
http://www.python-ds.com/python-3-list-methods
Extends the list by appending all the items from the iterable. This allows you to join two lists together. This method is equivalent to a[len(a):] = iterable.
_________
_________
itertools.groupby() Method
https://www.geeksforgeeks.org/itertools-groupby-in-python/
Calculates the keys for each element present in iterable. It returns key and iterable of grouped items.
_________
_________
How to Convert an Integer to a String
https://pythonprinciples.com/blog/converting-integer-to-string-in-python/
To convert an integer to a string, use the str() built-in function. The function takes an integer (or other type) as its input and produces a string as its output.
_________

"""
#Your code should go here:

