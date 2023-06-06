"""
####  Mubashir Cipher  ####

In Mubashir Cipher, encoding is done by simply replacing paired letters from the provided key.
Create a function that takes a string containing the message to be encoded with a fixed given 2D list of letters key.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
key = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'],
    ['s', 'v'], ['h', 'x'], ['i', 'z'], ['r', 'y'],
    ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]

message = "edabit is amazing !"

mubashir_cipher(message) ➞ "uqkgzf zv kckizlb !"
_____

Step 1: Search letter in the given key and replace it with paired letter:
___
e = u
d = q
a = k
b = g
.
.
.
g = b
_____

Step 2: Keep all characters (including spaces) other than letters in their original positions:
___
"uqkgzf zv kckizlb !"
_____

See the below examples for a better understanding:


[Examples]

___
mubashir_cipher("mubashir is not amazing") ➞ "cegkvxzy zv ljf kckizlb"

mubashir_cipher("%$ &%") ➞ "%$ &%"

mubashir_cipher("evgeny sh is amazing") ➞ "usbulr vx zv kckizlb"
_____



[Notes]

N/A


[algorithms] [cryptography] [logic] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
Used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other programming languages …
_________
_________
reduce() Method
https://www.geeksforgeeks.org/reduce-in-python/
Used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” mo …
_________
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
String islower() Method
https://www.programiz.com/python-programming/methods/string/islower
Returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.
_________
_________
String maketrans() Method
https://www.w3schools.com/python/ref_string_maketrans.asp
Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character.
_________
_________
String translate() Method
https://www.programiz.com/python-programming/methods/string/translate#:~:text=Join-,Python%20String%20translate(),as%20per%20the%20mapping%20table.
Returns a string where each character is mapped to its corresponding character in the translation table.
_________

"""
#Your code should go here:

