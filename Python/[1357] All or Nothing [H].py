"""
####  All or Nothing  ####

Suppose a student can earn 100% on an exam by getting the answers all correct or all incorrect. Given a potentially incomplete answer key and the student's answers, write a function that determines whether or not a student can still score 100%. Incomplete questions are marked with an underscore, "_".
___
["A", "_", "C", "_", "B"]   # answer key
["A", "D", "C", "E", "B"]   # student's solution

➞ True

# Possible for student to get all questions correct.

["B", "_", "B"]   # answer key
["B", "D", "C"]   # student's solution

➞ False

# First question is correct but third is wrong, so not possible to score 100%.

["T", "_", "F", "F", "F"]   # answer key
["F", "F", "T", "T", "T"]   # student's solution

➞ True

# Possible for student to get all questions incorrect.
_____



[Examples]

___
possibly_perfect(["B", "A", "_", "_"], ["B", "A", "C", "C"]) ➞ True

possibly_perfect(["A", "B", "A", "_"], ["B", "A", "C", "C"]) ➞ True

possibly_perfect(["A", "B", "C", "_"], ["B", "A", "C", "C"]) ➞ False

possibly_perfect(["B", "_"], ["C", "A"]) ➞ True

possibly_perfect(["B", "A"], ["C", "A"]) ➞ False

possibly_perfect(["B"], ["B"]) ➞ True
_____



[Notes]

Test has at least one question.


[arrays] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Any All
https://www.geeksforgeeks.org/any-all-in-python/
Are two built-ins provided in python used for successive And/Or.
_________
_________
Using the zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
Learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables in parallel and create dictionaries wit …
_________
_________
len() Function
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
set() Function
https://www.programiz.com/python-programming/methods/built-in/set
Creates a Python set from the given iterable. In this tutorial, we will learn about set() in detail with the help of examples.
_________

"""
#Your code should go here:

