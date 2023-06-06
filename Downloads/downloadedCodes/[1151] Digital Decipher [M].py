"""
####  Digital Decipher  ####

In Digital Decipher, decoding is done by the simple subtraction of numbers in the key and the corresponding characters on a given list. You may want to solve this challenge before proceeding further.
Create a function that takes two arguments; a positive integer and a list of integers and returns a decoded message as string.
Assign a unique number to each letter of the alphabet.
___
 a  b  c  d  e  f  g  h  i  j  k  l  m
 1  2  3  4  5  6  7  8  9  10 11 12 13
 n  o  p  q  r  s  t  u  v  w  x  y  z
 14 15 16 17 18 19 20 21 22 23 24 25 26
_____

There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
eMessage = [20, 12, 18, 30, 21]
key = 1939

digital_decipher(eMessage, key) ➞ "scout"
_____

Subtract each key digit from eMessage consecutive digits:
___
  20 12 18 30 21
-  1  9  3  9  1
 ---------------
  19  3 15 21 20
_____

Write the corresponding number against each character:
___
 s  c  o  u  t
19  3 15 21 20
_____

See the below example for a better understanding:
___
eMessage = [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
key = 1939

digital_decipher(eMessage, key) ➞ "masterpiece"

  14 10 22 29  6 27 19 18  6  12 8
-  1  9  3  9  1  9  3  9  1  9  3
  --------------------------------
  13  1 19 20  5 18 16  9  5  3  5
   m  a  s  t  e  r  p  i  e  c  e
_____



[Examples]

___
digital_decipher([20, 12, 18, 30, 21], 1939) ➞ "scout"

digital_decipher([14, 30, 11, 1, 20, 17, 18, 18], 1990) ➞ "mubashir"

digital_decipher([6, 4, 1, 3, 9, 20], 100) ➞ "edabit"
_____



[Notes]

N/A


[algorithms] [cryptography] [logic] 



-------------------------------------------------------------------
[Resources]
_________
String to Int() and Int to String
https://careerkarma.com/blog/python-string-to-int/#:~:text=To%20convert%20a%20string%20to,as%20an%20int%20%2C%20or%20integer.
To convert a string to integer in Python, use the int() function. This function takes two parameters: the initial string and the optional base to represent the data. Us …
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
itertools.cycle
https://docs.python.org/3/library/itertools.html#itertools.cycle
Make an iterator returning elements from the iterable and saving a copy of each. When the iterable is exhausted, return elements from the saved copy. Repeats indefinitely.
_________

"""
#Your code should go here:

