/*
####  Is This a Full Cycle?  ####

Say you want to traverse an array of integers starting at the first item and using each value as a pointer of what item to visit next. For example, you would traverse the array [1, 4, 3, 0, 2] in the following manner:

Because you visit every item once and go back to the starting point, the array [1, 4, 3, 0, 2] is a "full cycle".
Create a function that returns true if the input array is a full cycle, or false otherwise.


[Examples]

___
fullCycle([1, 4, 3, 0, 2]) ➞ true

fullCycle([1, 4, 0, 3, 2]) ➞ false

fullCycle([5, 3, 4, 2, 0, 1]) ➞ true
_____



[Notes]

Test arrays won't include any negative integers.


[algorithms] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::sort
https://www.geeksforgeeks.org/sort-c-stl/
Generally takes two parameters , the first one being the point of the array/vector from where the sorting needs to begin and the second parameter being the length up to …
_________

*/
//Your code should go here:

