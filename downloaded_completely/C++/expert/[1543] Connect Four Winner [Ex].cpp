/*
####  Connect Four Winner  ####

Connect Four is a two-player connection board game, in which the players choose a color and then take turns dropping colored discs into a seven-column, six-row vertically suspended grid.
The game has two players: yellow and red while columns are named from "A" to "G". The first player who connects four items of the same color is the winner.

Create a function that takes an array of player positions showing the order of the pieces which are dropped in columns. Function should return "Yellow", "Red" or "Draw" accordingly.


[Examples]

___
connectFourWinner([
  "A_Red",
  "B_Yellow",
  "A_Red",
  "B_Yellow",
  "A_Red",
  "B_Yellow",
  "G_Red",
  "B_Yellow"
]) ➞ "Yellow"

// Yellow has 4 conescutive discs in column B
_____

___
connectFourWinner([
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
Connect Four
https://en.wikipedia.org/wiki/Connect_Four
A two-player connection board game, in which the players choose a color and then take turns dropping colored discs into a seven-column, six-row vertically suspended gri …
_________
_________
std::string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments. When pos is specified, the search only includes characters at or after positio …
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i. …
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________

*/
//Your code should go here:

