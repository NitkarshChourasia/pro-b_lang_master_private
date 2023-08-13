"""
####  Coin Trouble  ####

Given a list of coins, father needs to distribute them amongst his three children. Write a function to determine if the coins can be distributed equally or not. Return True if each son receives the same amount of money, otherwise return False.
___
[1, 2, 3, 2, 2, 2, 3] ➞ True
_____

___
*) Amount to be distributed to each child = (1+2+3+2+4+3)/3 => 15/3 => 5
*) Possible set of coin to be distributed to children = [(1,2,2),(2,3),(2,3)]
___

___
[5, 3, 10, 1, 2] ➞ False
_____

___
*) Amount to be distributed to each child = (5+3+10+1+2)/3 => 21/3 => 7
*) But there are no combination such that each child get equal value which is 7.
___



[Examples]

___
coins_div([1, 2, 3, 2, 2, 2, 3]) ➞ True

coins_div([5, 3, 10, 1, 2]) ➞ False

coins_div([2, 4, 3, 2, 4, 9, 7, 8, 6, 9]) ➞ True
_____



[Notes]

___
*) Inputs will be an array of positive integers only.
*) Coin can be any positive value.
___



[arrays] [logic] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
counter() Method
https://docs.python.org/3/library/collections.html#collections.Counter
A dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts …
_________

"""
#Your code should go here:

