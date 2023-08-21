/*
####  Shared vs. Unique Letters  ####

Create a function that takes in two words as input and returns an array of three elements, in the following order:

Each element should have unique letters, and have each letter be alphabetically sorted.


[Examples]

___
letters("sharp", "soap") ➞ ["aps", "hr", "o"]

letters("board", "bored") ➞ ["bdor", "a", "e"]

letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]

letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
// Even with multiple matching letters (e.g. 3 f's), there should 
// only exist a single "f" in your first element.

letters("match", "ham") ➞ ["ahm", "ct", ""]
// "ham" does not contain any letters that are not found already 
// in "match".
_____



[Notes]

___
*) Both words will be in lower case.
*) You do not have to worry about punctuation, all words only have letters from [a-z].
*) If an element contains no letters, return an empty string (see last example).
___



[arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
std::set_difference
https://en.cppreference.com/w/cpp/algorithm/set_difference
Gives those elements that are in set 1 but not set 2.
_________
_________
std::set_intersection
https://en.cppreference.com/w/cpp/algorithm/set_intersection
Gives those elements that are in both sets.
_________

*/
//Your code should go here:

