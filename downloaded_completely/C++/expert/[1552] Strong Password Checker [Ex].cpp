/*
####  Strong Password Checker  ####

A password is considered strong if all the following conditions are met:

Write a function that takes a string str and return the MINIMUM change required to make it a strong password. If it's already strong, return 0.


[Examples]

___
strongPasswordChecker("Edabit!") ➞ 1
// 7 characters total, need to add one more digit for a strong password.
// 1 minimum change.

strongPasswordChecker("edabit1!") ➞ 1
// 8 characters total, need to add an uppercase letter.
// 1 minimum change.

strongPasswordChecker("EDABITEDABITEDABITEDA") ➞ 3
// 21 characters total, only uppercase letters, need to delete one
// character and replace two characters, 1 with a digit, 1 with a
// lowercase letter.
// 3 minimum changes.

strongPasswordChecker("Edaaaabit!!1") ➞ 1
// Contains more than 3 repeating characters in a row - "aaaa", need
// to replace an "a" with a different character (e.g. "a3aa" or in some
// cases add a character in the middle "aa2aa".
// 1 minimum change.
_____



[Notes]

___
*) Insertion, deletion or replacement of any one character is considered one change.
*) Spaces will be ignored for this challange.
___



[functional_programming] [higher_order_functions] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

