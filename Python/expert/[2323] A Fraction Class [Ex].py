"""
####  A Fraction Class  ####

Mathematically, a fraction can be defined as the ratio a/b, where a and b are integers and b is non zero.
In this challenge, we are going to implement a Fraction class and some methods to support arithmetic and comparison operations on them. Write a Fraction class that meets the following requirements:
___
*) Initialisation: Create a Fraction object with a as numerator and b as denominator, e.g. Fraction(5, 6) where a = 5 and b = 6. Validate that a and b are both integers and b is non-zero. If not, print the error message shown below and do not create any variables. The numerator and denominator should also be stored in factorized form, e.g. 4/6 should be stored as 2/3.
*) Representation: It should be possible to print a Fraction or obtain a string representation of it via the str built-in function. For a positive fraction, this should return the string "x/y" e.g. "5/4". If the fraction is negative, return "- x/y" e.g. "- 5/9" (note the space after the - sign). If the fraction has failed to initialize, detect this (it shouldn't have any instance variables) and return the string "Initialisation Failed".
*) Arithmetic Operations: Implement suitable methods to support +, -, *, and / operations between two fractions with the usual arithmetic meaning. Return the appropriate factorised Fraction e.g Fraction(2, 3) * Fraction(2, 5) should return Fraction(4, 15). A division operation could result in a zero denominator and this should be catered for by printing the error message described in the initialization section and returning None. If the result of an operation is a negative fraction, return the numerator as the negative integer.
*) Comparison Operations: Implement suitable methods to compare two Fraction objects using operators ==,!=, <, >, <= and >= with the usual meanings. For ==, apply a tolerance factor of 10^-7.
*) Instance Method: Implement instance method decimal. This should return the decimal equivalent of the Fraction object to up to seven decimal places e.g. Fraction(1/4).decimal() -> 0.25.
*) Class Method: Implement class method fraction(decimal) which returns a Fraction object equivalent to decimal to up to seven decimal places e.g. Fraction.fraction(2.5) -> Fraction(5, 2). If the parameter decimal is an integer, set the denominator in Fraction to 1.
___



[Examples]

___
str(Fraction(2, -3)) ➞ ""- 2/3"

str(Fraction(3, 0)) ➞ "Initialisation Failed"
# Should print "numerator must be an integer and denominator a non zero integer".

Fraction(1, 5) + Fraction(3, 10) ➞ Fraction(1, 2)

Fraction(5, 2) * Fraction(6, -10) ➞ Fraction(-3, 2)

Fraction(0, 3) / Fraction(0, 5) ➞ None
# Should print "numerator must be an integer and denominator a non zero integer".

Fraction(-4, 5) > Fraction(-3, 5) ➞ False

Fraction(10, 9) < Fraction(2, 1) ➞ True

Fraction.fraction(11) ➞ Fraction(11, 1)

Fraction(5, 9).decimal() ➞ 0.5555556
_____



[Notes]

You will need to use a technique called operator overloading to successfully complete this challenge. This requires the use of what are termed magic or dunder methods in Python (Resources have a useful link for these). If you need to brush up on arithmetic with fractions, there's a link for that too.


[classes] [language_fundamentals] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Operator Overloading
https://www.geeksforgeeks.org/operator-overloading-in-python/
Means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two …
_________
_________
Python's Instance, Class, and Static Methods Demystified
https://realpython.com/instance-class-and-static-methods-demystified/#:~:text=Instance%20methods%20need%20a%20class,access%20to%20cls%20or%20self%20.
This tutorial helps demystify what's behind class, static, and instance methods in Python. If you develop an intuitive understanding for their differences you’ll be abl …
_________
_________
Object-Oriented Programming (OOP) in Python
https://realpython.com/python3-object-oriented-programming/
In this tutorial, you'll learn all about object-oriented programming (OOP) in Python. You'll learn the basics of the OOP paradigm and cover concepts like classes and in …
_________
_________
Arithmetic Operations
https://courses.lumenlearning.com/boundless-algebra/chapter/introduction-to-arithmetic-operations/
Addition is the most basic operation of arithmetic. In its simplest form, addition combines two quantities into a single quantity, or sum. For example, say you have a g …
_________

"""
#Your code should go here:

