/*
####  Column With Maximum Sum  ####

Given an array of numbers and a value for n, split the numbers into n-sized groups. If we imagine that these groups are stacked on top of each other (see below), return the column number that has the greatest sum. If two or more columns have the same sum, return the one with the smallest column number.


[Example]

___
nums = [4, 14, 12, 7, 14, 16, 5, 13, 7, 16, 11, 19]
n = 4
_____

Gives the array:
___
[[4, 14, 12,  7],
[14, 16, 5, 13],
[7, 16, 11, 19]]

// 1, 2, 3, 4 (column)
// 25, 46, 28, 39 (sum)
_____

You would return 2, as the 2nd column has the greatest sum.


[Notes]

Nums will always divide into equal-length groups.


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
How to sum up elements of a C++ vector?
https://www.tutorialspoint.com/how-to-sum-up-elements-of-a-cplusplus-vector#:~:text=Sum%20up%20of%20all%20elements,vector%20to%20the%20specified%20sum.
Can be very easily done by std::accumulate method. It is defined in <numeric> header. It accumulates all the values present specified in the vector to the specified sum.
_________
_________
Modulo Operator (%)
https://www.geeksforgeeks.org/modulo-operator-in-c-cpp-with-examples
Is an arithmetic operator. The modulo division operator produces the remainder of an integer division.
_________

*/
//Your code should go here:

