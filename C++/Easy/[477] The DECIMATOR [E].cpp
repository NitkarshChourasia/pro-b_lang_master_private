/*
####  The DECIMATOR  ####

Write a DECIMATOR function which takes a string and decimates it (i.e. it removes the last 1/10 of the characters).
Always round up: if the string has 21 characters, 1/10 of the characters would be 2.1 characters, hence the DECIMATOR removes 3 characters. The DECIMATOR shows no mercy!


[Examples]

___
DECIMATOR("1234567890") ➞ "123456789"
// 10 characters, removed 1.

DECIMATOR("1234567890AB") ➞ "1234567890"
// 12 characters, removed 2.

DECIMATOR("123") ➞ "12"
// 3 characters, removed 1.

DECIMATOR("123456789012345678901") ➞ "123456789012345678"
// 21 characters, removed 3.
_____



[Notes]

Make sure to remove characters from the end of the string.


[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Ceil and Floor Functions
https://www.geeksforgeeks.org/ceil-floor-functions-cpp/
In mathematics and computer science, the floor and ceiling functions map a real number to the greatest preceding or the least succeeding integer, respectively. floor(x …
_________
_________
Ceil
https://www.cplusplus.com/reference/cmath/ceil/
Rounds x upward, returning the smallest integral value that is not less than x.
_________
_________
erase
https://www.cplusplus.com/reference/string/string/erase/
Erases part of the string, reducing its length.
_________

*/
//Your code should go here:

