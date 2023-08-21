/*
####  First Before Second Letter  ####

You are given three inputs: a string, one letter, and a second letter.
Write a function that returns true if every instance of the first letter occurs before every instance of the second letter.


[Examples]

___
firstBeforeSecond("a rabbit jumps joyfully", 'a', 'j') ➞ true
// every instance of "a" occurs before every instance of "j"

firstBeforeSecond("knaves knew about waterfalls", 'k', 'w') ➞  true

firstBeforeSecond("happy birthday", 'a', 'y') ➞ false
// the "a" in "birthday" occurs after the "y" in "happy"

firstBeforeSecond("precarious kangaroos", 'k', 'a') ➞ false
_____



[Notes]

___
*) All strings will be in lower case.
*) All strings will contain the first and second letters at least once.
___



[strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
string::find_last_of
https://www.cplusplus.com/reference/string/string/find_last_of/
Searches the string for the last character that matches any of the characters specified in its arguments.
_________
_________
string::find
https://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments.
_________

*/
//Your code should go here:

