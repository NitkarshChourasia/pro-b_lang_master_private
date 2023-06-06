/*
####  Count the Number of Duplicate Characters  ####

Create a function that returns the amount of duplicate characters in a string. It will be case sensitive and spaces are included. If there are no duplicates, return 0.


[Examples]

___
duplicates("Hello World!") ➞ 3
// "o" = 2, "l" = 3.
// "o" is duplicated 1 extra time and "l" is duplicated 2 extra times.
// Hence 1 + 2 = 3

duplicates("foobar") ➞ 1

duplicates("helicopter") ➞ 1

duplicates("birthday") ➞ 0
// If there are no duplicates, return 0
_____



[Notes]

Make sure to only start counting the second time a character appears.


[arrays] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::count
https://www.geeksforgeeks.org/std-count-cpp-stl/
Returns number of occurrences of an element in a given range. Returns the number of elements in the range [first,last) that compare equal to val.
_________
_________
std::unordered_map
https://www.cplusplus.com/reference/unordered_map/unordered_map/
Are associative containers that store elements formed by the combination of a key value and a mapped value, and which allows for fast retrieval of individual elements b …
_________
_________
string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments.
_________
_________
Set
https://www.geeksforgeeks.org/set-in-cpp-stl/
Are a type of associative containers in which each element has to be unique, because the value of the element identifies it. The value of the element cannot be modified …
_________

*/
//Your code should go here:

