/*
####  No Yelling  ####

Create a function that transforms sentences ending with multiple question marks ? or exclamation marks ! into a sentence only ending with one without changing punctuation in the middle of the sentences.


[Examples]

___
NoYelling("What went wrong?????????") ➞ "What went wrong?"

NoYelling("Oh my goodness!!!") ➞ "Oh my goodness!"

NoYelling("I just!!! can!!! not!!! believe!!! it!!!") ➞ "I just!!! can!!! not!!! believe!!! it!"
// Only change repeating punctuation at the end of the sentence.

NoYelling("Oh my goodness!") ➞ "Oh my goodness!"
// Do not change sentences where there exists only one or zero exclamation marks/question marks.

NoYelling("I just cannot believe it.") ➞ "I just cannot believe it."
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
RegExr: Learn, Build, & Test RegEx
https://regexr.com/
An online tool to learn, build, & test Regular Expressions (RegEx / RegExp).
_________
_________
Trimming Characters from the End of a String
https://docs.microsoft.com/en-us/dotnet/standard/base-types/trimming
If you are parsing a sentence into individual words, you might end up with words that have blank spaces (also called white spaces) on either end of the word. In this si …
_________
_________
String.EndsWith Method
https://docs.microsoft.com/en-us/dotnet/api/system.string.endswith?view=netframework-4.8
Determines whether the end of this string instance matches a specified string.
_________

*/
//Your code should go here:

