"""
####  Binary to ASCII Conversion  ####

Create a function that takes a string of 1's and 0's (binary) as an argument and return the equivalent decoded ASCII text. Characters can be in the range of "00000000" to "11111111", which means every eight digits of binary input represents a single character.
___
*) a = 01100001
*) b = 01100010
*) c = 01100011
___

If you were to combine these characters into the string "abc", the corresponding binary would be 011000010110001001100011. Use the resources tab for more info on how to approach this.


[Examples]

___
binary_conversion("011001010110010001100001011000100110100101110100") ➞ "edabit"

binary_conversion("001100010011001000110011") ➞ "123"

binary_conversion("010010000110010101101100011011000110111100111111") ➞ "Hello?"
_____



[Notes]

If you are given an empty string as input, you must also return an empty string. Otherwise, the input will always be a valid binary string.


[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python Program to Find ASCII Value of Character
https://www.programiz.com/python-programming/examples/ascii-character
In this program, you'll learn to find the ASCII value of a character and display it.
_________
_________
How do you convert 8-bit binary numbers into their ASCII characters?
https://stackoverflow.com/questions/9509502/in-python-how-do-you-convert-8-bit-binary-numbers-into-their-ascii-characters/9509521
I'm attempting to extract a hidden message from the blue pixels of a picture such that the if the blue value is even, it represents a 0 in the binary string, and if the …
_________
_________
chr() Function
https://www.w3schools.com/python/ref_func_chr.asp
Returns the character that represents the specified unicode.
_________
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string.
_________
_________
Split String Into Array Every N Characters
https://www.codegrepper.com/code-examples/python/split+string+into+array+every+n+characters+python
Python answers related to split a string into array every n characters.
_________

"""
#Your code should go here:

