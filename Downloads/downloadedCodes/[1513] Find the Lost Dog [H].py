"""
####  Find the Lost Dog  ####

___
*) 0 represents the dog.
*) Each list represents a house and each 1 represents an empty room.
*) Return the house and the room where it is located, there can be only one dog lost per building.
___



[Examples]

___
lost_dog([1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
➞ "Dog not found!"

lost_dog([1, 1, 1, 1, 1, 1],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
➞ {"Dog1": "House (2) and Room (1)", "Dog2": "House (3) and Room (2)"}

lost_dog([1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1])
➞ {"Dog1": "House (1) and Room (6)", "Dog2": "House (2) and Room (1)", "Dog3": "House (3) and Room (2)", "Dog4": "House (4) and Room (3)"}
_____



[Notes]

Check the Resources if you're stuck.


[arrays] [language_fundamentals] [logic] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
Appending Element to a Dictionary
https://www.guru99.com/python-dictionary-append.html
To append an element to an existing dictionary, you have to use the dictionary name followed by square brackets with the key name and assign a value to it.
_________
_________
enumerate() Method
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________
_________
Dictionaries
https://realpython.com/python-dicts/
Learn how to access and manage dictionary data. Once you have finished this tutorial, you should have a good sense of when a dictionary is the appropriate data type to …
_________
_________
index() Method
https://www.w3schools.com/python/ref_list_index.asp
Returns the position at the first occurrence of the specified value.
_________
_________
Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
Are used to store data values in key:value pairs.
_________
_________
Dictionary update() Method
https://www.w3schools.com/python/ref_dictionary_update.asp
Inserts the specified items to the dictionary. The specified items can be a dictionary, or an iterable object with key value pairs.
_________

"""
#Your code should go here:

