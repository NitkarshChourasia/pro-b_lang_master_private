"""
####  Flatten Nested List Iterator  ####

Implement a class iterator to flatten a nested list of lists of integers. Each list element is either an integer or a list. There can be many levels of nested lists in lists.
The class initializes with a nested list. It also has two methods:

Write the Class implementation for three required methods.


[Examples]

___
ni, actual = NestedIterator([[1, 1], 2, [1, 1]]), []
while ni.hasNext():
    actual.append(ni.next())
actual ➞ [1, 1, 2, 1, 1]

ni, actual = NestedIterator([1, [4, [6]]]), []
while ni.hasNext():
    actual.append(ni.next())
actual ➞ [1, 4, 6]

ni, actual = NestedIterator([[[]], []]), []
while ni.hasNext():
    actual.append(ni.next())
actual ➞ []
_____



[Notes]

N/A


[classes] [conditions] [data_structures] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

