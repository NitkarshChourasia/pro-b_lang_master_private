/*
####  No Yelling  ####

Create a function that transforms sentences ending with multiple question marks ? or exclamation marks ! into a sentence only ending with one without changing punctuation in the middle of the sentences.


[Examples]

___
noYelling("What went wrong?????????") ➞ "What went wrong?"

noYelling("Oh my goodness!!!") ➞ "Oh my goodness!"

noYelling("I just!!! can!!! not!!! believe!!! it!!!") ➞ "I just!!! can!!! not!!! believe!!! it!"
// Only change repeating punctuation at the end of the sentence.

noYelling("Oh my goodness!") ➞ "Oh my goodness!"
// Do not change sentences where there exists only one or zero exclamation marks/question marks.

noYelling("I just cannot believe it.") ➞ "I just cannot believe it."
_____



[Notes]

___
*) Only change ending punctuation - keep the exclamation marks or question marks in the middle of the sentence the same (see third example).
*) Don't worry about mixed punctuation (no cases that end in something like ?!??!).
*) Keep sentences that do not have question/exclamation marks the same.
___



[recursion] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::find_last_not_of
http://www.cplusplus.com/reference/string/string/find_last_not_of/
Searches the string for the last character that does not match any of the characters specified in its arguments.
_________
_________
std::string::substr
https://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object.
_________

*/
//Your code should go here:

