/*
####  Complete the Word  ####

An input string can be completed if additional letters can be added and no letters need to be taken away to match the word. Furthermore, the order of the letters in the input string must be the same as the order of letters in the final word.
Create a function that, given an input string, determines if the word can be completed.


[Examples]

___
canComplete("butl", "beautiful") ➞ true
// We can add "ea" between "b" and "u", and "ifu" between "t" and "l".

canComplete("butlz", "beautiful") ➞ false
// "z" does not exist in the word beautiful.

canComplete("tulb", "beautiful") ➞ false
// Although "t", "u", "l" and "b" all exist in "beautiful", they are incorrectly ordered.

canComplete("bbutl", "beautiful") ➞ false
// Too many "b"s, beautiful has only 1.
_____



[Notes]

Both string input and word will be lowercased.


[loops] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
contains() Method
https://www.guru99.com/string-contains-method-java.html
Check if String contains another substring or not. It returns boolean value so it can use directly inside if statements.
_________
_________
Complete the Word Java Coding Challenge
https://youtu.be/VdNKO67lFVc
Complete the Word Java Coding Challenge
_________

*/
//Your code should go here:

