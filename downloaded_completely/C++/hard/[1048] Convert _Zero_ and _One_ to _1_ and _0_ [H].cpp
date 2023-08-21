/*
####  Convert "Zero" and "One" to "1" and "0"  ####

Create a function that takes a string as an argument. The function must return a string containing 1s and 0s based on the string argument's words. If any word in the argument is not equal to "zero" or "one" (case insensitive), you should ignore it. The returned string's length should be a multiple of 8, if the string is not a multiple of 8 you should remove the numbers in excess.


[Examples]

___
textToNumberBinary("zero one zero one zero one zero one") ➞ "01010101"

textToNumberBinary("Zero one zero ONE zero one zero one") ➞ "01010101"

textToNumberBinary("zero one zero one zero one zero one one two") ➞ "01010101"

textToNumberBinary("zero one zero one zero one zero three") ➞ ""

textToNumberBinary("one one") ➞ ""
_____



[Notes]

You must return the result as a string.


[arrays] [formatting] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
tolower()
http://www.cplusplus.com/reference/cctype/tolower/
Converts c to its lowercase equivalent if c is an uppercase letter and has a lowercase equivalent. If no such conversion is possible, the value returned is c unchanged.
_________

*/
//Your code should go here:

