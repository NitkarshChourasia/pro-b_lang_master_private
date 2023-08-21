/*
####  Digits Recovery  ####

Mubashir shuffled a given string of letters by mistake. Some letters in the input string are representing a digit (from zero to nine). Help him to recover all the digits.
___
*) Only consecutive letters can be used. "OTNE" cannot be recovered to 1.
*) Every letter has to start with an increasing index. "ONENO" results to 11, because E can be used two times.
*) You can ignore all letters in the string if they don't end-up in a digit.
*) If no digits can be found, return "No digits found"
*) Take care about the order! "ENOWT" will be recovered to 12 and not to 21.
*) The input string consists only UpperCase letters.
___



[Examples]

___
digitsRecovery("NEO") ➞ "1"

digitsRecovery("ONETWO") ➞ "12"

digitsRecovery("ZYX") ➞ "No digits found"

digitsRecovery("NEOTWONEINEIGHTOWSVEEN") ➞ "12219827"
_____



[Notes]

N/A


[algorithms] [logic] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string
https://www.cplusplus.com/reference/string/string/
Strings are objects that represent sequences of characters. The standard string class provides support for such objects with an interface similar to that of a standard …
_________

*/
//Your code should go here:

