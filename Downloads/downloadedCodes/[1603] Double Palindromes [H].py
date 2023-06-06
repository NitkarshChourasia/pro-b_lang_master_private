"""
####  Double Palindromes  ####

Strings can be segregated into both their letter and digit components.

To illustrate:
___
"cab97ac79"
# double-palindrome: "cabac" and "9779" are both palindromes.

"1abc4de1"
# single-palindrome: "141" is a palindrome.
_____

Write a function that maps double palindromes to the number 2, single palindromes to the number 1, and everything else to the number 0.


[Examples]

___
palindrome_set(["cb77c", "ccc888", "ccc789", "abc89"]) ➞ [2, 2, 1, 0]

palindrome_set(["789", "555", "ccc", "abba"]) ➞ [0, 1, 1, 1]

palindrome_set(["7a", "5f", "6c"]) ➞ [2, 2, 2]
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
IF...ELSE
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics: Equals: a == b Not Equals: a != b Less than: a < b Less than or equal to: a <= b Greater than: a > b Grea …
_________
_________
How to retrieve an element from a set without removing it?
https://stackoverflow.com/questions/59825/how-to-retrieve-an-element-from-a-set-without-removing-it
How do I get a value (any value) out of s without doing s.pop()? I want to leave the item in the set until I am sure I can remove it - something I can only be sure of a …
_________

"""
#Your code should go here:

