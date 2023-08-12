"""
####  Convert from lambda to def  ####

Given a piece of code with a function assigned by lambda, rewrite it into a function assigned by def. The code given would be in string.


[Overview]

This is a quick example of a lambda expression:
___
func = lambda a, b: a * (b - 2)
_____

... is the same as ...
___
def func(a, b):
  return a * (b - 2)
_____



[Examples]

___
lambda_to_def("func = lambda w: w + 'lambda'") ➞ "def func(w):\n\treturn w + 'lambda'"

lambda_to_def("z = lambda lambdadef: lambdadef.split(':')") ➞ "def z(lambdadef):\n\treturn lambdadef.split(':')"
_____

Visualisation:
___
print(lambda_to_def("func = lambda w: w + 'lambda'"))

def func(w):
  return w + 'lambda'
_____

___
print(lambda_to_def("z = lambda lambdadef: lambdadef.split(':')"))

def z(lambdadef):
  return lambdadef.split(':')
_____



[Notes]

___
*) The new code should follow PEP8 guidelines.
*) For the sake of convenience, use \t for indentation.
*) Assume all lambda expressions are valid.
___



[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.programiz.com/python-programming/methods/string/split
Breaks up a string at the specified separator and returns a list of strings.
_________
_________
strip() Method
https://www.programiz.com/python-programming/methods/string/strip
Returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed).
_________
_________
find() Method
https://www.programiz.com/python-programming/methods/string/find
Returns the index of first occurrence of the substring (if found). If not found, it returns -1.
_________
_________
Lambda Functions
https://www.w3schools.com/python/python_lambda.asp
Is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
_________

"""
#Your code should go here:

