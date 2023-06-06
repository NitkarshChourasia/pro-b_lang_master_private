"""
####  Almost Palindrome  ####

A string is an almost-palindrome if, by changing only one character, you can make it a palindrome. Create a function that returns True if a string is an almost-palindrome and False otherwise.


[Examples]

___
almost_palindrome("abcdcbg") ➞ True
# Transformed to "abcdcba" by changing "g" to "a".

almost_palindrome("abccia") ➞ True
# Transformed to "abccba" by changing "i" to "b".

almost_palindrome("abcdaaa") ➞ False
# Can't be transformed to a palindrome in exactly 1 turn.

almost_palindrome("1234312") ➞ False
_____



[Notes]

Return False if the string is already a palindrome.


[strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How do you change one character in a string in Python?
https://www.quora.com/How-do-you-change-one-character-in-a-string-in-Python
It doesn’t accept changes, because, strings are immutable objects, you can’t edit a string variables once created. This has a lot of answers on the internet. Google the …
_________

"""
#Your code should go here:

