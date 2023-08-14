"""
####  Subset of a Cartasian Product  ####

Write a function which takes a list of numbers and returns a list of tuples that is a subset of product of the list with itself and first member of each tuple is less than or equall to the second one.
In mathematical terms:
___
A x A = {(x,y)| x∈A and y∈A}

{(x,y)| x>=y, (x,y) ∈ A x A }
_____



[Examples]

___
relation_list([0, 1, 2, 3]) ➞ [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3)]

relation_lst([858, 544, 164]) ➞ [(164, 164), (164, 544), (164, 858), (544, 544), (544, 858), (858, 858)]

relation_lst([-1]) ➞ [(-1, -1)]

relation_lst([0]) ➞ [(0, 0)]

relation_lst([]), []
_____



[Notes]

The result should be in ascending order.


[loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
Construct Cartesian Product Tuple list
https://www.geeksforgeeks.org/python-construct-cartesian-product-tuple-list/
Sometimes, while working with data, we need to create data as all possible pairs of containers. This type of application comes from web development domain. This link di …
_________
_________
Cartesian Product
https://en.wikipedia.org/wiki/Cartesian_product
In mathematics, the Cartesian product of two sets A and B, denoted A × B, is the set of all ordered pairs (a, b) where a is in A and b is in B.
_________
_________
Get the Cartesian Product of a Series of Lists
https://stackoverflow.com/questions/533905/get-the-cartesian-product-of-a-series-of-lists
How can I get the Cartesian product (every possible combination of values) from a group of lists?
_________

"""
#Your code should go here:

