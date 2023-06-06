/*
####  Simon Says  ####

Create a function that takes in two arrays and returns true if the second array follows the first array by one element, and false otherwise. In other words, determine if the second array is the first array shifted to the right by 1.


[Examples]

___
simonSays([1, 2], [5, 1]) ➞ true

simonSays([1, 2], [5, 5]) ➞ false

simonSays([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ true

simonSays([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ false
_____



[Notes]

___
*) Both input arrays will be of the same length, and will have a minimum length of 2.
*) The values of the 0-indexed element in the second list and the n-1th indexed element in the first list do not matter.
___



[arrays] [games] [validation] 



-------------------------------------------------------------------
[Resources]
_________
array::size
https://www.includehelp.com/stl/array-size-in-cpp-stl-with-example.aspx
Returns the size of the array (Note: "size()" can also be used for other containers like list etc).
_________
_________
vector::erase
http://www.cplusplus.com/reference/vector/vector/erase/
Removes from the vector either a single element (position) or a range of elements ([first, last)).
_________
_________
vector::pop_back
http://www.cplusplus.com/reference/vector/vector/pop_back/
Removes the last element in the vector, effectively reducing the container size by one.
_________
_________
std::equal
https://en.cppreference.com/w/cpp/algorithm/equal
If the elements in the two ranges are equal, returns true. Otherwise returns false.
_________

*/
//Your code should go here:

