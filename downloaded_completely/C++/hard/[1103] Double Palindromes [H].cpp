/*
####  Double Palindromes  ####

Strings can be segregated into both their letter and digit components.

To illustrate:
___
"cab97ac79" // double-palindrome
// "cabac" and "9779" are both palindromes.

"1abc4de1" // single-palindrome
// "141" is a palindrome.
_____

Write a function that maps double palindromes to the number 2, single palindromes to the number 1, and everything else to the number 0.


[Examples]

___
palindromeSet(["cb77c", "ccc888", "ccc789", "abc89"]) ➞ [2, 2, 1, 0]

palindromeSet(["789", "555", "ccc", "abba"]) ➞ [0, 1, 1, 1]

palindromeSet(["7a", "5f", "6c"]) ➞ [2, 2, 2]
_____



[Notes]

___
*) A string is composed of only letters or only numbers, can be at most a single palindrome (see example #2).
*) All single character components are trivially palindromes (see example #3).
*) All letters will be lower cased.
___



[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::reverse()
https://www.geeksforgeeks.org/stdreverse-in-c/
Is a predefined function in header file algorithm. It is defined as a template in the above mentioned header file. It reverses the order of the elements in the range [f …
_________
_________
Palindrome
https://en.wikipedia.org/wiki/Palindrome
Is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam, racecar.
_________

*/
//Your code should go here:

