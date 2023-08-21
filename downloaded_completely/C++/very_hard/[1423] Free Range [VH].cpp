/*
####  Free Range  ####

Create a function which converts an ordered number array into a array of ranges (represented as strings). Note how some arrays have some numbers missing.


[Examples]

___
numbersToRanges([1, 2, 3, 4, 5]) ➞ ["1-5"]

numbersToRanges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]

numbersToRanges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]

numbersToRanges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]
_____



[Notes]

___
*) If there are no numbers consecutive to a number in the array, represent it as only the string version of that number (see example #4).
*) Return an empty array if the given array is empty.
___



[arrays] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

