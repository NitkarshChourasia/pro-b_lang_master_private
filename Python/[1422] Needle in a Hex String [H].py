"""
####  Needle in a Hex String  ####

Find the index of a string within a hex encoded string.
You will be given a string which needs to be found in another string which has previously been translated into hex. You will need to return the first index of the needle within the hex encoded string.


[Examples]

___
first_index("68 65 6c 6c 6f 20 77 6f 72 6c 64", "world") ➞ 6

first_index("47 6f 6f 64 62 79 65 20 77 6f 72 6c 64", "world") ➞ 8

first_index("42 6f 72 65 64 20 77 6f 72 6c 64", "Bored") ➞ 0
_____



[Notes]

N/A


[formatting] [functional_programming] 



-------------------------------------------------------------------
[Resources]
_________
Hexadecimal
https://en.wikipedia.org/wiki/Hexadecimal
In mathematics and computing, hexadecimal (also base 16, or hex) is a positional numeral system with a radix, or base, of 16. It uses sixteen distinct symbols, most oft …
_________
_________
How do I convert hex to decimal in Python?
https://stackoverflow.com/questions/9210525/how-do-i-convert-hex-to-decimal-in-python
If by "hex data" you mean a string of the form s = "6a48f82d8e828ce82b82" you can use i = int(s, 16) to convert it to an integer and str(i) to convert it to a decima …
_________
_________
How to Convert a String From Hex to ASCII
https://www.kite.com/python/answers/how-to-convert-a-string-from-hex-to-ascii-in-python
Converting a hexadecimal string to an ASCII string decodes the hexadecimal base-16 encoding into ASCII encodings assigned to each character. For example, the hexadecima …
_________
_________
How can I find the first occurrence of a sub-string in a python string?
https://stackoverflow.com/questions/3221891/how-can-i-find-the-first-occurrence-of-a-sub-string-in-a-python-string
Using index() and find() functions to return the first instance of a sub-string in a string in Python.
_________

"""
#Your code should go here:

