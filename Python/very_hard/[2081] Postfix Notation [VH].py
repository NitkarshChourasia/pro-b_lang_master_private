"""
####  Postfix Notation  ####

Postfix notation is a mathematical notation in which operators follow their operands. In other words, pfexp1 pfexp2 op, where pfexp1 and pfexp2 are both postfix expressions.
Some examples:
___
*) 2 2 + is the postfix notation of the expression 2 + 2.
*) 2 3 * 1 - 5 / is the postfix notation of the expression ((2 * 3) - 1) / 5.
___

Here you have to compute the result from a postfix expression.


[Examples]

___
postfix("2 2 +") ➞ 4
# 2 + 2 = 4

postfix("2 3 * 1 - 5 /") ➞ 1
# ((2 * 3) - 1) / 5 = (6 - 1) / 5 = 5 / 5 = 1
_____



[Note]

___
*) Operators and operands are separated by a space.
*) The operators +, -, *, / may be supported.
*) You can use Python list as a stack data structure to solve this problem.
___



[data_structures] [language_fundamentals] [math] 



-------------------------------------------------------------------
[Resources]
_________
Postfix Notation
https://simple.wikipedia.org/wiki/Postfix_notation
A way to write down equations and other mathematical formulae. Postfix notation is also known as Reverse Polish Notation. The notation was invented by Charles Hamblin i …
_________

"""
#Your code should go here:

