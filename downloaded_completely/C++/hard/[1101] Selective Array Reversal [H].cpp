/*
####  Selective Array Reversal  ####

Create a function that takes an array and a number and selectively reverse the order of the array based on the number you're given (second argument). If you're given the arguments [1,2,3,4,5,6] and 2, you would return the array [2,1, 4,3, 6,5].


[Examples]

___
selReverse([1,2,3,4,5,6], 2) ➞ [2,1, 4,3, 6,5]

selReverse([2,4,6,8,10,12,14,16], 3) ➞ [6,4,2, 12,10,8, 16,14]

selReverse([5,7,2,6,0,4,6], 100) ➞ [6,4,0,6,2,7,5]
_____



[Notes]

___
*) If the array you're given can't be broken up into equal parts, just reverse the remaining numbers (see 2nd expample).
*) If len exceeds the array length, reverse everything.
*) If len is zero, return the original array.
___



[algorithms] [arrays] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
std::rbegin, std::crbegin
https://en.cppreference.com/w/cpp/iterator/rbegin
Returns an iterator to the reverse-beginning of the given container c or array array.
_________
_________
std::reverse
https://en.cppreference.com/w/cpp/algorithm/reverse
Reverses the order of the elements in the range [first, last).
_________
_________
std::reverse_copy
https://en.cppreference.com/w/cpp/algorithm/reverse_copy
Copies the elements from the range [first, last) to another range beginning at d_first in such a way that the elements in the new range are in reverse order.
_________
_________
Substring
https://www.tutorialspoint.com/substring-in-cplusplus#:~:text=A%20substring%20is%20a%20part%20of%20a%20string.,substring%20in%20C%2B%2B%20is%20given%20as%20follows%20%E2%88%92
A substring is a part of a string. A function to obtain a substring in C++ is substr(). This function contains two parameters: pos and len. T ...
_________

*/
//Your code should go here:

