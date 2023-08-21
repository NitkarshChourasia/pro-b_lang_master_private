/*
####  Omnipresent Value  ####

A value is omnipresent if it exists in every subarray inside the main array.
To illustrate:
___
[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// 3 exists in every element inside this array, so is omnipresent.
_____

Create a function that determines whether an input value is omnipresent for a given array.


[Examples]

___
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true

isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false

isOmnipresent([[5], [5], [5], [6, 5]], 5) ➞ true

isOmnipresent([[5], [5], [5], [6, 5]], 6) ➞ false
_____



[Notes]

Sub-arrays can be any length.


[algorithms] [arrays] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::find
https://www.geeksforgeeks.org/std-find-in-cpp/
Finds the element in the given range of numbers. Returns an iterator to the first element in the range [first,last) that compares equal to val. If no such element is fo …
_________
_________
Check if a vector contains a given element or not in C++
https://www.techiedelight.com/check-vector-contains-given-element-cpp/
Searching for an element in a vector is linear time operation unless the vector is sorted. The header offers many functions that we can use for searching.
_________
_________
std::find_if_not
http://www.cplusplus.com/reference/algorithm/find_if_not/
Find element in range (negative condition). Returns an iterator to the first element in the range [first,last) for which pred returns false. If no such element is found …
_________

*/
//Your code should go here:

