"""
####  Rhyme Time  ####

Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise, two lines rhyme if the last word from each sentence contains the same vowels.


[Examples]

___
does_rhyme("Sam I am!", "Green eggs and ham.") ➞ True

does_rhyme("Sam I am!", "Green eggs and HAM.") ➞ True
# Capitalization and punctuation should not matter.

does_rhyme("You are off to the races", "a splendid day.") ➞ False

does_rhyme("and frequently do?", "you gotta move.") ➞ False
_____



[Notes]

___
*) Case insensitive.
*) Here we are disregarding cases like "thyme" and "lime".
*) We are also disregarding cases like "away" and "today" (which technically rhyme, even though they contain different vowels).
___



[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
endswith() Method
https://www.tutorialspoint.com/python/string_endswith.htm
Returns True if the string ends with the specified suffix, otherwise return False optionally restricting the matching with the given indices start and end.
_________
_________
Slicing Strings
https://www.w3schools.com/python/python_strings_slicing.asp
You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
_________

"""
#Your code should go here:

