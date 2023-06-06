"""
####  Rolling Cipher  ####

Write a function that accepts a string and an n and returns a cipher by rolling each character forward (n > 0) or backward (n < 0) n times.
Note: Think of the letters as a connected loop, so rolling a backwards once will yield z, and rolling z forward once will yield a. If you roll 26 times in either direction, you should end up back where you started.


[Examples]

___
rolling_cipher("abcd", 1) ➞ "bcde"

rolling_cipher("abcd", -1) ➞ "zabc"

rolling_cipher("abcd", 3) ➞ "defg"

rolling_cipher("abcd", 26) ➞ "abcd"
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
ascii_lowercase Method
https://www.geeksforgeeks.org/python-string-ascii_lowercase/
A pre-initialized string used as string constant. In Python, string ascii_lowercase will give the lowercase letters ‘abcdefghijklmnopqrstuvwxyz’.
_________
_________
join() Method
https://www.programiz.com/python-programming/methods/string/join
A string method which returns a string concatenated with the elements of an iterable.
_________
_________
find() Method
https://www.programiz.com/python-programming/methods/string/find
Returns the index of first occurrence of the substring (if found). If not found, it returns -1.
_________
_________
Python For Loop
https://www.programiz.com/python-programming/for-loop
In this article, you'll learn to iterate over a sequence of elements using the different variations of for loop.
_________

"""
#Your code should go here:

