"""
####  Water Balloon  ####

Once a water balloon pops, is soaks the area around it. The ground gets drier the further away you travel from the balloon.
The effect of a water balloon popping can be modeled using a list. Create a function that takes a list which takes the pre-pop state and returns the state after the balloon is popped. The pre-pop state will contain at most a single balloon, whose size is represented by the only non-zero element.


[Examples]

___
pop([0, 0, 0, 0, 4, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]

pop([0, 0, 0, 3, 0, 0, 0]) ➞ [0, 1, 2, 3, 2, 1, 0]

pop([0, 0, 2, 0, 0]) ➞ [0, 1, 2, 1, 0]

pop([0]) ➞ [0]
_____



[Notes]

___
*) Length of input list is always odd.
*) The input list will always be the exact length it takes for there to be exactly one border zero.
*) If the input list consists only of zeroes, return the same list.
___



[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
len() Function
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
max() Function
https://thepythonguru.com/python-builtin-functions/max/
Returns the largest of the input values.Its syntax is as follows...
_________
_________
Python range() function explained with examples
https://pynative.com/python-range-function/
Python range() function explained with examples
_________
_________
Indexing and Slicing for Lists and other Sequential Types
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
Python, one of the most in-demand machine learning languages, supports slice notation for any sequential data type like lists, strings, and others. Discover more about …
_________

"""
#Your code should go here:

