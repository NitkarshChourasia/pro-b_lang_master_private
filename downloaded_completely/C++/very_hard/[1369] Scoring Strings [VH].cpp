/*
####  Scoring Strings  ####

Nesting level, for this challenge, refers to the depth of the parentheses surrounding an integer. For example, the string "(5((10)8))", 5 has a nesting level of 1 because it has one set of parentheses around it, 10 has a nesting level of 3 because it has 3 sets of parentheses around it, and 8 has a nesting level of 2.
We can score this string by multiplying each number with its nesting level and then summing up the results, as follows:
___
"(5((10)8))" ➞ 5*1 + 10*3 + 8*2 ➞ 51
_____

Create a function that takes a string as its argument and returns its score.


[Examples]

___
scoreIt("()") ➞ 0

scoreIt("4(123)") ➞ 123
// 4*0 + 123*1 = 123

scoreIt("((((1)2)3)4)") ➞ 20
// 1*4 + 2*3 + 3*2 + 4*1 = 20

scoreIt("(6)8((34(7)))") ➞ 95
// 6*1 + 8*0 + 34*2 + 7*3 = 95
_____



[Notes]

___
*) The nesting for all test cases is balanced and logically consistent (there are no missing or extra parentheses).
*) Test cases contain only positive integers.
___



[logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
isdigit() Function
https://www.programiz.com/cpp-programming/library-function/cctype/isdigit
Checks if the given character is a digit or not.
_________

*/
//Your code should go here:

