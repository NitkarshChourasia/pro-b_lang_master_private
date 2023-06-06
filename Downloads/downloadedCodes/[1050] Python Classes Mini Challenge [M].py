"""
####  Python Classes Mini Challenge  ####

In this challenge, you will learn about classes in Python.
Python classes are easy to understand. They are almost the same as JavaScript classes, with a different syntax and different constructor function names. Constructors define some variables in your class; in Python that is def __init__(self). Other functions are defined the same as normal.
I want you to create a class called programmer. It should have a salary value, work_hours value, and a __del__(self) function. __del__(self) should return "oof, " + str(salary) + ", " + str(work_hours) when the object is destroyed. salary and work_hours will be in the constructor. Variables in a class are defined with self.name = value.
Also, define a function that will compare two programmers (their salary and work_hours) and return the programmer with the lower salary. If their salary is equal, then compare their work_hours, which will always be different.
This is not really a challenge, just an introduction to Python classes.


[Examples]

___
prog = programmer(25000, 5)

prog.salary ➞ 25000

prog.work_hours ➞ 5

del prog ➞ "oof, 25000, 5"
# By the __del__ function.
_____



[Notes]

___
*) Only base functions are pre-written in the code tab. You need to complete them and possibly add a few arguments.
*) Class variables are defined inside the __init__ function.
*) In most cases __del__ isn't used to return values (but it's not possible to check print output in an Edabit test).
___



[classes] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Object-Oriented Programming (OOP) in Python
https://realpython.com/python3-object-oriented-programming/
Object-oriented Programming, or OOP for short, is a programming paradigm which provides a means of structuring programs so that properties and behaviors are bundled int …
_________
_________
Python Class Tutorial
https://docs.python.org/3/tutorial/classes.html
Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. …
_________
_________
The Style Guide for Python Code
https://pep8.org/#class-names
I only put this here to help others with style, since the class name wasn't properly in uppercase, as it should have been according to PEP 8. The naming convention for …
_________
_________
Classes
https://www.w3schools.com/python/python_classes.asp
Is an object-oriented programming language. Almost everything in Python is an object, with its properties and methods. A Class is like an object constructor, or a "bl …
_________

"""
#Your code should go here:

