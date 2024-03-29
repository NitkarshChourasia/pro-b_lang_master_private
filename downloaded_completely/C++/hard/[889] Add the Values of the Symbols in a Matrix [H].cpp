/*
####  Add the Values of the Symbols in a Matrix  ####

Write a function that takes an array of arrays and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:
___
*) # = 5
*) O = 3
*) X = 1
*) ! = -1
*) !! = -3
*) !!! = -5
___

An array of arrays containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.
If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.


[Examples]

___
checkScore([
  ["#", "!"],
  ["!!", "X"]
]) ➞ 2

checkScore([
  ["!!!", "O", "!"],
  ["X", "#", "!!!"],
  ["!!", "X", "O"]
]) ➞ 0

checkScore([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
]) ➞ 12
_____



[Notes]

Strings in the arrays will only be #, O, X, !, !! and !!!.


[functional_programming] [math] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::compare
http://www.cplusplus.com/reference/string/string/compare/
Compare strings Compares the value of the string object (or a substring) to the sequence of characters specified by its arguments.
_________

*/
//Your code should go here:

