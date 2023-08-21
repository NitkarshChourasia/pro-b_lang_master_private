/*
####  Number Pairs  ####

Create a function that determines how many number pairs are embedded in a space-separated string. The first numeric value in the space-separated string represents the count of the numbers, thus, excluded in the pairings.


[Examples]

___
numberPairs("7 1 2 1 2 1 3 2") ➞ 2
// (1, 1), (2, 2)

numberPairs("9 10 20 20 10 10 30 50 10 20") ➞ 3
// (10, 10), (20, 20), (10, 10)

numberPairs("4 2 3 4 1") ➞ 0
// Although two 4's are present, the first one is discounted.
_____



[Notes]

Always take into consideration the first number in the string is not part of the pairing, thus, the count. It may not seem so useful as most people see it, but it's mathematically significant if you deal with set operations.


[arrays] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

