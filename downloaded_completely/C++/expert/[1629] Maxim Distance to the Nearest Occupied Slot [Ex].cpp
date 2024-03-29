/*
####  Maxim Distance to the Nearest Occupied Slot  ####

The function is given a string consisting from "0", "1" characters. The string represents a parking area:
___
*) "1" - the slot is occupied,
*) "0" - the slot is vacant.
___

Find a vacant slot such that it has the maximum distance from an occupied one. It can be at the ends of the area or between two "1"s. Return the maximum distance as integer.


[Examples]

___
maxDistance("01") ➞ 1
// Only the first slot is vacant. Take it. The distance is 1.

maxDistance("100") ➞ 2
// Take the last slot on the right. The distance is 2.

maxDistance("100000101") ➞ 3
// Take the slot at index 3. The distance is 3.

maxDistance("000010000001001") ➞ 4
// Take the slot at index 0. The distance is 4.
// The other possible slots at indices 7, 8 have distance 3.
_____



[Notes]

N/A


[algorithms] [logic] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Substring in C++
https://www.geeksforgeeks.org/substring-in-cpp/
The substring function is used for handling string operations like strcat(), append(), etc. It generates a new string with its value initialized to a copy of a sub-stri …
_________

*/
//Your code should go here:

