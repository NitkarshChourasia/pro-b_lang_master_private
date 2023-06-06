"""
####  An OSHA Approved Ladder?  ####

Due to a huge scandal about the Laddersons Ladder Factory creating faulty ladders, the Occupational Safety and Health Administration require your help in determining whether a ladder is safe enough for use in the work place! It is vital that a ladder passes all criterea:
___
*) The ladder must be at least 5 characters wide.
*) The ladder mustn't have more than a 2 character gap between rungs.
*) Rungs must be evenly spaced apart.
*) Rungs should not be broken (i.e. no gaps).
___

Given a ladder (drawn as a list of strings) return True if it passes all of OSHA's criterea.


[Examples]

___
is_ladder_safe([
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]) ➞ True
_____

___
is_ladder_safe([
  "#   #",
  "#####",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]) ➞ False

# Uneven spaces between rungs.
_____

___
is_ladder_safe([
  "#  #",
  "####",
  "#  #",
  "#  #",
  "####",
  "#  #",
  "#  #",
  "####",
  "#  #"
]) ➞ False

# Ladder is too narrow, should be at least 5 characters wide.
_____

___
is_ladder_safe([
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]), ➞ False

# Gap between rungs is too wide, should be less than 3.
_____

___
is_ladder_safe([
  "#   #",
  "#  ##",
  "#   #",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]) ➞ False

# The top rung is broken.
_____



[Notes]

___
*) There will be a one character space with no rung at the top and bottom of every ladder.
*) The height of the ladder is not needed for solving this problem.
___



[arrays] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
any() Function
https://www.programiz.com/python-programming/methods/built-in/any
Returns True if any element of an iterable is True. If not, it returns False.
_________
_________
all() Function
https://www.programiz.com/python-programming/methods/built-in/all
Returns True if all elements in the given iterable are true. If not, it returns False.
_________

"""
#Your code should go here:

