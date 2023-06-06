/*
####  Character Code Math  ####

Turn each character in a string str into its ASCII character code and join them together to create a number.
For example, for string "abc", the number is 979899. We will call this number "num1".
___
"abc" ➞ "a" = 97, "b" = 98, "c" = 99 ➞ 979899
_____

Then replace any incidence of the number 7 with the number 1, and call this number "num2":
___
num1 = 979899

num2 = 919899
_____

Return the difference between the sum of the digits in num1 and num2:
___
  (9 + 7 + 9 + 8 + 9 + 9)
- (9 + 1 + 9 + 8 + 9 + 9)
-------------------------
         ➞  6
_____



[Examples]

___
calc("ABCDabcd") ➞ 12

calc("cdefgh") ➞ 0

calc("ifkhchlhfde") ➞ 6
_____



[Notes]

Lowercase and uppercase characters have different ASCII character codes.


[algorithms] [language_fundamentals] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
count
https://en.cppreference.com/w/cpp/algorithm/count
Returns the number of elements in the range [first, last) satisfying specific criteria.
_________

*/
//Your code should go here:

