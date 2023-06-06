"""
####  Same on Both Ends  ####

Given a sentence, return the number of words which have the same first and last letter.


[Examples]

___
count_same_ends("Pop! goes the balloon") ➞ 1

count_same_ends("And the crowd goes wild!") ➞ 0

count_same_ends("No I am not in a gang.") ➞ 1
_____



[Notes]

___
*) Don't count single character words (such as "I" and "A" in example #3).
*) The function should not be case sensitive, meaning a capital "P" should match with a lowercase one.
*) Mind the punctuation!
*) Bonus points indeed for using regex!
___



[loops] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Best way to strip punctuation from a string?
https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
From an efficiency perspective, you're not going to beat s.translate(None, string.punctuation) For higher versions of Python use the following code: s.translate(str.m …
_________
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

