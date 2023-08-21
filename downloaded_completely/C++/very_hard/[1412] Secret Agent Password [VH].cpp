/*
####  Secret Agent Password  ####

Mubashir is going on a secret mission. He needs your help but you have to learn how to encode a secret password to communicate safely with other agents. Create a function that takes an argument message and returns the encoded password.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
secretPassword("mubashirh") ➞ "hsajsi13u2"
_____

Step 1: Message length should be of nine characters containing only lowercase letters from 'a' to 'z'. If the argument doesn't meet this requirement you must return "BANG! BANG! BANG!" (Remember, there are no second chances in the spy world!)
Step 2: Divide the string into three equal parts of three characters each:
___
1 - mub
2 - ash
3 - irh
_____

Step 3: Convert the first and third letter to the corresponding number, according to the English alphabets (ex. a = 1, b = 2, c = 3 ... z = 26, etc).
___
mub = 13u2
_____

Step 4: Reverse the fourth, fifth, and sixth letters:
___
ash = hsa
_____

Step 5: Replace seventh, eighth, and ninth letter with next letter (z will be substituted with a).
___
irh = jsi
_____

Step 6: Return the string in the following order: "Part_2+Part_3+Part_1"
___
"hsajsi13u2"
_____

See the below examples for a better understanding:


[Examples]

___
secretPassword("mubashirh") ➞ "hsajsi13u2"

secretPassword("mattedabi") ➞ "detbcj13a20"

secretPassword("HeLen-eda") ➞ "BANG! BANG! BANG!"
// Length is not equal to 9
// Contains characters other than lower alphabets
_____



[Notes]

N/A


[algorithms] [cryptography] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String Concatenation
https://www.w3schools.com/cpp/cpp_strings_concat.asp
The + operator can be used between strings to add them together to make a new string. This is called concatenation.
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
std::string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments. When pos is specified, the search only includes characters at or after positio …
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________
_________
std::string::length
http://www.cplusplus.com/reference/string/string/length/
Returns the length of the string, in terms of bytes. This is the number of actual bytes that conform the contents of the string, which is not necessarily equal to its …
_________
_________
std::string::insert
http://www.cplusplus.com/reference/string/string/insert/
Inserts additional characters into the string right before the character indicated by pos (or p).
_________

*/
//Your code should go here:

