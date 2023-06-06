"""
####  Hashtag Generator  ####

Create a function that is a Hashtag Generator by using the following rules:
___
*) The output must start with a hashtag (#).
*) Each word in the output must have its first letter capitalized.
*) If the final result, a single string, is longer than 140 characters, the function should return false.
*) If either the input (str) or the result is an empty string, the function should return false.
___



[Examples]

___
generate_hashtag("    Hello     World   " ) ➞ "#HelloWorld"

generate_hashtag("") ➞ false, "Expected an empty string to return false"

generate_hashtag("Edabit Is Great") ➞ "#EdabitIsGreat", "Should remove spaces."
_____



[Notes]

N/A


[algorithms] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.w3schools.com/python/ref_string_split.asp
Splits a string into a list.
_________
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string.
_________
_________
title() Method
https://www.w3schools.com/python/ref_string_title.asp
Returns a string where the first character in every word is upper case. Like a header, or a title. If the word contains a number or a symbol, the first letter after th …
_________
_________
replace() Method
https://www.w3schools.com/python/ref_string_replace.asp
Replaces a specified phrase with another specified phrase.
_________
_________
capitalize() Method
https://www.w3schools.com/python/ref_string_capitalize.asp
Returns a string where the first character is upper case.
_________

"""
#Your code should go here:

