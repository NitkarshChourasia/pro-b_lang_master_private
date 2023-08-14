"""
####  Find the Bugs: Returning Valid Prices  ####

There has been a masterdata issue which affected the prices of the products. Check if each product has a valid price (integer or float, and greater than or equal to zero). Products with a price of 0 are free and count as a valid price.
The return value should be a Boolean.


[Examples]

___
has_valid_price({ "product": "Milk", "price": 1.50 }) ➞ True

has_valid_price({ "product": "Cheese", "price": -1 }) ➞ False

has_valid_price({ "product": "Eggs", "price": 0 }) ➞ True

has_valid_price({ "product": "Cereals", "price": "3.0" }) ➞ False

has_valid_price(None) ➞ False
_____



[Notes]

Type of the price should be an integer/float. If it's anything else, you should return False.


[bugs] [conditions] [control_flow] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Ternary Operators
https://www.geeksforgeeks.org/ternary-operator-in-python/
Are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply allows to test a condition in a single …
_________
_________
Exception Handling Using Try, except and Finally Statement
https://www.programiz.com/python-programming/exception-handling
In this tutorial, you'll learn how to handle exceptions in your Python program using try, except and finally statements with the help of examples.
_________

"""
#Your code should go here:

