/*
####  Three Darts Thrown... How Many Scored?  ####

Having just watched the PDC World Darts Championship, Adam has become inspired to become the next Gerwyn Price and takes to the dartboard.
Create a function convert the text information of what Adam has thrown in his three darts into the number of points scored.
For those familiar to watching darts on TV...
You will see a string with three passages of text in the same format as the bar that comes on the screen when a player is on a checkout.
For those not familiar to a dartbord and/or not familiar to watching darts on TV...
You will see a string with three passages of text separated by a space. Each of the three passages of text shall be in one of the following five formats:


[Format #1]

___
*) The numbers 1 to 20 (inclusive).
*) These represent the single segments of the dartboard.
*) For example: 17 means single 17 which is 1 x 17 = 17.
___



[Format #2]

___
*) The numbers 1 to 20 inclusive with the letter D in front.
*) These represents the double segments of the dartboard.
*) For example: D12 means double 12 which is 2 x 12 = 24.
___



[Format #3]

___
*) The numbers 1 to 20 inclusive with the letter T in front.
*) These represents the treble segments of the dartboard.
*) For example: T9 means treble 9 which is 3 x 9 = 27.
___



[Format #4]

___
*) The number 25 which is the common name for the outer bullseye.
*) This, perhaps unsurprisingly, is worth twenty-five points.
___



[Format #5]

___
*) The word BULL which is the common name for the inner bullseye.
*) This is worth fifty points.
___



[Examples]

___
howManyScored("BULL 10 T1") ➞ 63
// 50 + (1 x 10) + (3 x 1) = 63

howManyScored("D10 T12 15") ➞ 71
// (2 x 10) + (3 x 12) + (1 x 15) = 71

howManyScored("14 25 T8") ➞ 63
// (1 x 14) + 25 + (3 x 8) = 63
_____



[Notes]

___
*) Each passage of text is separated by a space.
*) There will always be three passages of text in the string.
*) Each passage of text shall be in one of the five valid formats mentioned above.
*) i.e. Adam will not go outside the board and score zero with any darts.
___



[loops] [math] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
Operators
https://www.w3schools.com/cpp/cpp_operators.asp
Used to perform operations on variables and values. In the example below, we use the + operator to add together two values.
_________

*/
//Your code should go here:

