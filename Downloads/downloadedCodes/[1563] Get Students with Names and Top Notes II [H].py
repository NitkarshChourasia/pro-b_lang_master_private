"""
####  Get Students with Names and Top Notes II  ####

Create a function that takes a list of dictionaries like [{ "name": "John", "notes": [3, 5, 4]}, { "name": "Mich", "notes": [1, 3, 5]}] and returns a list of dictionaries like [{ "name": "John", "top_note": 5 }, {"name": "Mich", "top_note": 5}].
If a student has no notes (an empty list), return top_note: 0.


[Examples]

___
get_name_and_top_note([{ "name": "John", "notes": [2, 4, 5]}, { "name": "Mich", "notes": [1, 3, 5]}])  ➞ [{ "name": "John", "top_note": 5 }, {"name": "Mich", "top_note": 5}]

get_name_and_top_note([{ "name": "Paul", "notes": []}, {"name": "Victoria", "notes": [3, 4, 2, 1]}])  ➞ [{ "name": "Paul", "top_note": 0 }, {"name": "Victoria", "top_note": 4}]
_____



[Notes]

___
*) Please do not translate this challenge into JavaScript.
*) This challenge is a translation of Bartosz Cytrowski's JavaScript challenge that was not properly translated to Python. You can find the challenge here.
___



[arrays] [functional_programming] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Iterate Over a List in Python
https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
List is equivalent to arrays in other languages, with the extra benefit of being dynamic in size. In Python, the list is a type of container in Data Structures, which i …
_________
_________
Python - Dictionary
https://www.tutorialspoint.com/python/python_dictionary.htm
Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any …
_________
_________
Dictionaries in Python
https://realpython.com/python-dicts/
In this Python dictionaries tutorial you'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, yo …
_________
_________
Removing Items from a Dictionary
https://www.w3schools.com/python/gloss_python_remove_dictionary_items.asp
Removing items from a dictionary.
_________
_________
Python Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is unordered, changeable and does not allow duplicates. Dictionaries …
_________

"""
#Your code should go here:

