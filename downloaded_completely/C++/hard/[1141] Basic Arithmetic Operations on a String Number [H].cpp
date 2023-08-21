/*
####  Basic Arithmetic Operations on a String Number  ####

Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 / 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.
In case of division, whenever the second number equals "0" return -1.
For example:
___
"15 / 0"  ➞ -1
_____



[Examples]

___
arithmeticOperation("12 + 12") ➞ 24 // 12 + 12 = 24

arithmeticOperation("12 - 12") ➞ 0 // 12 - 12 = 0

arithmeticOperation("12 * 12") ➞ 144 // 12 * 12 = 144

arithmeticOperation("12 / 0") ➞ -1 // 12 / 0 = -1
_____



[Notes]

___
*) All the inputs are only integers.
*) The operators are * - + and /.
*) Hint: Think about the single space that appears before and after the arithmetic operator.
___



[arrays] [control_flow] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
atoi() Function
https://www.geeksforgeeks.org/write-your-own-atoi/
Takes a string (which represents an integer) as an argument and returns its value of type int.
_________
_________
string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments. When pos is specified, the search only includes characters at or after position …
_________
_________
string::rfind
http://www.cplusplus.com/reference/string/string/rfind/
Searches the string for the last occurrence of the sequence specified by its arguments. When pos is specified, the search only includes sequences of characters that beg …
_________

*/
//Your code should go here:

