"""
####  Coffee Shop  ####

Write a class called CoffeeShop, which has three instance variables:

and seven methods:

IMPORTANT: Orders are fulfilled in a FIFO (first-in, first-out) order.


[Examples]

___
tcs.add_order("hot cocoa") ➞ "This item is currently unavailable!"
# Tesha's coffee shop does not sell hot cocoa
tcs.add_order("iced tea") ➞ "This item is currently unavailable!"
# specifying the variant of "iced tea" will help the process

tcs.add_order("cinnamon roll") ➞  "Order added!"
tcs.add_order("iced coffee") ➞ "Order added!"
tcs.list_orders ➞ ["cinnamon roll", "iced coffee"]
# all items of the current order

tcs.due_amount() ➞ 2.17

tcs.fulfill_order() ➞ "The cinnamon roll is ready!"
tcs.fulfill_order() ➞ "The iced coffee is ready!"
tcs.fulfill_order() ➞ "All orders have been fulfilled!"
# all orders have been presumably served

tcs.list_orders() ➞ []
# an empty list is returned if all orders have been exhausted

tcs.due_amount() ➞ 0.0
# no new orders taken, expect a zero payable

tcs.cheapest_item() ➞ "lemonade"
tcs.drinks_only() ➞ ["orange juice", "lemonade", "cranberry juice", "pineapple juice", "lemon iced tea", "vanilla chai latte", "hot chocolate", "iced coffee"]
tcs.food_only() ➞ ["tuna sandwich", "ham and cheese sandwich", "bacon and egg", "steak", "hamburger", "cinnamon roll"]
_____



[Notes]

Round off due amount up to two decimal places.


[arrays] [classes] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Classes and Objects [With Examples]
https://www.programiz.com/python-programming/class
In this tutorial, you will learn about the core functionality of Python objects and classes. You'll learn what a class is, how to create it and use it in your program.
_________
_________
Object-Oriented Programming (OOP) in Python
https://realpython.com/python3-object-oriented-programming/
In this tutorial, you'll learn all about object-oriented programming (OOP) in Python. You'll learn the basics of the OOP paradigm and cover concepts like classes and in …
_________
_________
Dictionaries in Python
https://realpython.com/python-dicts/
In this Python dictionaries tutorial you'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, yo …
_________
_________
Python Dictionary
https://www.programiz.com/python-programming/dictionary
In this tutorial, you'll learn everything about Python dictionaries; how they are created, accessing, adding, removing elements from them and various built-in methods.
_________

"""
#Your code should go here:

