"""
####  Alphabetically Sorted  ####

A word is alphabetically sorted if all of the letters in it are in consecutive alphabetical order. Some examples of alphabetically sorted words: abhors (a is before b, b is before h, h is before o, etc.), ghost, accent, hoop.
Create a function that takes in a sentence as input and returns True if there is at least one alphabetically sorted word inside that has a minimum length of 3.


[Examples]

___
is_alphabetically_sorted("Paula has a French accent.") ➞ True
# "accent" is alphabetically sorted.

is_alphabetically_sorted("The biopsy returned negative results.") ➞ True
# "biopsy" is alphabetically sorted.

is_alphabetically_sorted("She sells sea shells by the sea shore.") ➞ False
# Although "by" is alphabetically sorted, it is only 2 letters long.
_____



[Notes]

___
*) Do not count words with 2 or fewer characters.
*) Ignore punctuation (periods, commas, etc).
___



[regex] [sorting] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Regular Expression Cheatsheet
https://learnbyexample.github.io/cheatsheet/python/python-regex-cheatsheet/
This blog post gives an overview and examples of regular expression syntax as implemented by the re built-in module (Python 3.8+). Assume ASCII character set unless oth …
_________
_________
Use sorted() and sort()
https://realpython.com/python-sort/
In this step-by-step tutorial, you’ll learn how to sort in Python. You'll know how to sort various types of data in different data structures, customize the order, and …
_________
_________
Any All
https://www.geeksforgeeks.org/any-all-in-python/
Any and All are two built ins provided in python used for successive And/Or. Any returns true if any of the items is True. It returns False if empty or all are false. …
_________
_________
sort() Method
https://www.w3schools.com/python/ref_list_sort.asp
Sorts the list ascending by default.
_________

"""
#Your code should go here:

