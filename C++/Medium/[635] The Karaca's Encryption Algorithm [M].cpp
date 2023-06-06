/*
####  The Karaca's Encryption Algorithm  ####

Make a function that encrypts a given input with these steps:
Input: "apple"
Step 1: Reverse the input: "elppa"
Step 2: Replace all vowels using the following chart:
___
a => 0
e => 1
i => 2
o => 2
u => 3

// "1lpp0"
_____

Step 3: Add "aca" to the end of the word: "1lpp0aca"
Output: "1lpp0aca"


[Examples]

___
encrypt("banana") ➞ "0n0n0baca"

encrypt("karaca") ➞ "0c0r0kaca"

encrypt("burak") ➞ "k0r3baca"

encrypt("alpaca") ➞ "0c0pl0aca"
_____



[Notes]

All inputs are strings, no uppercases and all output must be strings.


[algorithms] [cryptography] [formatting] [regex] 



-------------------------------------------------------------------
[Resources]
_________
How to Reverse a String in C++
https://www.educative.io/edpresso/how-to-reverse-a-string-in-cpp
Reversing a string, or completely flipping a string means flipping changing the order of the characters in it, such that it reads backward. The illustration below shows …
_________
_________
How to replace all occurrences of a character in string?
https://stackoverflow.com/questions/2896600/how-to-replace-all-occurrences-of-a-character-in-string
What is the effective way to replace all occurrences of a character with another character in std::string?
_________
_________
std::map::operator[]
http://www.cplusplus.com/reference/map/map/operator[]/
If k matches the key of an element in the container, the function returns a reference to its mapped value. If k does not match the key of any element in the container, …
_________

*/
//Your code should go here:

