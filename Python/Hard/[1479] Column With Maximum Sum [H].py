"""
####  Column With Maximum Sum  ####

Given a list of numbers and a value for n, split the numbers into n-sized groups. If we imagine that these groups are stacked on top of each other (see below), return the column number that has the greatest sum. If two or more columns have the same sum, return the one with the smallest column number.


[Example]

___
nums = [4, 14, 12, 7, 14, 16, 5, 13, 7, 16, 11, 19]
n = 4
_____

Gives the array:
___
[[4, 14, 12, 7],
[14, 16,  5, 13],
[7, 16, 11, 19]]

# 1, 2, 3, 4 (column)
# 25, 46, 28, 39 (sum)
_____

You would return 2, as the 2nd column has the greatest sum.


[Notes]

Nums will always divide into equal-length groups.


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
max() Function
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.
_________
_________
enumerate() Method
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________
_________
range() Type
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
How to select every other using slicing in Python?
https://stackoverflow.com/questions/43905817/how-to-select-every-other-using-slicing-in-python
In order to get the joined string for the given integer list a from the second element per list item onwards, you could slice each item of the list to from the second e …
_________
_________
While Loops
https://www.w3schools.com/python/python_while_loops.asp
Requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
_________

"""
#Your code should go here:

