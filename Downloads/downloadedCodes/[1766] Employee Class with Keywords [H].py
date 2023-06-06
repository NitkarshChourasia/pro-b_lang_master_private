"""
####  Employee Class with Keywords  ####

Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. Each instance should have a name and a lastname attribute plus one more attribute for each of the keywords, if any.


[Examples]

___
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

john.name ➞ "John"
mary.lastname ➞ "Major"
richard.height ➞ 178
giancarlo.nationality ➞ "Italian"
_____



[Notes]

___
*) First and last names will be separated by whitespace. The test will not include any middle names or initials.
*) The value of the keywords can be an int, a str or a list.
___



[classes] [loops] 



-------------------------------------------------------------------
[Resources]
_________
setattr() Method
https://www.programiz.com/python-programming/methods/built-in/setattr
Sets the value of the attribute of an object. In this tutorial, we will learn about Python setattr() in detail with the help of examples.
_________
_________
How do I use **kwargs in Python 3 class __init__ function?
https://stackoverflow.com/questions/60418497/how-do-i-use-kwargs-in-python-3-class-init-function/
I am writing a class in Python 3 that I want to be able to take various keyword arguments from the user and to store these values for later use in class methods. An exa …
_________
_________
args and kwargs
https://realpython.com/python-kwargs-and-args/
In this step-by-step tutorial, you'll learn how to use args and kwargs in Python to add more flexibility to your functions. You'll also take a closer look at the single …
_________
_________
Class Definition with **kwargs
https://stackoverflow.com/questions/46213381/python-class-definition-with-kwargs
When trying to instantiate the following class I am getting the following error : "TypeError: __init__() takes exactly 2 arguments (3 given)" Do you know what would be …
_________
_________
Introduction to Python
http://introtopython.org/classes.html
Is a resource for students who want to learn Python as their first language, and for teachers who want a free and open curriculum to use with their students.
_________
_________
Python Update Object From Dictionary
https://stackoverflow.com/questions/405489/python-update-object-from-dictionary
Is there a built-in function/operator I could use to unpack values from a dictionary and assign it into instance variables?
_________

"""
#Your code should go here:

