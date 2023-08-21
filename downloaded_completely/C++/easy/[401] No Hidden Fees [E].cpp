/*
####  No Hidden Fees  ####

Given an array of prices prices and a "supposed" total t, return true if there is a hidden fee added to the total (i.e. the total is greater than the sum of prices), otherwise return false.


[Examples]

___
hasHiddenFee(["$2", "$4", "$1", "$8"], "$15") ➞ false

hasHiddenFee(["$1", "$2", "$3"], "$6") ➞ false

hasHiddenFee(["$1"], "$4") ➞ true
_____



[Notes]

___
*) Remember that each price is given as a string.
*) All $ signs will be at the beginning of the number.
___



[arrays] [language_fundamentals] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::stoi
http://www.cplusplus.com/reference/string/stoi/
Parses str interpreting its content as an integral number of the specified base, which is returned as an int value. If idx is not a null pointer, the function also set …
_________
_________
string::substr
https://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________

*/
//Your code should go here:

