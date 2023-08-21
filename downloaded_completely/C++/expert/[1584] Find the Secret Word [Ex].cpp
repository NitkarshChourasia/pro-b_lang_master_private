/*
####  Find the Secret Word  ####

This string, "sadbpstcrdvaefikkgoenqrt" has a five letter word embedded within it.
Here's a clue on how to find it:

Given the str and len of the secret word, improvise a function that finds the secret word.


[Examples]

___
secretWord("sadbpstcrdvaefikkgoenqrt", 5) ➞ "brake"
// sa(dbp)st(crd)(vae)f(ikk)g(oen)qrt
// The values of the triplets in parentheses are 22, 25, 28, 31, 34.
// An arithmetic series with difference of 3.

secretWord("aheiayd", 3) ➞ "hey"
// (a[he)i](ayd)
// The triplets with the secret letters can overlap.
// ahe=14, hei=22, ayd=30; a series with a difference of 8.
_____



[Notes]

N/A


[algorithms] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

