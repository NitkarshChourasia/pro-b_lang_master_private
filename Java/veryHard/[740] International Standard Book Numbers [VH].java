/*
####  International Standard Book Numbers  ####

The International Standard Book Number (ISBN) is a unique identifying number given to each published book. ISBNs assigned after January 2007 are 13 digits long (ISBN-13), however books with 10-digit ISBNs are still in wide use.
An ISBN-10 is verified this way:
___
isbn10 = "0330301624"
_____

Line up the digits with the numbers 10 to 1:

Multiply each digit with the number below it (the 10th digit in an ISBN can be an X. This last X simply means 10).
Sum up the products:
___
0 + 27 + 24 + 0 + 18 + 0 + 4 + 18 + 4 + 4 = 99
_____

If the sum is divisible by 11, the ISBN-10 is valid.
An ISBN-13 is verified this way:
___
isbn13 = "9780316066525"
_____

Line up the digits with alternating 1s and 3s:

Multiply each digit with the number below it and get the sum:
___
9 + 21 + 8 + 0 + 3 + 3 + 6 + 0 + 6 + 18 + 5 + 6 + 5 = 90
_____

If the sum is divisible by 10, the ISBN-13 is valid.
Create a function that takes a string of numbers (possibly with an X at the end) and...

Convert a valid ISBN-10 to ISBN-13 by tacking 978 to the start, then changing the last digit (the check digit) so that the resulting number passes the ISBN-13 check.


[Examples]

___
isbn13("9780316066525") ➞ "Valid"

isbn13("0330301824") ➞ "Invalid"

isbn13("0316066524") ➞ "9780316066525"
_____



[Notes]

N/A


[algorithms] [loops] [validation] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

