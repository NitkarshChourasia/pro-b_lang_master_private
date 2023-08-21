/*
####  Message from Space  ####

You have received an encrypted message from space. Your task is to decrypt the message with the following simple rules:
___
*) Message string will consist of capital letters, numbers, and brackets only.
*) When there's a block of code inside the brackets, such as [10AB], it means you need to repeat the letters AB for 10 times.
*) Message can be embedded in multiple layers of blocks.
*) Final decrypted message will only consist of capital letters.
___

Create a function that takes encrypted message str and returns the decrypted message.


[Examples]

___
spaceMessage("ABCD") ➞ "ABCD"

spaceMessage("AB[3CD]") ➞ "ABCDCDCD"
// "AB" = "AB"
// "[3CD]" = "CDCDCD"

spaceMessage("IF[2E]LG[5O]D") ➞ "IFEELGOOOOOD"
_____



[Notes]

N/A


[loops] [recursion] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string.
_________
_________
std::string::insert
http://www.cplusplus.com/reference/string/string/insert/
Inserts additional characters into the string right before the character indicated by pos (or p).
_________

*/
//Your code should go here:

