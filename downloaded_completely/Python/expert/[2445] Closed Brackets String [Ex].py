"""
####  Closed Brackets String  ####

The function is given a string consisting of a collection of three characters:
___
*) "(" open bracket
*) ")" closed bracket
*) "J" Joker, which can be replaced by "(", ")" or ""
___

Develop a solution to determine if the given string represents a proper sequence of parenthesis; return True / False. Each open bracket on the left should have a corresponding closed bracket on the right. For example "(()())" is a proper sequence, "()(()" is not a proper sequence. The presence of Jokers adds an extra level of difficulty to the analysis because each "J" makes three possibilities to consider. An empty string is considered a valid string because it does not contain unbalanced brackets.


[Examples]

___
closed_brackets("(J))") ➞ True
# J can be replaced with (

closed_brackets("(") ➞ False
# Unbalanced open bracket.

closed_brackets("") ➞ True
# Empty string is a valid sequence.

closed_brackets("()J(") ➞ False
# Not possible to balance the brackets.

closed_brackets("J") ➞ True
# J can be replaced with an empty string.

closed_brackets(")(") ➞ False
# Numbers of ( and ) are the same but they are in the wrong places.

closed_brackets("()") ➞ True
# A proper sequence of balanced brackets.
_____



[Notes]

N/A


[algorithms] [data_structures] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python If ... Else
https://www.w3schools.com/python/python_conditions.asp
Equals: a == b Not Equals: a != b Less than: a < b Less than or equal to: a <= b Greater than: a > b Greater than or equal to: a >= b
_________

"""
#Your code should go here:

