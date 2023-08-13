"""
####  Check for Balance  ####

Write a function that takes a string of source code and checks whether the braces/parentheses are balanced. Every ( or { must be closed by a } or ) in the opposite order. Return the index at which an imbalance occurs, or -1 if the string is balanced. If any ( or { are never closed, return the string's length.


[Examples]

___
check_balance("if (a(4) > 9) { foo(a(2)); }") ➞ -1
# Returns -1 because it's balanced.

check_balance("for (i=0;i<a(3};i++) { foo{); )") ➞ 14
# Returns 14 because } is out of order.

check_balance("if (x) {")  ➞ 8
# Returns 8 because { is never closed.
_____



[Notes]

Think about how you can leverage Stack Data Structure.


[algorithms] [data_structures] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to Implement Stack
https://www.educative.io/edpresso/how-to-implement-stack-in-python
A stack is implemented using a list object.
_________
_________
Conditional Statements
https://realpython.com/python-conditional-statements/
In this step-by-step tutorial you'll learn how to work with conditional ("if") statements in Python. Master if-statements step-by-step and see how to write complex deci …
_________
_________
Stack
https://dbader.org/blog/stacks-in-python
Is a collection of objects that supports fast last-in, first-out (LIFO) semantics for inserts and deletes. Unlike lists or arrays, stacks typically don’t allow for rand …
_________

"""
#Your code should go here:

