"""
####  Pizza Points™ 🍕  ####


Google is launching a network of autonomous pizza delivery drones and wants you to create a flexible rewards system (Pizza Points™) that can be tweaked in the future. The rules are simple: if a customer has made at least N orders of at least Y price, they get a FREE pizza!
Create a function that takes a dictionary of customers, a minimum number of orders and a minimum order price. Return a list of customers that are eligible for a free pizza.


[Examples]

___
customers = {
  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
}

  pizza_points(customers, 5, 20) ➞ ["Spider-Man"]

  pizza_points(customers, 3, 10) ➞ ["Batman", "Spider-Man"]

  pizza_points(customers, 5, 100) ➞ []
_____



[Notes]

⚠️Sort the returned array of customer names in alphabetical order.


[games] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Data Structures
https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary
This chapter describes some things you’ve learned about already in more detail, and adds some new things as well.
_________
_________
Mapping Types
https://docs.python.org/3/library/stdtypes.html#typesmapping
A mapping object maps hashable values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the dictionary. (For other …
_________
_________
How to Iterate Through a Dictionary in Python
https://realpython.com/iterate-through-dictionary-python/
As a Python coder, you’ll often be in situations where you’ll need to iterate through a dictionary in Python, while you perform some actions on its key-value pairs. Whe …
_________

"""
#Your code should go here:

