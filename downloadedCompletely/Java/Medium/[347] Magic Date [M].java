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
endsWith() Method
https://beginnersbook.com/2013/12/java-string-endswith-method-example/
Checks whether the String ends with a specified suffix. This method returns a boolean value true or false. If the specified suffix is found at the end of the string the …
_________
_________
How do you get the numerical value from a string of digits?
https://stackoverflow.com/questions/28773871/how-do-you-get-the-numerical-value-from-a-string-of-digits
I need to add certain parts of the numerical string. for example like. 036000291453 I want to add the numbers in the odd numbered position so like 0+6+0+2+1+5 and h …
_________
_________
split() Method
https://www.geeksforgeeks.org/split-string-java-examples/
Splits a given string around matches of the given regular expression. Learn more with different examples.
_________

*/
//Your code should go here:

