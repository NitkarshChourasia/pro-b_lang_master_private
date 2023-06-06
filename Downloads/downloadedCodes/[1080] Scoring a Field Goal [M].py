"""
####  Scoring a Field Goal  ####

In (American) Football, a team can score if they manage to kick a ball through the goal (i.e. above the crossbar and between the uprights).
Create a function that returns True if the ball 0 goes through the goal. You will be given a list of lists.


[Examples]

___
is_goal_scored([
  ["  #     #  "],
  ["  #  0  #  "],
  ["  #     #  "],
  ["  #######  "],
  ["     #     "],
  ["     #     "],
  ["     #     "]
]) ➞ True

is_goal_scored([
  ["  #0    #  "],
  ["  #     #  "],
  ["  #     #  "],
  ["  #######  "],
  ["     #     "],
  ["     #     "],
  ["     #     "]
]) ➞ True

is_goal_scored([
  ["  #     #  "],
  ["  #     #  "],
  ["  #     # 0"],
  ["  #######  "],
  ["     #     "],
  ["     #     "],
  ["     #     "]
]) ➞ False
_____



[Notes]

___
*) All goals will be of the same size.
*) All lists will be of equal length (11).
*) A team can never score if it hits the crossbar or goes underneath it.
___



[arrays] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
index() Method
https://www.programiz.com/python-programming/methods/list/index
Searches an element in the list and returns its index.
_________
_________
any() function
https://www.w3schools.com/python/ref_func_any.asp
Returns True if any item in an iterable is true, otherwise, it returns False.
_________

"""
#Your code should go here:

