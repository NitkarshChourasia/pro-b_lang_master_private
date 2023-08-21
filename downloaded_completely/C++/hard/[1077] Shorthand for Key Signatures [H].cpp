/*
####  Shorthand for Key Signatures  ####

Given a string containing a key signature written in shorthand, create a function which replaces the shorthand with its full written name.
___
*) A lowercase letter denotes a minor key.
*) An uppercase letter denotes a major key.
___

See the examples below for a more helpful guide!


[Examples]

___
fullKeyName("Prelude in C") ➞ "Prelude in C major"

fullKeyName("Fugue in c") ➞ "Fugue in C minor"

fullKeyName("Toccata and Fugue in d") ➞ "Toccata and Fugue in D minor"

fullKeyName("Sonata in eb") ➞ "Sonata in Eb minor"
_____



[Notes]

___
*) Write the letter name in uppercase (ignore b and #).
*) Write "major" or "minor" in all lowercase (rather than "Major" or "Minor").
___



[Hint]

The first letter of the term should always be capital, even if it's "b".


[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

