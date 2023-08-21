/*
####  Word Buckets  ####

Write a function that divides a phrase into word buckets, with each bucket containing n or fewer characters. Only include full words inside each bucket.


[Examples]

___
bucketize("she sells sea shells by the sea", 10)
➞ ["she sells", "sea shells", "by the sea"]

bucketize("the mouse jumped over the cheese", 7)
➞ ["the", "mouse", "jumped", "over", "the", "cheese"]

bucketize("fairy dust coated the air", 20)
➞ ["fairy dust coated", "the air"]

bucketize("a b c d e", 2)
➞ ["a", "b", "c", "d", "e"]
_____



[Notes]

___
*) Spaces count as one character.
*) Trim beginning and end spaces for each word bucket (see final example).
*) If buckets are too small to hold a single word, return an empty array: []
*) The final goal isn't to return just the words with a length equal (or lower) to the given n, but to return the entire given phrase bucketized (if possible). So, for the specific case of "by" the only word with a proper length, the phrase can't be bucketized, and the returned array has to be empty.
___



[control_flow] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String Length
https://www.w3schools.com/cpp/cpp_strings_length.asp
To get the length of a string, use the length() function. Tip: You might see some C++ programs that use the size() function to get the length of a string. This is just …
_________
_________
std::find, std::find_if, std::find_if_not
https://en.cppreference.com/w/cpp/algorithm/find
Returns an iterator to the first element in the range [first, last) that satisfies specific criteria.
_________
_________
std::basic_stringstream
https://en.cppreference.com/w/cpp/io/basic_stringstream
Implements input and output operations on string-based streams. It effectively stores an instance of std::basic_string and performs the input and output operations on it.
_________

*/
//Your code should go here:

