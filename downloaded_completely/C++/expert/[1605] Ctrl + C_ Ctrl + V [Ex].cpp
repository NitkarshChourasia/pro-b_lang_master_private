/*
####  Ctrl + C, Ctrl + V  ####

Given a sentence containing few instances of "Ctrl + C" and "Ctrl + V", return the sentence after those keyboard shortcuts have been applied! Note that:
___
*) In this case, "Ctrl + C" will copy all text behind it.
*) In this case, "Ctrl + V" will do nothing if there is no "Ctrl + C" before it.
*) A "Ctrl + C" which follows another "Ctrl + C" will overwrite what it copies.
___



[Examples]

___
keyboardShortcut("the egg and Ctrl + C Ctrl + V the spoon") ➞ "the egg and the egg and the spoon"

keyboardShortcut("WARNING Ctrl + V Ctrl + C Ctrl + V") ➞ "WARNING WARNING"

keyboardShortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V") ➞ "The The Town The The Town"
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
How to Use the Cut, Copy, and Paste Keyboard Shortcuts in Windows
https://www.digitaltrends.com/computing/windows-keyboard-shortcuts-cut-copy-paste-undo/
Are you tired of having to right-click and search for the simple command you want to be able to do, like cut, copy, and paste? While not super labor-intensive, it can b …
_________

*/
//Your code should go here:

