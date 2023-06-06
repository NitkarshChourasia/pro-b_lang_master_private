/*
####  Typing Game  ####

You're in the midst of creating a typing game.
Create a function that takes in two arrays: the array of user-typed words, and the array of correctly-typed words and outputs an array containing 1s (correctly-typed words) and -1s (incorrectly-typed words).
___
Inputs:
User-typed Array: ["cat", "blue", "skt", "umbrells", "paddy"]
Correct Array: ["cat", "blue", "sky", "umbrella", "paddy"]

Output: [1, 1, -1, -1, 1]
_____



[Examples]

___
correctStream(
  ["it", "is", "find"],
  ["it", "is", "fine"]
) ➞ [1, 1, -1]

correctStream(
  ["april", "showrs", "bring", "may", "flowers"],
  ["april", "showers", "bring", "may", "flowers"]
) ➞ [1, -1, 1, 1, 1]
_____



[Notes]

The input array lengths will always be the same.


[arrays] [games] [loops] 



-------------------------------------------------------------------
[Resources]
_________
std::vector::push_back
http://www.cplusplus.com/reference/vector/vector/push_back/
Adds an element to the end of an array.
_________
_________
std::vector::size
http://www.cplusplus.com/reference/vector/vector/size/
Returns the number of elements in a vector.
_________
_________
std::generate
http://www.cplusplus.com/reference/algorithm/generate/
Generate values for range with function. Assigns the value returned by successive calls to gen to the elements in the range [first,last).
_________

*/
//Your code should go here:

