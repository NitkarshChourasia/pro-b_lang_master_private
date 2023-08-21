/*
####  Sentence Searcher  ####

Create a function that returns the whole of the first sentence which contains a specific word. Include the full stop at the end of the sentence.


[Examples]

___
string str = "I have a cat. I have a mat. Things are going swell."

sentenceSearcher(str, "have") ➞ "I have a cat."

sentenceSearcher(str, "MAT") ➞ "I have a mat."

sentenceSearcher(str, "things") ➞ "Things are going swell."

sentenceSearcher(str, "flat") ➞ ""
_____



[Notes]

___
*) Sentences will always end with a period.
*) Your function should not be case sensitive.
*) Return an empty string if the word isn't found in the sentence.
___



[loops] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________
_________
std::transform()
https://www.geeksforgeeks.org/transform-c-stl-perform-operation-elements/
Consider the problem of adding contents of two arrays into a third array. It is given that all arrays are of same size.
_________

*/
//Your code should go here:

