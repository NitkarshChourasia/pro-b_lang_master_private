"""
####  Perimeters with a Catch  ####

Write a function that takes a number and returns the perimeter of either a circle or a square. The input will be in the form (letter l, number num) where the letter will be either "s" for square, or "c" for circle, and the number will be the side of the square or the radius of the circle.
Use the following formulas:
___
*) Perimeter of a square: 4 * side.
*) Perimeter of a circle: 6.28 * radius.
___

The catch is you can only use arithmetic or comparison operators, which means:
___
*) No if... else statements.
*) No dictionaries.
*) No lambdas.
*) No formatting methods, etc.
___

The goal is to write a short, branch-free piece of code.


[Examples]

___
perimeter("s", 7) ➞ 28

perimeter("c", 4) ➞ 25.12

perimeter("c", 9) ➞ 56.52
_____



[Notes]

___
*) No rounding is needed.
*) Hint: The Boolean True, used with arithmetic operators, counts as 1, while False counts as 0. That means (a>b)+1 will return 1 or 2, depending on the values of a and b.
___



[conditions] [geometry] [logic] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Conditionals
https://openbookproject.net/thinkcs/python/english3e/conditionals.html
Programs get really interesting when we can test conditions and change the program behaviour depending on the outcome of the tests. That’s what this chapter is about.
_________
_________
Operators and Expressions
https://realpython.com/python-operators-expressions/#arithmetic-operators
You'll see how calculations can be performed on objects in Python. By the end of this tutorial, you will be able to create complex expressions by combining Python objec …
_________

"""
#Your code should go here:

