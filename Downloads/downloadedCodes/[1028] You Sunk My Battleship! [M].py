"""
####  You Sunk My Battleship!  ####

Remember the game Battleship? Ships are floating in a matrix. You have to fire torpedos at their suspected coordinates, to try and hit them.
Create a function that takes a list of lists (matrix) and a coordinate as a string. If the coordinate contains only water ".", return "splash" and if the coordinate contains a ship "*", return "BOOM".
Instruction text contains two blank spaces between quotation marks; the code/test does not. See examples below.


[Examples]

___
[
  [".", ".", ".", "*", "*"],
  [".", "*", ".", ".", "."],
  [".", "*", ".", ".", "."],
  [".", "*", ".", ".", "."],
  [".", ".", "*", "*", "."],
]

fire(matrix, "A1") ➞ "splash"

fire(matrix, "A4") ➞ "BOOM"

fire(matrix, "D2") ➞ "BOOM"
_____



[Notes]

___
*) The provided matrix is always a square.
*) The provided matrix will not be larger than 5 * 5 ( A1 * E5).
___



[arrays] [games] [language_fundamentals] [validation] 



-------------------------------------------------------------------
[Resources]
_________
find() method
https://www.programiz.com/python-programming/methods/string/find
Returns the index of first occurrence of the substring (if found). If not found, it returns -1.
_________
_________
index() Method
https://www.w3schools.com/python/ref_string_index.asp
Is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)
_________

"""
#Your code should go here:

