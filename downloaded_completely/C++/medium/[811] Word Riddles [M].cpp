/*
####  Word Riddles  ####

What does the word LFAND represent? It represents the word Finland, because F is in LAND!
Create a function which replicates this to create brand new original word riddles! For the purposes of this challenge, take the string of letters before the word "in", and insert it into the 2nd letter position of the word formed after the word "in".
See the examples below for further clarity :)


[Examples]

___
makeWordRiddle("Finland") ➞ "LFAND"

makeWordRiddle("dinner") ➞ "NDER"

makeWordRiddle("tkinter") ➞ "TTKER"

makeWordRiddle("STRINGS") ➞ "GSTRS"
_____



[Notes]

___
*) All words given will contain only one occurence of "in" (so no occurences of the words Insulin, Infinity, etc).
*) There will be no examples of Interest, Pin, or Ping, etc... as there is no clear way to insert the strings into one another.
*) Return in all CAPS.
___



[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

