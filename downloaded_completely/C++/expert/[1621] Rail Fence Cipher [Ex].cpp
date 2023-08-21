/*
####  Rail Fence Cipher  ####

In Rail Fence Cipher encoding is done by placing each character successively in a diagonal along with a set of rails.
Create a function that takes two arguments; a string and the number of rails, and returns the encoded message.
___
message = "WEAREDISCOVEREDFLEEATONCE"
rails = 3

railFenceCipher(message, rails) ➞ "WECRLTEERDSOEEFEAOCAIVDEN"
_____

In the above example, the given message to be decomposed in 3 rails:
___
W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C
    A       I       V       D       E       N
_____

Starting from the upper line, the encoded message will be:
___
"WECRLTEERDSOEEFEAOCAIVDEN"
_____



[Examples]

___
railFenceCipher("WEAREDISCOVEREDFLEEATONCE", 3) ➞ "WECRLTEERDSOEEFEAOCAIVDEN"

railFenceCipher("EDABITISAMAZING", 4) ➞ "EIIDTSZNAIAAGBM"

railFenceCipher("WEWILLALLDIEONEDAY", 3) ➞ "WLLOAEILLDENDYWAIE"
_____



[Notes]

Rails will be >=2


[algorithms] [cryptography] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Rail Fence Cipher
https://crypto.interactive-maths.com/rail-fence-cipher.html
Is a transposition cipher that uses a table that looks a bit like an old rail fence viewed from above.
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________
_________
std::string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments. When pos is specified, the search only includes characters at or after positio …
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

