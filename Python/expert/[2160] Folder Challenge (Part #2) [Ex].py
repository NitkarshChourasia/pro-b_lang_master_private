"""
####  Folder Challenge (Part #2)  ####

This is a sequel to part #1, with the same setup, but a different goal.
A folder system on a computer might look something like the picture below:

In this challenge, folder systems will be represented by dictionaries where the keys are folders X and the value at X is the list of subfolders of X.
For example, the picture above becomes the dictionary:
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
*) Two folders X and Y.
___

Write a function that finds the "smallest" folder containing both X and Y (in the illustration, this is the lowest folder for which you can travel down to both X and Y; or, if you view the system as a "family tree", this is the last common ancestor).


[Examples]

___
last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "B", "C") ➞ "A"

last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "I", "J") ➞ "G"

last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "I", "K") ➞ "D"

last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "D", "I") ➞ "D"

last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "G", "G") ➞ "G"
_____



[Notes]

___
*) All the examples above use the folder system in the illustration, but the tests will use other folder systems as well.
*) For the purposes of this challenge, any folder is inside itself, as in the last two examples.
___



[algorithms] [data_structures] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Dictionaries
https://realpython.com/python-dicts/
Learn how to access and manage dictionary data. Once you have finished this tutorial, you should have a good sense of when a dictionary is the appropriate data type to …
_________
_________
Recursion
https://realpython.com/python-recursion/
Learn about recursion in Python. You'll see what recursion is, how it works in Python, and under what circumstances you should use it. You'll finish by exploring severa …
_________
_________
Common Python Data Structures
https://realpython.com/python-data-structures/
In this tutorial, you'll learn about Python's data structures. You'll look at several implementations of abstract data types and learn which implementations are best fo …
_________

"""
#Your code should go here:

