/*
####  Filter by Digit Length  ####

Create a function that filters out an array to include numbers that only have a certain number of digits.


[Examples]

___
filterDigitLength([88, 232, 4, 9721, 555], 3) ➞ [232, 555]
// Include only numbers with 3 digits.

filterDigitLength([2, 7, 8, 9, 1012], 1) ➞ [2, 7, 8, 9]
// Include only numbers with 1 digit.

filterDigitLength([32, 88, 74, 91, 300, 4050], 1) ➞ []
// No numbers with only 1 digit exist => return empty array.

filterDigitLength([5, 6, 8, 9], 1) ➞ [5, 6, 8, 9]
// All numbers in the array have 1 digit only => return original array.
_____



[Notes]

___
*) If no numbers of the specified digit length exist, return an empty array.
*) If all numbers in the array have the specified digit length, return the original array.
*) The sub-array returned should have the same relative order as the original array.
___



[arrays] [higher_order_functions] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
remove_if
http://www.cplusplus.com/reference/algorithm/remove_if/?kw=remove_if
Remove elements from range. Transforms the range [first,last) into a range with all the elements for which pred returns true removed, and returns an iterator to the ne …
_________
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Returns a string with the representation of val.
_________
_________
log10
http://www.cplusplus.com/reference/cmath/log10/
Compute common logarithm. Returns the common (base-10) logarithm of x.
_________

*/
//Your code should go here:

