/*
####  Filter out Strings from an Array  ####

Create a function that takes an array of non-negative integers and strings and return a new array without the strings.


[Examples]

___
filterArray([1, 2, "a", "b"]) ➞ [1, 2]

filterArray([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

filterArray([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
_____



[Notes]

___
*) Zero is a non-negative integer.
*) The given array only has integers and strings.
*) Numbers in the array should not repeat.
*) The original order must be maintained.
___



[arrays] [formatting] [loops] 



-------------------------------------------------------------------
[Resources]
_________
std::isdigit
http://en.cppreference.com/w/cpp/string/byte/isdigit
Non-zero return value if the character is a numeric character.
_________
_________
std::remove AND std::remove_if
http://en.cppreference.com/w/cpp/algorithm/remove
Removes all elements from the given range if they satisfy a specific criteria.
_________

*/
//Your code should go here:

