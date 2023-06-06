"""
####  Word Nests  ####

A word nest is created by taking a starting word, and generating a new string by placing the word inside itself. This process is then repeated.
Nesting 3 times with the word "incredible":
___
start  = incredible
first  = incre|incredible|dible
second = increin|incredible|credibledible
third  = increinincr|incredible|ediblecredibledible
_____

The final nest is "increinincrincredibleediblecredibledible" (depth = 3).
Given a starting word and the final word nest, return the depth of the word nest.


[Examples]

___
word_nest("floor", "floor") ➞ 0

word_nest("code", "cocodccococodededeodeede") ➞ 5

word_nest("incredible", "increinincrincredibleediblecredibledible") ➞ 3
_____



[Notes]

N/A


[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python String Methods
https://www.programiz.com/python-programming/methods/string
Python has quite a few methods that string objects can call to perform frequency occurring task (related to string). For example, if you want to capitalize the first le …
_________
_________
Text Sequence Type — str
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways …
_________

"""
#Your code should go here:

