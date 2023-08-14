"""
####  Smallest Square Ending  ####

In a letter to Lord Bowden in 1837, Charles Babbage asked, "What is the smallest positive integer whose square ends in 269,696?". He thought the answer was 99,736 whose square is 9,947,269,696. Was he right?
Write a function that takes a positive integer n and returns the smallest number whose square ends with n. One small twist, if n == 269696 return "Babbage was correct!" if the smallest number whose square ends with 269,696 is 99,736, otherwise return "Babbage was incorrect!".


[Examples]

___
babbage(25) ➞ 5

babbage(161) ➞ 119
# 119 * 119 == 14,161
# Ends with 161

babbage(269696) ➞ "Babbage was {?}!"
# Replace {?} with the word "correct" or "incorrect".
_____



[Notes]

___
*) n will always be a positive integer n > 0.
*) Make sure your solution is efficient enough to pass the tests within a 12 second time limit.
___



[algorithms] [logic] [math] 



-------------------------------------------------------------------
[Resources]
_________
range() Type
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
Check if a Number Is Integer or Decimal
https://note.nkmk.me/en/python-check-int-float/
How to check whether a number is integer or decimal in Python is explained with sample code in the following cases. Check if object is int or float: isinstance() Check …
_________
_________
Babbage Problem
https://rosettacode.org/wiki/Talk:Babbage_problem
I can only assume that a   positive integer   is meant to be found,   otherwise finding the   smallest negative integer   would be pointless.
_________

"""
#Your code should go here:

