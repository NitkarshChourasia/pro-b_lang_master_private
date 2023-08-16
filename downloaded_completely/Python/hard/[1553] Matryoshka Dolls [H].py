"""
####  Matryoshka Dolls  ####

Matryoshka dolls are traditionally wooden dolls that can be nested by fitting smaller dolls into larger ones. Suppose lists can be nested similarly, placing smaller lists into larger ones, in the following sense:
List A can be nested inside List B if:

For example, if A = [2, 3, 9, 5] and B = [10, 2, 1], then A can be nested inside B, since:
___
*) min(A) = 2 > 1 = min(B) and
*) max(A) = 9 < 10 = max(B)
___

Create a function that returns True if every single sub-list inside a list can be nested Matroyshka style, and False otherwise.


[Examples]

___
matryoshka([[2, 2, 7], [3, 4, 5, 6], [4, 5]]) ➞ True
# [4, 5] nested inside [3, 4, 5, 6], [3, 4, 5, 6] nested inside [2, 2, 7], etc.
# Dolls nested from largest to smallest.

matryoshka([[4, 5], [6, 3], [7, 6, 5, 4, 3, 2], [8, 1]]) ➞ True
# Dolls nested from smallest to largest.

matryoshka([[7, 1], [7, 6, 5, 4, 3, 2], [6, 3], [4, 5]]) ➞ False
# [7, 1] and [7, 6, 5, 4, 3, 2] share the same max.
# Second doll cannot be nested properly inside first doll.

matryoshka([[1, 5], [2, 6], [3, 7]]) ➞ False
# Elements are overlapping, cannot be nested.
_____



[Notes]

___
*) Sublists can be nested from smallest to largest or largest to smallest.
*) Elements must be strictly nested - e.g. no two lists can share either the same MAX or the same MIN (see example #3).
*) Sublists may not necessarily have unique elements (see example #1).
*) Sublists can be in any order (see example #2).
___



[arrays] [logic] [sorting] [validation] 



-------------------------------------------------------------------
[Resources]
_________
all() Method
https://www.programiz.com/python-programming/methods/built-in/all
Returns True when all elements in the given iterable are true. If not, it returns False.
_________
_________
zip() Function
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it. In this tutorial, we will learn about Python zip() in detail with the help of examples.
_________

"""
#Your code should go here:

