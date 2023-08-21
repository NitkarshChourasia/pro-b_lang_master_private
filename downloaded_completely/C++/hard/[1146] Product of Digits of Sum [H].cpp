/*
####  Product of Digits of Sum  ####

Create a function that takes an array of numbers and adds them together to get a new number. The function then repeatedly multiplies the digits of the new number by each other, yielding a new number, until the product is only 1 digit long. Return the final product.


[Examples]

___
sumDigProd([16, 28]) ➞ 6
// 16 + 28 = 44
// 4 * 4 =  16
// 1 * 6 = 6

sumDigProd([0]) ➞ 0

sumDigProd([1, 2, 3, 4, 5, 6]) ➞ 2
_____



[Notes]

The input of the function is at least one number.


[arrays] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
std::accumulate
https://en.cppreference.com/w/cpp/algorithm/accumulate
Computes the sum of the given value init and the elements in the range [first, last). The first version uses operator+ to sum up the elements, the second version uses t …
_________

*/
//Your code should go here:

