/*
####  Upper or Lower Case  ####

Return the smallest number of steps it takes to convert a string entirely into uppercase or entirely into lower case, whichever takes the fewest number of steps. A step consists of changing one character from lower to upper case, or vice versa.


[Examples]

___
stepsToConvert("abC") ➞ 1
// "abC" converted to "abc" in 1 step

stepsToConvert("abCBA") ➞ 2
// "abCBA" converted to "ABCBA" in 2 steps

stepsToConvert("aba") ➞ 0

stepsToConvert("abaCCC") ➞ 3
_____



[Notes]

___
*) Return 0 if empty string.
*) Return 0 if the string is already entirely in one case.
*) Only alphabetic characters.
*) Input has no spaces.
___



[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
isupper
http://www.cplusplus.com/reference/cctype/isupper/
Checks if parameter c is an uppercase alphabetic letter.
_________
_________
islower
http://www.cplusplus.com/reference/cctype/islower/
Checks whether c is a lowercase letter.
_________
_________
min
https://www.cplusplus.com/reference/algorithm/min/
Returns the smallest of a and b. If both are equivalent, a is returned.
_________
_________
toupper
http://www.cplusplus.com/reference/cctype/toupper/
Converts c to its uppercase equivalent if c is a lowercase letter and has an uppercase equivalent. If no such conversion is possible, the value returned is c unchanged.
_________
_________
tolower
http://www.cplusplus.com/reference/cctype/tolower/
Converts c to its lowercase equivalent if c is an uppercase letter and has a lowercase equivalent. If no such conversion is possible, the value returned is c unchanged.
_________

*/
//Your code should go here:

