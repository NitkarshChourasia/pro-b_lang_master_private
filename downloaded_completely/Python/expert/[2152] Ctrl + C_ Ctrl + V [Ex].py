"""
####  Ctrl + C, Ctrl + V  ####

Given a sentence containing few instances of "Ctrl + C" and "Ctrl + V", return the sentence after those keyboard shortcuts have been applied! Note that:
___
*) In this case, "Ctrl + C" will copy all text behind it.
*) In this case, "Ctrl + V" will do nothing if there is no "Ctrl + C" before it.
*) A "Ctrl + C" which follows another "Ctrl + C" will overwrite what it copies.
___



[Examples]

___
keyboard_shortcut("the egg and Ctrl + C Ctrl + V the spoon") ➞ "the egg and the egg and the spoon"

keyboard_shortcut("WARNING Ctrl + V Ctrl + C Ctrl + V") ➞ "WARNING WARNING"

keyboard_shortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V") ➞ "The The Town The The Town"
_____



[Notes]

___
*) Keyboard shortcut commands will appear like normal words in a sentence but shouldn't be copied themselves (see example #2).
*) Pasting should add a space between words.
___



[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python String startswith() Method
https://www.w3schools.com/python/ref_string_startswith.asp
Check if the string starts with "Hello":
_________

"""
#Your code should go here:

