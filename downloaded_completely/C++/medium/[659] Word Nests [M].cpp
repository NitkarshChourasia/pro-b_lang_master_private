/*
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
wordNest("floor", "floor") ➞ 0

wordNest("code", "cocodccococodededeodeede") ➞ 5

wordNest("incredible", "increinincrincredibleediblecredibledible") ➞ 3
_____



[Notes]

N/A


[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
string::length
http://www.cplusplus.com/reference/string/string/length/
Returns the length of the string, in terms of bytes. This is the number of actual bytes that conform the contents of the string, which is not necessarily equal to its …
_________

*/
//Your code should go here:

