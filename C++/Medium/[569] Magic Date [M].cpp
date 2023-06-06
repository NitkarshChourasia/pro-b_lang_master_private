/*
####  Magic Date  ####

You are to read each part of the date into its own integer type variable. The year should be a 4 digit number. You can assume the user enters a correct date formatted d m yyyy (no error checking required).
Determine whether the entered date is a magic date. Here are the rules for a magic date:
___
*) mm * dd is a 1-digit number that matches the last digit of yyyy or
*) mm * dd is a 2-digit number that matches the last 2 digits of yyyy or
*) mm * dd is a 3-digit number that matches the last 3 digits of yyyy
___

The program should then display true if the date is magic, or false if it is not.


[Examples]

___
Magic("1 1 2011") ➞ true

Magic("4 1 2001") ➞ false

Magic("5 2 2010") ➞ true

Magic("9 2 2011") ➞ false
_____



[Notes]

N/A


[dates] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::to_string
https://www.geeksforgeeks.org/stdto_string-in-cpp/
Convert numerical value to string.
_________
_________
std::stoi(string s)
https://www.techiedelight.com/convert-string-to-int-cpp/
use this to convert string to integer
_________

*/
//Your code should go here:

