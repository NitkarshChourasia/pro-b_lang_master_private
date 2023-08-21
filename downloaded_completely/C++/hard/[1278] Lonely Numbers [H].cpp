/*
####  Lonely Numbers  ####

Given a number, insert duplicate digits on both sides of all digits which appear in a group of 1.


[Worked Example]

___
numbersNeedFriendsToo(22733) ➞ 2277733

// The number can be split into groups 22, 7, and 33.
// 7 appears on its own.
// Put 7s on both sides to create 777.
// Put the numbers together and return the result.
_____



[Examples]

___
numbersNeedFriendsToo(123) ➞ 111222333

numbersNeedFriendsToo(56657) ➞ 55566555777

numbersNeedFriendsToo(33) ➞ 33
_____



[Notes]

All tests will include positive integers.


[loops] [numbers] [regex] 



-------------------------------------------------------------------
[Resources]
_________
std::stol
http://www.cplusplus.com/reference/string/stol/
Parses str interpreting its content as an integral number of the specified base, which is returned as a value of type long int.
_________
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Convert numerical value to string Returns a string with the representation of val.
_________

*/
//Your code should go here:

