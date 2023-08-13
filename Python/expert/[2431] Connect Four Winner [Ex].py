"""
####  Connect Four Winner  ####

Connect Four is a two-player connection board game, in which the players choose a color and then take turns dropping colored discs into a seven-column, six-row vertically suspended grid.
The game has two players: yellow and red while columns are named from "A" to "G". The first player who connects four items of the same color is the winner.

Create a function that takes a list of player positions showing the order of the pieces which are dropped in columns. Function should return "Yellow", "Red" or "Draw" accordingly.


[Examples]

___
connect_four_winner([
  "A_Red",
  "B_Yellow",
  "A_Red",
  "B_Yellow",
  "A_Red",
  "B_Yellow",
  "G_Red",
  "B_Yellow"
]) ➞ "Yellow"

# Yellow has 4 conescutive discs in column B
_____

___
connect_four_winner([
  "A_Red",
  "B_Yellow",
  "A_Red",
  "E_Yellow",
  "F_Red",
  "G_Yellow",
  "A_Red",
  "G_Yellow"
]) ➞ "Draw"
_____



[Notes]

N/A


[algorithms] [games] [logic] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
numpy.rot90
https://numpy.org/doc/stable/reference/generated/numpy.rot90.html?highlight=rot90#numpy.rot90
Rotate an array by 90 degrees in the plane specified by axes. Rotation direction is from the first towards the second axis.
_________
_________
join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
map() Method
https://www.geeksforgeeks.org/python-map-function/
Returns a map object (which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple, etc).
_________
_________
str() Method
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object.
_________
_________
Connect Four
https://en.wikipedia.org/wiki/Connect_Four
A two-player connection board game, in which the players choose a color and then take turns dropping colored discs into a seven-column, six-row vertically suspended gri …
_________
_________
numpy.diagonal
https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html
If a is 2-D, returns the diagonal of a with the given offset, i.e., the collection of elements of the form a[i, i+offset]. If a has more than two dimensions, then the a …
_________

"""
#Your code should go here:

