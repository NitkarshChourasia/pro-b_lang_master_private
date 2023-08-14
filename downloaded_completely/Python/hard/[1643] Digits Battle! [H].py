"""
####  Digits Battle!  ####

Starting from the left side of an integer, adjacent digits pair up in "battle" and the larger digit wins. If two digits are the same, they both lose. A lone digit automatically wins.
Create a function that returns the victorious digits.
To illustrate:
___
battle_outcome(578921445) ➞ 7925
# [57]: 7 wins; [89] 9 wins; [21] 2 wins;
# [44] neither wins; 5 (automatically) wins
_____



[Examples]

___
battle_outcome(32531) ➞ 351
# 3 deffeats 2, 5 defeats 3, 1 is a single.

battle_outcome(111) ➞ 1
# 1 and 1 tie, so neither move on, last 1 is a single.

battle_outcome(78925) ➞ 895
_____



[Notes]

___
*) There are no winners in a battle with equal digits (neither should be printed).
*) If the length of the number is odd, the lone digit should be printed at the end of the number.
___



[games] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Check if a Number is Odd or Even
https://www.programiz.com/python-programming/examples/odd-even
Source code to check whether a number entered by user is either odd or even in Python programming with output and explanation…
_________
_________
Try Except
https://www.w3schools.com/python/python_try_except.asp
The try block lets you test a block of code for errors. The except block lets you handle the error. The finally block lets you execute code, regardless of the result …
_________

"""
#Your code should go here:

