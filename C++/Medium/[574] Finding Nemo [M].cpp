/*
####  Finding Nemo  ####

You're given a string of words. You need to find the word "Nemo", and return a string like this: "I found Nemo at [the order of the word you find Nemo]!".
If you can't find Nemo, return "I can't find Nemo :(".


[Examples]

___
findNemo("I am finding Nemo !") ➞ "I found Nemo at 4!"

findNemo("Nemo is me") ➞ "I found Nemo at 1!"

findNemo("I Nemo am") ➞ "I found Nemo at 2!"
_____



[Notes]

___
*) ! , ? . are always separated from the last word.
*) Nemo will always look like Nemo, and not NeMo or other capital variations.
*) Nemo's, or anything that says Nemo with something behind it, doesn't count as Finding Nemo.
*) If there are multiple Nemo's in the sentence, only return the first one.
___



[arrays] [formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string
http://www.cplusplus.com/reference/string/string/
Strings are objects that represent sequences of characters.
_________
_________
Concatenate an Integer to a String Object
https://www.techiedelight.com/concatenate-integer-string-object-cpp/
The most commonly used approach to concatenate an integer to a string object in C++ is to call the std::to_string function which can return the string representation of …
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object.
_________

*/
//Your code should go here:

