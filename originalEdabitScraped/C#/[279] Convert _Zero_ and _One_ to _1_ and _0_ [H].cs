/*
####  Convert "Zero" and "One" to "1" and "0"  ####

Create a function that takes a string as an argument. The function must return a string containing 1s and 0s based on the string argument's words. If any word in the argument is not equal to "zero" or "one" (case insensitive), you should ignore it. The returned string's length should be a multiple of 8, if the string is not a multiple of 8 you should remove the numbers in excess.


[Examples]

___
TextToNumberBinary("zero one zero one zero one zero one") ➞ "01010101"

TextToNumberBinary("Zero one zero ONE zero one zero one") ➞ "01010101"

TextToNumberBinary("zero one zero one zero one zero one one two") ➞ "01010101"

TextToNumberBinary("zero one zero one zero one zero three") ➞ ""

TextToNumberBinary("one one") ➞ ""
_____



[Notes]

You must return the result as a string.


[arrays] [formatting] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Is there a C# case insensitive equals operator?
https://stackoverflow.com/questions/631233/is-there-a-c-sharp-case-insensitive-equals-operator
I know that the following is case sensitive: if (StringA == StringB) So is there an operator which will compare two strings in an insensitive manner?
_________

*/
//Your code should go here:

