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
replaceFirst() Method
https://www.tutorialspoint.com/java/java_string_replacefirst.htm
Replaces the first substring of this string that matches the given regular expression with the given replacement.
_________

*/
//Your code should go here:

