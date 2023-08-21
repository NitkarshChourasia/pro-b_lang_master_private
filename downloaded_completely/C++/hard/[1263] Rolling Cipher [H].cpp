/*
####  Rolling Cipher  ####

Write a function that accepts a string and an n and returns a cipher by rolling each character forward (n > 0) or backward (n < 0) n times.
Note: Think of the letters as a connected loop, so rolling a backwards once will yield z, and rolling z forward once will yield a. If you roll 26 times in either direction, you should end up back where you started.


[Examples]

___
rollingCipher("abcd", 1) ➞ "bcde"

rollingCipher("abcd", -1) ➞ "zabc"

rollingCipher("abcd", 3) ➞ "defg"

rollingCipher("abcd", 26) ➞ "abcd"
_____



[Notes]

___
*) All letters are lower cased.
*) No spacing.
*) Each character is rotated the same number of times.
___



[arrays] [cryptography] 



-------------------------------------------------------------------
[Resources]
_________
Rolling Cipher
http://www.thealmightyguru.com/Wiki/index.php?title=Rolling_cipher#:~:text=A%20rolling%20cipher%2C%20also%20called,which%20uses%20a%20rolling%20key.&text=The%20starting%20number%20to%20shift,encrypt%20and%20decrypt%20the%20message.
Is a primitive form of substitution encryption which uses a rolling key. Like the Caesar cipher, each letter is shifted forward along the alphabet, looping back around …
_________

*/
//Your code should go here:

