/*
####  Seven Segment Display  ####

Create a function that takes a single Hexadecimal number as an argument and returns the equivalent six-digit binary number to light the display. Consider the six-digit binary number as an incoming input from a serial port. The segment display is a common cathode segment display that means you need to give a logical 1 to light up each segment.



[Examples]

___
toDisplay('1') ➞ 0x06

toDisplay('8') ➞ 0x7F

toDisplay('0') ➞ 0x3F
_____



[Notes]

___
*) The segment display is a common cathode segment display that means you need to give (5v logical 1) to light up each segment.
*) Expect an input from 0-9.
*) LSB starts from a, b, c.
___



[functional_programming] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Working with Seven Segment LED Displays
https://www.jameco.com/Jameco/workshop/techtip/working-with-seven-segment-displays.html
This is s a quick introduction to the basics of using seven segment LED displays with microcontrollers. Be sure to refer to the manufacturer's data sheets for more info …
_________

*/
//Your code should go here:

