"""
####  The Hangman Game  ####

Create a function that, given a phrase and a number of letters guessed, returns a string with hyphens - for every letter of the phrase not guessed, and each letter guessed in place.


[Examples]

___
hangman("helicopter", ["o", "e", "s"]) ➞ "-e---o--e-"

hangman("tree", ["r", "t", "e"]) ➞ "tree"

hangman("Python rules", ["a", "n", "p", "r", "z"]) ➞ "P----n r----"

hangman("He"s a very naughty boy!", ["e", "a", "y"]) ➞ "-e"- a -e-y -a----y --y!"
_____



[Notes]

___
*) The letters are always given in lowercase, but they should be returned in the same case as in the original phrase (see example #3).
*) All characters other than letters should always be returned (see example #4).
___



[games] [language_fundamentals] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
join() Function
https://www.geeksforgeeks.org/join-function-python/
Is a string method and returns a string in which the elements of sequence have been joined by str separator.
_________
_________
lower() Method
https://www.programiz.com/python-programming/methods/string/lower
Converts all uppercase characters in a string into lowercase characters and returns it.
_________
_________
isalpha() Method
https://www.programiz.com/python-programming/methods/string/isalpha
Returns True if all characters in the string are alphabets. If not, it returns False.
_________
_________
isalpha() Method
https://www.w3schools.com/python/ref_string_isalpha.asp
Returns True if all the characters are alphabet letters (a-z). Example of characters that are not alphabet letters: (space)!#%&? etc.
_________
_________
replace() Method
https://www.w3schools.com/python/ref_string_replace.asp
Replaces a specified phrase with another specified phrase.
_________

"""
#Your code should go here:

