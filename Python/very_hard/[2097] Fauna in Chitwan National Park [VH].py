"""
####  Fauna in Chitwan National Park  ####

Create a function that takes a string containing both the name and number of animals and plants that may or may not be found in Chitwan National Park. The function should return an list of tuples where the first element in the tuple is the animal name and the second element in the tuple is a number of that particular animal that is found in Chitwan National Park.


[Animals Present in Chitwan National Park]

___
animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
_____



[Examples]

___
fauna_number("There are 24 one-hornedrhino,50 python and 20000 mango.") ➞ [("one-hornedrhino", "24"), ("python", "50")]
# Mango not present in animal list.

fauna_number("There are 244 bengaltiger,200 monitorlizard and 5000 apples .") ➞ [("bengaltiger", "244"), ("monitorlizard", "200")]
# Apples not present in animal list.
_____



[Notes]

___
*) Input contains name and number of both animals and plants.
*) If there is no match, return an empty list.
___



[language_fundamentals] [logic] [regex] 



-------------------------------------------------------------------
[Resources]
_________
isnumeric() Method
https://www.geeksforgeeks.org/python-string-isnumeric-application/
Returns True if all characters in the string are numeric characters, otherwise returns False.
_________
_________
A Complete Python List Tutorial
https://data-flair.training/blogs/python-list-examples/
In today’s tutorial, we will learn about Python list. We will discuss how to create, access, slice, and reassign list in Python. Then we will see how to apply functions …
_________
_________
Python RegEx
https://www.programiz.com/python-programming/regex
In this tutorial, you will learn about regular expressions (RegEx), and use Python's re module to work with RegEx (with the help of examples).
_________

"""
#Your code should go here:

