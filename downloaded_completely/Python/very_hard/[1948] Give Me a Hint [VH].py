"""
####  Give Me a Hint  ####

Given a sentence, return a list of strings which gradually reveals the next letter in every word at the same time. Use underscores to hide the remaining letters.


[Examples]

___
grant_the_hint("Mary Queen of Scots") ➞ [
  "____ _____ __ _____",
  "M___ Q____ o_ S____",
  "Ma__ Qu___ of Sc___",
  "Mar_ Que__ of Sco__",
  "Mary Quee_ of Scot_",
  "Mary Queen of Scots"
]

grant_the_hint("The Life of Pi") ➞ [
  "___ ____ __ __",
  "T__ L___ o_ P_",
  "Th_ Li__ of Pi",
  "The Lif_ of Pi",
  "The Life of Pi"
]
_____



[Notes]

Maintain capitalisation.


[arrays] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
.span() returns a tuple containing the start-, and end positions of the match. .string returns the string passed into the function .group() returns the part of the st …
_________
_________
join() Method
https://www.geeksforgeeks.org/join-function-python/
A string method and returns a string in which the elements of sequence have been joined by str separator.
_________
_________
List Comprehension
https://www.w3schools.com/python/python_lists_comprehension.asp
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
_________
_________
split() Method
https://www.w3schools.com/python/ref_string_split.asp
Splits a string into a list. You can specify the separator, default separator is any whitespace.
_________
_________
re.sub()
https://www.codespeedy.com/re-sub-in-python/
Replaces the substrings that match with the search pattern with a string of user's choice.
_________

"""
#Your code should go here:

