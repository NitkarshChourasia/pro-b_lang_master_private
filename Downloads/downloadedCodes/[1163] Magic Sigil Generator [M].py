"""
####  Magic Sigil Generator  ####

A magic sigil is a glyph which represents a desire one wishes to manifest in their lives. There are many ways to create a sigil, but the most common is to write out a specific desire (e.g. "I HAVE WONDERFUL FRIENDS WHO LOVE ME"), remove all vowels, remove any duplicate letters (keeping the last occurence), and then design a glyph from what remains.
Using the sentence above as an example, we would remove duplicate letters:
___
AUFRINDSWHLOVME
_____

And then remove all vowels, leaving us with:
___
FRNDSWHLVM
_____

Create a function that takes a string and removes its vowels and duplicate letters. The returned string should not contain any spaces and be in uppercase.


[Examples]

___
sigilize("i am healthy") ➞ "MLTHY"

sigilize("I FOUND MY SOULMATE") ➞ "FNDYSLMT"

sigilize("I have a job I enjoy and it pays well") ➞ "HVBJNDTPYSWL"
_____



[Notes]

___
*) For duplicate letters the last one is kept.
*) When performing actual sigil magic, you must make your sigils manually.
*) Check the Resources tab for more info on sigils if you're interested in the concept.
___



[formatting] [loops] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
rindex() Method
https://www.w3schools.com/python/ref_string_rindex.asp
It is same as rfind method. It is used to find the index of the last occured repeated element in a string or list.
_________
_________
sorted() Method
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
set() Method
https://www.geeksforgeeks.org/python-set-method/
Used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set.
_________
_________
String upper() Method
https://www.w3schools.com/python/ref_string_upper.asp
Returns a string where all characters are in upper case. Symbols and Numbers are ignored.
_________
_________
join() Method
https://www.geeksforgeeks.org/join-function-python/
Returns a string in which the elements of sequence have been joined by str separator.
_________
_________
Sigil Magic: How to Manifest Your Desires
https://houseofintuitionla.com/blogs/news/sigil-magic-how-to-manifest-your-desires
Sigils are probably one of the most common kinds of magic we all see in the modern world, but no one seems to notice. Sigil magic is the art of using symbols and imager …
_________

"""
#Your code should go here:

