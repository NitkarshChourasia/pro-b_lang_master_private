/*
####  Index Filtering  ####

Create a function that takes two inputs: idx (an array of integers) and str (a string). The function should return another string with the letters of str at each index in idx in order.


[Examples]

___
indexFilter([2, 3, 8, 11], "Autumn in New York") ➞ "tune"

indexFilter([0, 1, 5, 7, 4, 2], "Cry me a river") ➞ "creamy"

indexFilter([9, -9, 2, 27, 36, 6, 5, 13, -1, 2, 0, 30, 2], 
  "That's life, I've got you under my skin") ➞ "frank sinatra"
_____



[Notes]

___
*) Indexes may not be in order or may be negative (see example #2 and #3).
*) The output string must always be lowercase, but the input str may not be (see examples).
___



[arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

