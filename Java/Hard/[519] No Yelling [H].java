/*
####  No Yelling  ####

Create a function that transforms sentences ending with multiple question marks ? or exclamation marks ! into a sentence only ending with one without changing punctuation in the middle of the sentences.


[Examples]

___
noYelling("What went wrong?????????") ➞ "What went wrong?"

noYelling("Oh my goodness!!!") ➞ "Oh my goodness!"

noYelling("I just!!! can!!! not!!! believe!!! it!!!") ➞ "I just!!! can!!! not!!! believe!!! it!"
// Only change repeating punctuation at the end of the sentence.

noYelling("Oh my goodness!") ➞ "Oh my goodness!"
// Do not change sentences where there exists only one or zero exclamation marks/question marks.

noYelling("I just cannot believe it.") ➞ "I just cannot believe it."
_____



[Notes]

___
*) Only change ending punctuation - keep the exclamation marks or question marks in the middle of the sentence the same (see third example).
*) Don't worry about mixed punctuation (no cases that end in something like ?!??!).
*) Keep sentences that do not have question/exclamation marks the same.
___



[recursion] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.geeksforgeeks.org/split-string-java-examples/
Splits a given string around matches of the given regular expression. Learn more with different examples.
_________
_________
Class Pattern
https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html
A regular expression, specified as a string, must first be compiled into an instance of this class. The resulting pattern can then be used to create a Matcher object th …
_________
_________
No Yelling Java Coding Challenge
https://www.youtube.com/watch?v=enithnBBK6E&t=75s
No Yelling In today’s challenge, we are tasked with writing a method that transforms a phrase ending with multiple questions marks, or exclamation marks, int...
_________

*/
//Your code should go here:

