"""
####  Longest Abecedarian Word  ####

An abecedarian word is a word where all of its letters are arranged in alphabetical order. Examples of these words include:
___
*) Empty
*) Forty
*) Almost
___

Given a list of words, create a function which returns the longest abecedarian word. If no word in a list matches the criterea, return an empty string.


[Examples]

___
longest_abecedarian(["ace", "spades", "hearts", "clubs"]) ➞ "ace"

longest_abecedarian(["forty", "choppy", "ghost"]) ➞ "choppy"

longest_abecedarian(["one", "two", "three"]) ➞ ""
_____



[Notes]

___
*) All words will be given in lowercase.
*) If two abecedarian words have the same length, return the word which appeared first in the list.
___



[arrays] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Char Comparisons
https://stackoverflow.com/questions/50918637/python-char-comparisons
When you compare chars, their ordinal values are compared So 'a' < 'b' just means ord('a') < ord('b').
_________

"""
#Your code should go here:

