"""
####  String Cleaver  ####

Create a function that takes a string (without spaces) and a word list, cleaves the string into words based on the list, and returns the correctly spaced version of the string (a sentence). If a section of the string is encountered that can't be found on the word list, return "Cleaving stalled: Word not found".


[Examples]

___
word_list = ["about", "be", "hell", "if", "is", "it", "me", "other", "outer", "people", "the", "to", "up", "where"]


cleave("ifitistobeitisuptome", word_list) ➞ "if it is to be it is up to me"

cleave("hellisotherpeople", word_list) ➞ "hell is other people"

cleave("hellisotterpeople", word_list) ➞ "Cleaving stalled: Word not found"
_____



[Notes]

Words on the word_list can appear more than once in the string. The word_list is a reference guide, kind of like a dictionary that lists which words are allowed.


[strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python Indexing and Slicing for Lists and Other Sequential Types
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
Python supports slice notation for any sequential data type like lists, strings, and others. Discover more about indexing and slicing operations over Python's lists and …
_________
_________
How to Index and Slice Strings in Python
https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
The Python string data type is a sequence made up of one or more individual characters consisting of letters, numbers, whitespace characters, or symbols. Strings are se …
_________
_________
Python String join()
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________

"""
#Your code should go here:

