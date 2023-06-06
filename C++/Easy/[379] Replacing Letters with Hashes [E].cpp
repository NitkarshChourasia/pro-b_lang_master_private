/*
####  Replacing Letters with Hashes  ####

Write a function that replaces all letters within a specified range with the hash symbol #.


[Examples]

___
replace("abcdef", "c-e") ➞ "ab###f"

replace("rattle", "r-z") ➞ "#a##le"

replace("microscopic", "i-i") ➞ "m#croscop#c"

replace("", "a-z") ➞ ""
_____



[Notes]

___
*) The range will always be in order, a.k.a. for m-n, character m will always come before or equal n.
*) Strings will be in lower case letters only.
*) Return an empty string if the input is an empty string.
___



[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Regular Expressions Library
https://en.cppreference.com/w/cpp/regex
The regular expressions library provides a class that represents regular expressions, which are a kind of mini-language used to perform pattern matching within strings. …
_________
_________
std::transform
http://www.cplusplus.com/reference/algorithm/transform/?kw=transform
Applies an operation sequentially to the elements of one (1) or two (2) ranges and stores the result in the range that begins at result.
_________

*/
//Your code should go here:

