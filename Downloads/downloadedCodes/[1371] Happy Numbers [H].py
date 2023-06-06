"""
####  Happy Numbers  ####

Given any number, we can create a new number by adding the sums of squares of digits of that number. For example, given 203, our new number is 4 + 0 + 9 = 13. If we repeat this process, we get a sequence of numbers:
___
203 -> 13 -> 10 -> 1 -> 1
_____

Sometimes, like with 203, the sequence reaches (and stays at) 1. Numbers like this are called happy.
Not all numbers are happy. If we started with 11, the sequence would be:
___
11 -> 2 -> 4 -> 16 -> ...
_____

This sequence will never reach 1, and so the number 11 is called unhappy.
Given a positive whole number, you have to determine whether that number is happy or unhappy.


[Examples]

___
happy(203) ➞ True

happy(11) ➞ False

happy(107) ➞ False
_____



[Notes]

___
*) You can assume (and it is actually true!) that all positive whole numbers are either happy or unhappy. Any happy number will have a 1 in its sequence, and every unhappy number will have a 4 in its sequence.
*) The only numbers passed to your function will be positive whole numbers.
___



[loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
eval() Method
https://www.programiz.com/python-programming/methods/built-in/eval
Parses the expression passed to this method and runs python expression (code) within the program. In simple terms, the eval() function runs the python code (which is pa …
_________
_________
Sum of Squares Function
https://stackoverflow.com/questions/16367823/python-sum-of-squares-function
This uses sum() together with a generator expression to turn all the digits back to integers, square them, and sum the results together again.
_________
_________
Happy Number
https://en.wikipedia.org/wiki/Happy_number
A happy number by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits in base-ten, and repeat the pro …
_________

"""
#Your code should go here:

