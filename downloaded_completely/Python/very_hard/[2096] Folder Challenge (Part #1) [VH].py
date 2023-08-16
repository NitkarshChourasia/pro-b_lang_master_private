"""
####  Folder Challenge (Part #1)  ####

A folder system on a computer might look something like the picture below.

In this challenge, folder systems will be represented by dictionaries where the keys are folders X and the value at X is the list of subfolders of X. For example, the picture above becomes the dictionary.
___
{
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}
_____

The inputs for this challenge will be:
___
*) A dictionary representing a folder system.
*) Two folders, X and Y.
___

Write a function that decides whether "X is inside Y" (in the illustration, this means that you can travel down from Y to X).


[Examples]

___
is_it_inside({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "B",  "A") ➞ True

is_it_inside({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "B",  "D") ➞ False

is_it_inside({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "I",  "D") ➞ True

is_it_inside({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "A", "K") ➞ False

is_it_inside({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "D", "D") ➞ True
_____



[Notes]

___
*) All the examples above use the folder system in the illustration, but the tests will use other folder systems as well.
*) For the purposes of this challenge, any folder is inside itself, as in the last example.
*) This challenge has a part 2.
___



[algorithms] [data_structures] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Dictionaries
https://www.tutorialspoint.com/python/python_dictionary.htm
Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any …
_________
_________
Dictionaries
https://realpython.com/python-dicts/
In this Python dictionaries tutorial, you'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, y …
_________

"""
#Your code should go here:

