/*
####  License Plate  ####

Travelling through Europe one needs to pay attention to how the license plate in the given country is displayed. When crossing the border you need to park on the shoulder, unscrew the plate, re-group the characters according to the local regulations, attach it back and proceed with the journey.
Create a solution that can format the dmv number into a plate number with correct grouping. The function input consists of string s and group length n. The output has to be upper case characters and digits. The new groups are made from right to left and connected by -. The original order of the dmv number is preserved.


[Examples]

___
licensePlate("5F3Z-2e-9-w", 4) ➞ "5F3Z-2E9W"

licensePlate("2-5g-3-J", 2) ➞ "2-5G-3J"

licensePlate("2-4A0r7-4k", 3) ➞ "24-A0R-74K"

licensePlate("nlj-206-fv", 3) ➞ "NL-J20-6FV"
_____



[Notes]

___
*) A recursive version of this challenge can be found in here.
___



[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String toUpperCase() Method
https://www.tutorialspoint.com/java/java_string_touppercase.htm
This method has two variants. The first variant converts all of the characters in this String to upper case using the rules of the given Locale.
_________
_________
String charAt() Method
https://www.w3schools.com/java/ref_string_charat.asp
Returns the character at the specified index in a string. The index of the first character is 0, the second character is 1, and so on.
_________

*/
//Your code should go here:

