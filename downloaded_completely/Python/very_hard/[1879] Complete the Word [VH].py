"""
####  Complete the Word  ####

An input string can be completed if additional letters can be added and no letters need to be taken away to match the word. Furthermore, the order of the letters in the input string must be the same as the order of letters in the final word.
Create a function that, given an input string, determines if the word can be completed.


[Examples]

___
can_complete("butl", "beautiful") ➞ True
# We can add "ea" between "b" and "u", and "ifu" between "t" and "l".

can_complete("butlz", "beautiful") ➞ False
# "z" does not exist in the word beautiful.

can_complete("tulb", "beautiful") ➞ False
# Although "t", "u", "l" and "b" all exist in "beautiful", they are incorrectly ordered.

can_complete("bbutl", "beautiful") ➞ False
# Too many "b"s, beautiful has only 1.
_____



[Notes]

Both string input and word will be lowercased.


[loops] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
RegEx
https://www.programiz.com/python-programming/regex
In this tutorial, you will learn about regular expressions (RegEx), and use Python's re module to work with RegEx (with the help of examples).
_________
_________
replace() Method
https://www.programiz.com/python-programming/methods/string/replace
Returns a copy of the string where all occurrences of a substring is replaced with another substring.
_________
_________
find() Method
https://www.guru99.com/python-string-find.html
Helps to find the index of the first occurrence of the substring in the given string. It will return 1 if the substring is not present. In
_________
_________
How to Sort a List of Strings
https://www.geeksforgeeks.org/python-how-to-sort-a-list-of-strings/
Given a list of strings, the task is to sort that list based on given requirement. There are multiple scenarios possible while sorting a list of sting, like – Sorting i …
_________

"""
#Your code should go here:

