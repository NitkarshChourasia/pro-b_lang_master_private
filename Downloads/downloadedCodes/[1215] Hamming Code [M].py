"""
####  Hamming Code  ####

The Hamming Code is used to correct errors in data transmissions. Create a function that takes a string containing the message and returns an encoded message using hamming code.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
hamming_code("hey") ➞
"000111111000111000000000000111111000000111000111000111111111111000000111"
_____

Step 1: Convert every character to its ASCII value:
___
h, e, y = 104, 101, 121
_____

Step 2: Convert ASCII values to 8-bit binary:
___
104, 101, 121 = 01101000, 01100101, 01111001
_____

Step 3: Triple every bit:
___
01101000, 01100101, 01111001 =

000111111000111000000000, 000111111000000111000111, 000111111111111000000111
_____

Step 4: Concatenate the result:
___
"000111111000111000000000000111111000000111000111000111111111111000000111"
_____

See the below examples for a better understanding:


[Examples]

___
hamming_code("hey") ➞
"000111111000111000000000000111111000000111000111000111111111111000000111"

hamming_code("mubashir") ➞
"000111111000111111000111000111111111000111000111000111111000000000111000000111111000000000000111000111111111000000111111000111111000111000000000000111111000111000000111000111111111000000111000"

hamming_code("matt") ➞
"000111111000111111000111000111111000000000000111000111111111000111000000000111111111000111000000"
_____



[Notes]

N/A


[cryptography] [logic] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
bin() Method
https://www.programiz.com/python-programming/methods/built-in/bin
Converts and returns the binary equivalent string of a given integer. If the parameter isn't an integer, it has to implement __index__() method to return an integer.
_________
_________
ord() Method
https://www.programiz.com/python-programming/methods/built-in/ord
Returns an integer representing the Unicode character.
_________
_________
String zfill() Method
https://www.w3schools.com/python/ref_string_zfill.asp
Adds zeros (0) at the beginning of the string, until it reaches the specified length.
_________

"""
#Your code should go here:

