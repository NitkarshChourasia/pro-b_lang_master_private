/*
####  Broken Bridge II  ####

Create a function that returns the count of all bridges in a two-dimensional grid.
Bridge B should be counted if:
___
*) It connects from one end of the grid to the one opposite to it.
*) It is unobstructed.
___



[Example]

___
"#########/#       #/#   #   #/#   #   #/#### ####/#   #   #/#   #   #/#       #/#########"
_____

In this case the number 4 is returned because, when unraveled, the string reveals four bridges that meet the requirements listed above as shown:
___
#########/
#       #/
#   #   #/
#   #   #/
#### ####/
#   #   #/
#   #   #/
#       #/
#########
_____



[Notes]

___
*) Slashes / act as separators.
*) Intersecting bridges can still count, as shown.
*) Vertical bridges count as long as the requirements are met.
___



[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

