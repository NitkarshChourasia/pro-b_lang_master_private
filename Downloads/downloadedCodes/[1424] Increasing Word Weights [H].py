"""
####  Increasing Word Weights  ####

The weight of an English word can be calculated by summing the ASCII code point for each character in the word, excluding any punctuation:
___
"Wouldn't" = 87 + 111 + 117 + 108 + 100 + 110 + 116 = 749
_____

Write a function that takes a sentence as a string, returning True if all word weights increase for each word in the sentence, and False if any word weight decreases or remains the same. For any single-word sentences, return True.


[Examples]

___
increasing_word_weights("Why not try?") ➞ True
# 312 -> 337 -> 351 (weights increase)

increasing_word_weights("All other roads.") ➞ False
# 281 -> 546 -> 537 (537 is less than 546)
_____



[Notes]

Check the Resources for links on how to return character codes.


[arrays] [language_fundamentals] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
isalpha() Method
https://www.programiz.com/python-programming/methods/string/isalpha
Returns True if all characters in the string are alphabets. If not, it returns False.
_________
_________
zip() Function
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it. In this tutorial, we will learn about Python zip() in detail with the help of examples.
_________
_________
Converting Characters to Unicode Code Points
https://docs.python.org/3/library/functions.html#ord
Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 …
_________
_________
String isalpha() and Its Application
https://www.geeksforgeeks.org/python-string-isalpha-application/
Returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”. This function is used to check if the argument contains any alphabets chara …
_________

"""
#Your code should go here:

