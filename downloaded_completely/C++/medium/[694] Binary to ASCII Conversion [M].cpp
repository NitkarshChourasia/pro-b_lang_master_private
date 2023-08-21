/*
####  Binary to ASCII Conversion  ####

Create a function that takes a string of 1's and 0's (binary) as an argument and return the equivalent decoded ASCII text. Characters can be in the range of "00000000" to "11111111", which means every eight digits of binary input represents a single character.
___
*) a = 01100001
*) b = 01100010
*) c = 01100011
___

If you were to combine these characters into the string "abc", the corresponding binary would be 011000010110001001100011. Use the resources tab for more info on how to approach this.


[Examples]

___
binaryConversion("011001010110010001100001011000100110100101110100") ➞ "edabit"

binaryConversion("001100010011001000110011") ➞ "123"

binaryConversion("010010000110010101101100011011000110111100111111") ➞ "Hello?"
_____



[Notes]

If you are given an empty string as input, you must also return an empty string. Otherwise, the input will always be a valid binary string.


[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::stoi, std::stol, std::stoll
https://devdocs.io/cpp/string/basic_string/stol
Interprets a signed integer value in the string str.
_________
_________
std::bitset
https://devdocs.io/cpp/utility/bitset
The class template bitset represents a fixed-size sequence of N bits. (initialized with constructor).
_________

*/
//Your code should go here:

