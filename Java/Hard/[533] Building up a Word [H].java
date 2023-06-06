/*
####  Building up a Word  ####

You are given an input list of strings, ordered by ascending length.
Write a function that returns True if, for each pair of consecutive strings, the second string can be formed from the first by adding a single letter either at the beginning or end.


[Examples]

___
canBuild(["a", "at", "ate", "late", "plate", "plates"]) ➞ True

canBuild(["a", "at", "ate", "late", "plate", "plater", "platter"]) ➞ False
# "platter" is formed by adding "t" in the middle of "plater"

canBuild(["it", "bit", "bite", "biters"]) ➞ False
# "biters" is formed by adding two letters - we can only add one

canBuild(["mean", "meany"]) ➞ True
_____



[Notes]

___
*) Return False if a word is NOT formed by adding only one letter.
*) Return False if the letter is added to the middle of the previous word.
*) Letters in tests will all be lower case.
___



[arrays] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Java String contains()
https://www.w3schools.com/java/ref_string_contains.asp
Checks whether a string contains a sequence of characters.
_________

*/
//Your code should go here:

