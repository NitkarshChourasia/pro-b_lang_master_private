"""
####  Difference Cipher  ####

It's time to send and receive secret messages.
Create a single function that takes a string or a list and returns a coded or decoded message.
The first letter of the string, or the first element of the list represents the Character Code of that letter. The next elements are the differences between the characters: e.g. A +3 --> C or z -1 --> y.


[Examples]

___
dif_ciph("Hello") ➞ [72, 29, 7, 0, 3]
# H = 72, the difference between the H and e is 29 (upper- and lowercase).
# The difference between the two l's is obviously 0.

dif_ciph([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]) ➞ "Hi there!"

dif_ciph("Sunshine") ➞ [83, 34, -7, 5, -11, 1, 5, -9]
_____



[Notes]

The input of the function will always be a string or a list with numbers.


[arrays] [cryptography] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
ord() Function
https://www.programiz.com/python-programming/methods/built-in/ord
Returns an integer representing the Unicode character.
_________
_________
type() Function
https://www.programiz.com/python-programming/methods/built-in/type
In this tutorial, we will learn about the Python type() function with the help fo examples. The type() function either returns the type of the object or returns a new t …
_________
_________
join() String Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
chr() Method
https://www.programiz.com/python-programming/methods/built-in/chr
Returns a character (a string) from an integer (represents unicode code point of the character).
_________

"""
#Your code should go here:

