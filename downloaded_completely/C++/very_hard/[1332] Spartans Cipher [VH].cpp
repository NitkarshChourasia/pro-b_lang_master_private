/*
####  Spartans Cipher  ####

In Spartans Cipher, encoding is done by writing the text horizontally, across the strap in the plaintext word of a message. In ancient times, Spartans and Greeks invented an interesting way of encryption called Scytale.
The ancient Greeks, and the Spartans in particular, are said to have used this cipher to communicate during military campaigns.
Create a function that takes two arguments, a number of slides nSlide and a string message, and returns the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "Mubashir Scytale Code"
nSlide = 6

spartansCipher(message, nSlide) ➞ "Ms t euhSaC biclo aryed"
_____

Step 1: Imagine this Scytale:

Step 2: You can write the given message on a 6 slide Scytale like this:
___
| M | u | b | a |
| s | h | i | r |
|   | S | c | y |
| t | a | l | e |
|   | C | o | d |
| e |   |   |   |
_____

Step 3: Encode the message column-wise:
___
"Ms t euhSaC biclo aryed "
_____

Step 4: Trim all spaces at the end and return the final encoded message:
___
"Ms t euhSaC biclo aryed"
_____

See the below examples for a better understanding:


[Examples]

___
spartansCipher("Mubashir Scytale Code", 6) ➞ "Ms t euhSaC biclo aryed"

spartansCipher("Matt and Edabit are amazing", 8) ➞ "M  baai aaEirmn tndteag tda  z"

spartansCipher("", 99) ➞ ""
_____



[Notes]

N/A


[algorithms] [cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Scytale
https://en.wikipedia.org/wiki/Scytale
A tool used to perform a transposition cipher, consisting of a cylinder with a strip of parchment wound around it on which is written a message. The ancient Greeks, and …
_________
_________
Ceil and Floor Functions in C++
https://www.geeksforgeeks.org/ceil-floor-functions-cpp/
In mathematics and computer science, the floor and ceiling functions map a real number to the greatest preceding or the least succeeding integer, respectively. floor(x …
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________

*/
//Your code should go here:

