/*
####  Consecutive Numbers  ####

Given an array of random digits of any length, return true if the number n appears times times in a row, and false otherwise.


[Worked Example]

___
IsThereConsecutive(new int[] { 1, 3, 5, 5, 3, 3, 1 }, 3, 2) ➞ true
// Second parameter is the number to look out for (3).
// Third parameter means you need to find the number 3 twice in a row.
// Return true if it can be found.
_____



[Examples]

___
IsThereConsecutive(new int[] { 1, 2, 3, 4, 5 }, 1, 1) ➞ true

IsThereConsecutive(new int[] { 3 }, 1, 0) ➞ true

IsThereConsecutive(new int[] { 2, 2, 3, 2, 2, 2, 2, 3, 4, 1, 5 }, 3, 2) ➞ false

IsThereConsecutive(new int[] { 5, 5, 5, 5, 5 }, 5, 7) ➞ false
_____



[Notes]

___
*) Arrays will only contain positive single digit numbers.
*) Expect all parameters to be valid.
___



[arrays] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Enumerable.Repeat() Method
https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.repeat
Generates a sequence that contains one repeated value.
_________
_________
string.contains() Method
https://docs.microsoft.com/en-us/dotnet/api/system.string.contains
Returns a value indicating whether a specified character occurs within this string.
_________

*/
//Your code should go here:

