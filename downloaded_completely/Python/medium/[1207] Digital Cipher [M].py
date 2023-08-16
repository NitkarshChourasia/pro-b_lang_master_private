"""
####  Digital Cipher  ####

In Digital Cipher, encoding is done by the simple addition of numbers in the key and the corresponding characters on a string input.
Create a function that takes two arguments; a positive integer and a string and returns an encoded list of integers as message.
Assign a unique number to each letter of the alphabet.
___
 a  b  c  d  e  f  g  h  i  j  k  l  m
 1  2  3  4  5  6  7  8  9  10 11 12 13
 n  o  p  q  r  s  t  u  v  w  x  y  z
 14 15 16 17 18 19 20 21 22 23 24 25 26
_____

There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "scout"
key = 1939

digital_cipher(message, key) ➞ [20, 12, 18, 30, 21]
_____

Write the corresponding number against each character:
___
 s  c  o  u  t
19  3 15 21 20
_____

Add to each obtained digit consecutive digits from the key:
___
   s  c  o  u  t
  19  3 15 21 20
 + 1  9  3  9  1
 ---------------
  20 12 18 30 21
_____

See the below example for a better understanding:
___
message = "masterpiece"
key = 1939

digital_cipher(message, key) ➞ [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]

   m  a  s  t  e  r  p  i  e  c  e
  13  1 19 20  5 18 16  9  5  3  5
+  1  9  3  9  1  9  3  9  1  9  3
  --------------------------------
  14 10 22 29  6 27 19 18  6  12 8
_____



[Examples]

___
digital_cipher("scout", 1939) ➞ [20, 12, 18, 30, 21]

digital_cipher("mubashir", 1990) ➞ [14, 30, 11, 1, 20, 17, 18, 18]

digital_cipher("edabit", 100) ➞ [6, 4, 1, 3, 9, 20]
_____



[Notes]

Liked this challenge ? Let's decode your encrypted version here!!!


[algorithms] [cryptography] [logic] 



-------------------------------------------------------------------
[Resources]
_________
String to Int() and Int to String
https://careerkarma.com/blog/python-string-to-int/#:~:text=To%20convert%20a%20string%20to,as%20an%20int%20%2C%20or%20integer.
To convert a string to integer in Python, use the int() function. This function takes two parameters: the initial string and the optional base to represent the data. Us …
_________
_________
Caesar Cipher
https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
Is a simple and easy method of encryption technique. It is simple type of substitution cipher. Each letter of plain text is replaced by a letter with some fixed numbe …
_________
_________
map() Method
https://www.geeksforgeeks.org/python-map-function/
Returns a map object (which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple, etc).
_________
_________
str() Method
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object.
_________
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
How to Find the Sum of Two Lists
https://www.kite.com/python/answers/how-to-find-the-sum-of-two-lists-in-python
Adding two lists results in a new list where each element is the sum of the elements in the corresponding positions of the two lists. For example, [1, 2, 3] + [4, 5, 6] …
_________
_________
Populating a Dictionary Using for Loops
https://stackoverflow.com/questions/30280856/populating-a-dictionary-using-for-loops-python
Discussion on how to create a dictionary using for loops.
_________

"""
#Your code should go here:

