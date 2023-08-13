"""
####  Evaluate the Group of Parentheses  ####

The function is given a balanced parentheses string. Each open "(" has corresponding closed ")". Compute the total score based on the following rules:
___
*) Substring s = "()" has score 1,
*) Substring "s1s2" has total score as score of "s1" + score of "s2",
*) Substring "(s)" has total score as 2 * score of "s".
___

Calculate the total score of the given expression and return it as integer.


[Examples]

___
eval_parentheses("()") ➞ 1
# 1

eval_parentheses("(())") ➞ 2
# 2 * 1

eval_parentheses("()()") ➞ 2
# 1 + 1

eval_parentheses("((())())") ➞ 6
# 2 * (2 * 1 + 1)

eval_parentheses("(()(()))") ➞ 6
# 2 * (1 + 2 * 1)

eval_parentheses("()(())") ➞ 3
# 1 + 2 * 1

eval_parentheses("()((()))") ➞ 5
# 1 + 2 * 2 * 1
_____



[Notes]

N/A


[algorithms] [logic] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Stack in Python
https://www.geeksforgeeks.org/stack-in-python/
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and a …
_________

"""
#Your code should go here:

