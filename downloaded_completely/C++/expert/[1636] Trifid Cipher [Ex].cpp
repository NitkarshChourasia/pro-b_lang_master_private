/*
####  Trifid Cipher  ####

In Trifid Cipher, encoding is done by using a table to fractionate each plaintext letter into a trigram, mixes the constituents of the trigrams, and then applies the table in reverse to turn these mixed trigrams into ciphertext letters.
Create a function that takes three arguments; a 27 letter key, a break period, and a string containing the message to be encoded.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
key = "EPSDUCVWYM+ZLKXNBTFGORIJHAQ"
period = 5
message = "DEFENDTHEEASTWALLOFTHECASTLE+"

trifidCipher(key, period, message) ➞ "SUEFECPHSEGYYJIXIMFOFOCEJLBSP"
_____

Step 1: Divide the key in the form of three squares:
___
Square 1   Square 2   Square 3

  1 2 3      1 2 3      1 2 3
1 E P S    1 M + Z    1 F G O
2 D U C    2 L K X    2 R I J
3 V W Y    3 N B T    3 H A Q
_____

Step 2: Locate the plaintext letters in the squares above, D is in square 1, row 2, column 1, so D becomes 121. Similarly, E becomes 111 and so on.
Write down the numbers corresponding to each letter vertically:
___
D E F E N D T H E E A S T W A L L O F T H E C A S T L E +
1 1 3 1 2 1 2 3 1 1 3 1 2 1 3 2 2 3 3 2 3 1 1 3 1 2 2 1 2
2 1 1 1 3 2 3 3 1 1 3 1 3 3 3 2 2 1 1 3 3 1 2 3 1 3 2 1 1
1 1 1 1 1 1 3 1 1 1 2 3 3 2 2 1 1 3 1 3 1 1 3 2 3 3 1 1 2
_____

Step 3: At the moment, it is still a substitution cipher and fairly easy to break. Now, you have to use period, which is usually a number between 5 - 20.
___
D E F E N  D T H E E  A S T W A  L L O F T  H E C A S  T L E +
1 1 3 1 2  1 2 3 1 1  3 1 2 1 3  2 2 3 3 2  3 1 1 3 1  2 2 1 2
2 1 1 1 3  2 3 3 1 1  3 1 3 3 3  2 2 1 1 3  3 1 2 3 1  3 2 1 1 
1 1 1 1 1  1 3 1 1 1  2 3 3 2 2  1 1 3 1 3  1 1 3 2 3  3 1 1 2
_____

Step 4: Group the numbers and read off the numbers in each group horizontally, and do the substitution back to the letters using the original key-squares.
___
113 122 111 311 111  123 112 331 113 111  312 133 133 323 322
S   U   E   F   E    C   P   H   S   E    G   Y   Y   J   I

223 322 211 311 313  311 313 123 111 323   221 232 113 112
X   I   M   F   O    F   O   C   E   J     L   B   S   P
_____

Step 5: Return the final result:
___
eMessage = "SUEFECPHSEGYYJIXIMFOFOCEJLBSP"
_____

See the below examples for a better understanding:


[Examples]

___
key="EPSDUCVWYM+ZLKXNBTFGORIJHAQ"

trifidCipher(key, 5, "DEFENDTHEEASTWALLOFTHECASTLE+") ➞ "SUEFECPHSEGYYJIXIMFOFOCEJLBSP"

trifidCipher(key, 15, "MUBASHIR") ➞ "+OHTW+XD"

trifidCipher(key, 6, "ABCDEFG") ➞ "RSAMXEG"
_____



[Notes]

___
*) The key, data, and output will all contain exclusively valid uppercase letters and a plus sign(+) as the 27th letter.
*) Keys will always be a complete 27-letter alphabet with no repeats, and periods will always be positive integers.
___



[algorithms] [cryptography] [logic] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Trifid Cipher
https://en.wikipedia.org/wiki/Trifid_cipher
A classical cipher invented by Félix Delastelle and described in 1902.[1] Extending the principles of Delastelle's earlier bifid cipher, it combines the techniques of f …
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Generate substring Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the ob …
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Get character in string Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a ch …
_________
_________
std::stoi
http://www.cplusplus.com/reference/string/stoi/
Convert string to integer Parses str interpreting its content as an integral number of the specified base, which is returned as an int value. If idx is not a null poin …
_________

*/
//Your code should go here:

