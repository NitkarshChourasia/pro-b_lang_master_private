"""
####  Vending Machine  ####

Your task is to create a function that simulates a vending machine.
Given an amount of money (in cents ¢ to make it simpler) and a product_number, the vending machine should output the correct product name and give back the correct amount of change.
The coins used for the change are the following: [500, 200, 100, 50, 20, 10]
The return value is a dictionary with 2 properties:
___
*) product: the product name that the user selected.
*) change: an array of coins (can be empty, must be sorted in descending order).
___



[Examples]

___
vending_machine(products, 200, 7) ➞ { "product": "Crackers", "change": [ 50, 20, 10 ] }

vending_machine(products, 500, 0) ➞ "Enter a valid product number"

vending_machine(products, 90, 1) ➞ "Not enough money for this product"
_____



[Notes]

___
*) The products are fixed and you can find them in the Tests tab.
*) If product_number is invalid (out of range) you should return the string: "Enter a valid product number".
*) If money is not enough to buy a certain product you should return the string: "Not enough money for this product".
*) If there's no change, return an empty array as the change.
___



[arrays] [interview] [loops] [objects] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Python Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and  they have keys and values.
_________

"""
#Your code should go here:

