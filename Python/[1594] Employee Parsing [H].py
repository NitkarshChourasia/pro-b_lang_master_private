"""
####  Employee Parsing  ####

In the class Employee, implement the instance attributes as firstname, lastname and salary.
Create the method from_string() which parses a string containing these attributes and assigns them to the correct properties. Properties will be separated by a dash.


[Examples]

___
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
_____

___
emp1.firstname ➞ "Mary"

emp1.salary ➞ 60000

emp2.firstname ➞ "John"

emp2.salary ➞ 55000
_____



[Notes]

___
*) The salary is an integer.
*) Check the Resources for some helpful tutorials on how to do this.
___



[classes] [language_fundamentals] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Class Methods: Alternate Constructors
https://code-maven.com/slides/python-programming/class-methods-alternative-constructor
Are used as Factory methods, they are usually good for alternative constructors. In order to be able to use a method as a class-method (Calling Date.method(...) one nee …
_________
_________
What is a clean Pythonic way to have multiple constructors?
https://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
I can't find a definitive answer for this. As far as I know, you can't have multiple __init__ functions in a Python class. So how do I solve this problem? Suppose I hav …
_________
_________
classmethod() Method
https://www.programiz.com/python-programming/methods/built-in/classmethod
Returns a class method for the given function.
_________
_________
classmethod() Method
https://www.programiz.com/python-programming/methods/built-in/classmethod
Returns a class method for the given function.
_________
_________
Class Methods and When to Use Them
https://www.pythontutorial.net/python-oop/python-class-methods/
In this tutorial, you'll learn about Python class methods and when to use them appropriately.
_________

"""
#Your code should go here:

