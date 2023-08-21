/*
####  Sentence Searcher II  ####

Create a function that returns the sentence that contains the word at index n. Remember to include the full stop at the end.


[Worked Example]

___
string txt = "I have a dog. I have a log. There is no stopping me now."

sentenceSearcher(txt, 7) ➞ "I have a log."
// The word at index 7 is "log".
// The full sentence that contains the word at index 7 is "I have a log."
// Return the sentence.
_____



[Examples]

___
sentenceSearcher(txt, 2) ➞ "I have a dog."

sentenceSearcher(txt, 4) ➞ "I have a log."

sentenceSearcher(txt, -1) ➞ "There is no stopping me now."
// The index at -1 is the last word.
// The last word is "now".
_____



[Notes]

___
*) All sentences will end with a full stop.
*) You need to also account for negative indexes.
___



[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string.
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________

*/
//Your code should go here:

