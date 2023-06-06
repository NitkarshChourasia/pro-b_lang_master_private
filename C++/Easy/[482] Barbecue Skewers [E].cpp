/*
####  Barbecue Skewers  ####

You are in charge of the barbecue grill. A vegetarian skewer is a skewer that has only vegetables (-o). A non-vegetarian skewer is a skewer with at least one piece of meat (-x).
For example, the grill below has 4 non-vegetarian skewers and 1 vegetarian skewer (the one in the middle).
___
["--xo--x--ox--",
"--xx--x--xx--",
"--oo--o--oo--",      <<< vegetarian skewer
"--xx--x--ox--",
"--xx--x--ox--"]
_____

Given a BBQ grill, write a function that returns [# vegetarian skewers, # non-vegetarian skewers]. For example above, the function should return [1, 4].


[Examples]

___
bbqSkewers( [
  "--oooo-ooo--",
  "--xx--x--xx--",
  "--o---o--oo--",
  "--xx--x--ox--",
  "--xx--x--ox--"
]) ➞ [2, 3]

bbqSkewers([
  "--oooo-ooo--",
  "--xxxxxxxx--",
  "--o---",
  "-o-----o---x--",
  "--o---o-----"
]) ➞ [3, 2]
_____



[Notes]

N/A


[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to Use the Conditional (ternary) Operator
http://www.cplusplus.com/forum/articles/14631/
The ternary operator can be used to shorten an if-else expression.
_________
_________
std::count
http://www.cplusplus.com/reference/algorithm/count/
Return the number of times a particular element occurs in a specified range.
_________

*/
//Your code should go here:

