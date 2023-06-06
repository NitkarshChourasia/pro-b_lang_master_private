"""
####  Find the Shortest Word(s) in a Sentence  ####

Create a function that accepts a string as an argument. Find its shortest word(s) and return them as a list sorted alphabetically (if there are multiple shortest words).


[Examples]

___
find_shortest_words("I think the solution is fairly obvious.") ➞ ["i"]

find_shortest_words("Chase two rabbits, catch none.") ➞ ["two"]

find_shortest_words("We become what we think about.") ➞ ["we", "we"]

find_shortest_words("The quick brown fox jumped over the lazy dogs back.") ➞ ["fox", "the", "the"]
_____



[Notes]

___
*) Periods, commas and other special characters don't count as part of a word's length.
*) Remember to sort the list of words alphabetically before returning your result.
*) Return words in lowercase only.
___



[language_fundamentals] [loops] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
lower() Method
https://www.tutorialspoint.com/python/string_lower.htm
Returns a copy of the string in which all case-based characters have been lowercased.
_________
_________
split() Method
https://www.tutorialspoint.com/python/string_split.htm
Returns a list of all the words in the string, using str as the separator (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.
_________
_________
sorted() Method
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the given iterable.
_________
_________
re — Regular Expression Operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________

"""
#Your code should go here:

