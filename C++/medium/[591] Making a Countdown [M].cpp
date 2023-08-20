/*
####  Making a Countdown  ####

Create a function where given the number n to count down from, and some words str, return a countdown sequence as a string leading up to the words at the end.
Put a full stop after each number and uppercase and add an exclamation mark to the word. See the examples below for clarification!


[Examples]

___
countdown(10, "Blast Off") ➞ "10. 9. 8. 7. 6. 5. 4. 3. 2. 1. BLAST OFF!"

countdown(3, "go") ➞ "3. 2. 1. GO!"

countdown(5, "FIRE") ➞ "5. 4. 3. 2. 1. FIRE!"
_____



[Notes]

___
*) n will be a number greater than 0.
*) str won't already include an exclamation mark.
*) Don't include 0 in the countdown.
___



[formatting] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::transform
http://www.cplusplus.com/reference/algorithm/transform/
Applies an operation sequentially to the elements of one (1) or two (2) ranges and stores the result in the range that begins at result.
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
Convert a String to Upper Case
https://stackoverflow.com/questions/735204/convert-a-string-in-c-to-upper-case
How could one convert a string to upper case. The examples I have found from googling only have to deal with chars.
_________

*/
//Your code should go here:

