"""
####  Building Profiles  ####

Create a function that takes multiple arguments, including the first and last name of a person. It should return a dictionary containing all the information which was given in an orderly manner.


[Examples]

___
build_profile("Isaac", "Newton",  location="Kensington", field=["physics", "math", "astronomy", "theology"] ) ➞ { "first_name": "Isaac", "last_name": "Newton", "location": "Kensington", "field": ["physics", "math", "astronomy", "theology"] }

build_profile("Marie", "Curie",  location="Sancellemoz", field="chemistry", discovered="Radium, Polonium" ) ➞ { "first_name": "Marie", "last_name": "Curie", "location": "Sancellemoz", "field": "chemistry", "discovered": "Radium, Polonium" }

build_profile("Donald", "Trump",  party="republican", current_profession="president", president = "45th" ) ➞ { "first_name": "Donald", "last_name": "Trump", "party": "republican", "current_profession": "president", "president": "45th" }
_____



[Notes]

___
*) The arguments must include the first and last name.
*) Other arguments may or may not be given.
___



[logic] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
*args and **kwargs
https://www.geeksforgeeks.org/args-kwargs-python/
The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-le …
_________
_________
update() Method
https://www.programiz.com/python-programming/methods/dictionary/update
Updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.
_________

"""
#Your code should go here:

