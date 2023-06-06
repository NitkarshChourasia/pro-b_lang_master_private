/*
####  Mini Peaks  ####

Write a function that returns all the elements in an array that are strictly greater than their adjacent left and right neighbors.


[Examples]

___
miniPeaks([4, 5, 2, 1, 4, 9, 7, 2]) ➞ [5, 9]
// 5 has neighbours 4 and 2, both are less than 5.

miniPeaks([1, 2, 1, 1, 3, 2, 5, 4, 4]) ➞ [2, 3, 5]

miniPeaks([1, 2, 3, 4, 5, 6]) ➞ []
_____



[Notes]

___
*) Do not count boundary numbers, since they only have one left/right neighbor.
*) If no such numbers exist, return an empty array.
___



[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Check if a Vector Contains a Given Element or Not
https://www.techiedelight.com/check-vector-contains-given-element-cpp/
The simplest solution is to count the total number of elements in the vector having the specified value. If the count is nonzero, we have found our element. This can be …
_________
_________
Range-based for loop
https://en.cppreference.com/w/cpp/language/range-for
Used as a more readable equivalent to the traditional for loop operating over a range of values, such as all elements in a container.
_________

*/
//Your code should go here:

