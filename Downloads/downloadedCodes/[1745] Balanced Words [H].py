"""
####  Balanced Words  ####

We can assign a value to each character in a word, based on their position in the alphabet (a = 1, b = 2, ... , z = 26). A balanced word is one where the sum of values on the left-hand side of the word equals the sum of values on the right-hand side. For odd length words, the middle character (balance point) is ignored.
Write a function that returns True if the word is balanced, and False if it's not.


[Examples]

___
balanced_word("zips") ➞ True
# "zips" = "zi|ps" = 26+9|16+19 = 35|35 = True

balanced_word("brake") ➞ False
# "brake" = "br|ke" = 2+18|11+5 = 20|16 = False
_____



[Notes]

___
*) All words will be lowercase, and have a minimum of 2 characters.
*) Palindromic words will always be balanced.
___



[strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
index() Method
https://www.programiz.com/python-programming/methods/string/index
Returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.
_________

"""
#Your code should go here:

