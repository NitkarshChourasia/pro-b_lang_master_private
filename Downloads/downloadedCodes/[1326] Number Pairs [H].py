"""
####  Number Pairs  ####

Create a function that determines how many number pairs are there embedded in a space-separated string. The first numeric value in the space-separated string represents the count of the numbers, thus, excluded in the pairings.


[Examples]

___
number_pairs("7 1 2 1 2 1 3 2") ➞ 2
# (1, 1), (2, 2)

number_pairs("9 10 20 20 10 10 30 50 10 20") ➞ 3
# (10, 10), (20, 20), (10, 10)

number_pairs("4 2 3 4 1") ➞ 0
# although two 4's are present but
# the first one is discounted
_____



[Notes]

Always take into consideration the first number in the string is not part of the pairing, thus, the count. It may not seem so useful as most people see it, but it's mathematically significant if you deal with set operations.


[arrays] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
Returns the number of times the specified element appears in the list.
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
set() Method
https://www.programiz.com/python-programming/methods/built-in/set
Creates a Python set from the given iterable. In this tutorial, we will learn about set() in detail with the help of examples.
_________
_________
split() Method
https://www.programiz.com/python-programming/methods/string/split
Breaks up a string at the specified separator and returns a list of strings.
_________
_________
Dictionary Comprehension
https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
Learn all about Python dictionary comprehension: how you can use it to create dictionaries, to replace (nested) for loops or lambda functions with map(), filter() and r …
_________

"""
#Your code should go here:

