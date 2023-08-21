/*
####  Pluralize!  ####

Given an array of words in the singular form, return a set of those words in the plural form if they appear more than once in the array.


[Examples]

___
pluralize(["cow", "pig", "cow", "cow"]) ➞ [ "cows", "pig" ]

pluralize(["table", "table", "table"]) ➞ [ "tables" ]

pluralize(["chair", "pencil", "arm"]) ➞ [ "chair", "pencil", "arm" ]
_____



[Notes]

___
*) This is an oversimplification of the English language so no edge cases will appear.
*) Only focus on whether or not to add an s to the ends of words.
*) All tests will be valid.
___



[arrays] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
std::vector::erase
http://www.cplusplus.com/reference/vector/vector/erase/
Removes from the vector either a single element (position) or a range of elements ([first,last)). This effectively reduces the container size by the number of elements …
_________

*/
//Your code should go here:

