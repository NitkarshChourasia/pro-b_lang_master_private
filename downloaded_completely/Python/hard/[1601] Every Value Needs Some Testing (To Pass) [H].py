"""
####  Every Value Needs Some Testing (To Pass)  ####

In this challenge, you have to verify that every, or some, of the given variables, pass a given test condition. There are seven parameters:
___
*) test: A string being the condition to verify.
*) val: A string with two possible values:
everybody if every variable has to pass the test;
somebody if at least one of the variables has to pass the test.
*) a, b, c, d, e: The variables being integers or booleans.
___

Create a function that returns True or False, depending on the result of the test applied to the variables.


[Examples]

___
every_some(">= 1", "everybody", 1, 1, -1, 1, 1) ➞ False
# Is every variable >= 1?

every_some(">= 1", "somebody", -1, -1, -1, -1, 1) ➞ True
# Is some variable >= 1?

every_some("< 4 / 2", "everybody", 1, 2, 1, 0, -10) ➞ False
# Is every variable < 2?
_____



[Notes]

N/A


[conditions] [validation] 



-------------------------------------------------------------------
[Resources]
_________
any() Method
https://docs.python.org/3/library/functions.html#any
Return True if any element of the iterable is true. If the iterable is empty, return False.
_________
_________
all() Method
https://docs.python.org/3/library/functions.html#all
Return True if all elements of the iterable are true (or if the iterable is empty).
_________

"""
#Your code should go here:

