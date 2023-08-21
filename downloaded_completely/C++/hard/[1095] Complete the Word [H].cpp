/*
####  Complete the Word  ####

An input string can be completed if additional letters can be added and no letters need to be taken away to match the word. Furthermore, the order of the letters in the input string must be the same as the order of letters in the final word.
Create a function that, given an input string, determines if the word can be completed.


[Examples]

___
canComplete("butl", "beautiful") ➞ true
// We can add "ea" between "b" and "u", and "ifu" between "t" and "l".

canComplete("butlz", "beautiful") ➞ false
// "z" does not exist in the word beautiful.

canComplete("tulb", "beautiful") ➞ false
// Although "t", "u", "l" and "b" all exist in "beautiful", they are incorrectly ordered.

canComplete("bbutl", "beautiful") ➞ false
// Too many "b"s, beautiful has only 1.
_____



[Notes]

Both string input and word will be lowercased.


[loops] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Regular Expressions Library
https://en.cppreference.com/w/cpp/regex
The regular expressions library provides a class that represents regular expressions, which are a kind of mini-language used to perform pattern matching within strings.
_________

*/
//Your code should go here:

