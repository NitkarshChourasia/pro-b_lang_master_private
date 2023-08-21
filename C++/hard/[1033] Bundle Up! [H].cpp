/*
####  Bundle Up!  ####

Let's assume for the purposes of this challenge that for every layer of fabric you wear when it's cold outside (coats, cardigans, etc), the temperature increases by a tenth of the total.
Given n number of layers and a given temperature, return the temperature inside of all those warm fuzzy layers. Round to the nearest tenth of a degree.
___
calcBundledTemp(2, "10*C") ➞ "12.1*C"
// 10 * 1.1 = 11
// 11 * 1.1 = 12.1
_____



[Examples]

___
calcBundledTemp(1, "2*C") ➞ "2.2*C"

calcBundledTemp(4, "6*C") ➞ "8.8*C"

calcBundledTemp(20, "4*C") ➞ "26.9*C"
_____



[Notes]

___
*) The temperature will be given in Celsius and as a string.
*) Note that the degrees sign is given as an asterisk.
___



[loops] [math] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

