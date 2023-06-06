"""
####  Lambda Expressions All the Way Down  ####

Create a function which takes a parameter n and returns a function such that it, when called n times, returns the string "edabit".


[Examples]

___
lambda_depth(0) ➞ "edabit"

lambda_depth(1)() ➞ "edabit"

lambda_depth(2)()() ➞ "edabit"

type(lambda_depth(2)()) ➞ <class: "function">
_____



[Notes]

___
*) num will always be a non-negative integer.
*) If num == 0, return "edabit".
*) If num > 0, return a function.
*) All non-example test cases come in two forms: checking whether lambda_depth(k), after being called k times, returns a string, and checking whether lambda_depth(k) returns a function.
___



[functional_programming] [higher_order_functions] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Lambda Expressions
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used whe …
_________
_________
eval() Method
https://docs.python.org/3/library/functions.html#eval
The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object. The expression ar …
_________

"""
#Your code should go here:

