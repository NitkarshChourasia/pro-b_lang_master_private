/*
####  Construct and Deconstruct  ####

Given a string, create a function which outputs an array, building and deconstructing the string letter by letter. See the examples below for some helpful guidance.


[Examples]

___
constructDeconstruct("Hello") ➞ [
  "H",
  "He",
  "Hel",
  "Hell",
  "Hello",
  "Hell",
  "Hel",
  "He",
  "H"
]

constructDeconstruct("edabit") ➞ [
  "e",
  "ed",
  "eda",
  "edab",
  "edabi",
  "edabit",
  "edabi",
  "edab",
  "eda",
  "ed",
  "e"
]

constructDeconstruct("the sun") ➞ [
  "t",
  "th",
  "the",
  "the ",
  "the s",
  "the su",
  "the sun",
  "the su",
  "the s",
  "the ",
  "the",
  "th",
  "t"
]
_____



[Notes]

Include spaces (see example #3).


[arrays] [language_fundamentals] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________
_________
Reverse
https://en.cppreference.com/w/cpp/algorithm/reverse
Reverses the order of the elements in the range [first, last].
_________
_________
std::reverse()
https://www.geeksforgeeks.org/stdreverse-in-c/
Is a predefined function in header file algorithm. It is defined as a template in the above mentioned header file. It reverses the order of the elements in the range [f …
_________

*/
//Your code should go here:

