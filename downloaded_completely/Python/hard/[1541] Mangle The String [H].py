"""
####  Mangle The String  ####

Create a function that takes a string and replaces every letter with the letter following it in the alphabet ("c" becomes "d", "z" becomes "a", "b" becomes "c", etc). Then capitalize every vowel (a, e, i, o, u) and return the new modified string.


[Examples]

___
mangle("Fun times!") ➞ "GvO Ujnft!"

mangle("The quick brown fox.") ➞ "UIf rvjdl cspxO gpy."

mangle("Omega") ➞ "Pnfhb"
_____



[Notes]

___
*) If a letter is already uppercase, return it as uppercase (regardless of being a vowel).
*) "y" is not considered a vowel.
___



[formatting] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
str.translate(table)
https://docs.python.org/3/library/stdtypes.html#str.translate
Return a copy of the string in which each character has been mapped through the given translation table.
_________
_________
static str.maketrans(x[, y[, z]])
https://docs.python.org/3/library/stdtypes.html#str.maketrans
This static method returns a translation table usable for str.translate().
_________
_________
Common String Operations
https://docs.python.org/3.4/library/string.html
The constants defined in this module are: string.ascii_letters The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not …
_________
_________
Regular Expression Operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________
_________
class str(object='')
https://docs.python.org/3/library/functions.html#func-str
Return a str version of object.
_________

"""
#Your code should go here:

