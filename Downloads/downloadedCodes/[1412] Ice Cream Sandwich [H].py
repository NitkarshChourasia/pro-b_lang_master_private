"""
####  Ice Cream Sandwich  ####

An ice cream sandwich is a string that is formed by two identical ends and a different middle.

___
"AABBBAA"

"3&&3"

"yyyyymmmmmmmmyyyyy"

"hhhhhhhhmhhhhhhhh"
_____

Notice how left and right ends of the sandwich are identical in both length and in repeating character). The middle section is distinctly different.

___
"BBBBB"
// You can't have just plain icecream.

"AAACCCAA"
// You can't have unequal sandwich ends.

"AACDCAA"
// You can't have more than one filling.

"A"
// You can't have fewer than 3 characters.
_____

Write a function that returns True if a string is an ice cream sandwich and False otherwise.


[Examples]

___
is_icecream_sandwich("CDC") ➞ True

is_icecream_sandwich("AAABB") ➞ False

is_icecream_sandwich("AA") ➞ False
_____



[Notes]

An ice cream sandwich must have a minimum length of 3 characters, and at least two of these characters must be distinct (you can't only have the filling!).


[language_fundamentals] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Reverse String
https://www.journaldev.com/23647/python-reverse-string
Python String doesn’t have a built-in reverse() function. However, there are various ways to reverse a string in Python.
_________
_________
len() Function
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
Set
https://www.programiz.com/python-programming/set
In this tutorial, you'll learn everything about Python sets; how they are created, adding or removing elements from them, and all operations performed on sets in Python.
_________
_________
How to split a string on character change?
https://stackoverflow.com/questions/34196262/how-to-split-a-string-on-character-change
Let's say I have the string aaaabccdddefgg, I want to split the string on character change, using Python 3. So it would output: ["aaaa", "b", "cc", "ddd", "e", "f", "g …
_________

"""
#Your code should go here:

