/*
####  String Cleaver  ####

Create a function that takes a string (without spaces) and a word array, cleaves the string into words based on the array, and returns the correctly spaced version of the string (a sentence). If a section of the string is encountered that can't be found on the word array, return "Cleaving stalled: Word not found".


[Examples]

___
const words = ["about", "be", "hell", "if", "is", "it", "me", "other", "outer", "people", "the", "to", "up", "where"]


cleave("ifitistobeitisuptome", words) ➞ "if it is to be it is up to me"

cleave("hellisotherpeople", words) ➞ "hell is other people"

cleave("hellisotterpeople", words) ➞ "Cleaving stalled: Word not found"
_____



[Notes]

Words in the words array can appear more than once in the string. The words array is a reference guide, kind of like a dictionary that lists which words are allowed.


[strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________

*/
//Your code should go here:

