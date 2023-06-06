/*
####  Western Showdown  ####

Wild Roger is participating in a Western Showdown, meaning he has to draw (pull out and shoot) his gun faster than his opponent in a gun standoff.
Given two strings,p1 and p2, return which person drew their gun the fastest. If both are drawn at the same time, return "tie".


[Examples]

___
showdown(
  "   Bang!        ",
  "        Bang!   "
) ➞ "p1"

// p1 draws his gun sooner than p2

showdown(
  "               Bang! ",
  "             Bang!   "
) ➞ "p2"

showdown(
  "     Bang!   ",
  "     Bang!   "
) ➞ "tie"
_____



[Notes]

Both strings are the same length.


[conditions] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
string::find
https://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments. When pos is specified, the search only includes characters at or after positio …
_________

*/
//Your code should go here:

