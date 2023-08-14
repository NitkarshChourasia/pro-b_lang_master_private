"""
####  Widen the Streets!  ####

Given a list of strings depicting a row of buildings, create a function which sets the gap between buildings as a given amount.


[Examples]

___
widen_streets([
  "###   ## #",
  "### # ## #",
  "### # ## #",
  "### # ## #",
  "### # ## #"
], 3) ➞
[
  "###       ##   #",
  "###   #   ##   #",
  "###   #   ##   #",
  "###   #   ##   #",
  "###   #   ##   #"
]

widen_streets([
  "## ### ###",
  "## ### ###",
  "## ### ###",
  "## ### ###"
], 2) ➞
[
  "##  ###  ###",
  "##  ###  ###",
  "##  ###  ###",
  "##  ###  ###"
]

widen_streets([
  "# # # # #"
], 2) ➞
[
  "#  #  #  #  #"
]
_____



[Notes]

___
*) Buildings may be different sizes.
*) There will always be a starting gap size of one character.
___



[arrays] [formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
len() Function
https://www.w3schools.com/python/ref_func_len.asp
Returns the number of items in an object.
_________

"""
#Your code should go here:

