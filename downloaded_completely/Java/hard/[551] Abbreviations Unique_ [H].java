/*
####  Abbreviations Unique?  ####

You are given two inputs:

Write a function that returns true if each abbreviation uniquely identifies a word, and false otherwise.


[Examples]

___
uniquely(["ho", "h", "ha"], ["house", "hope", "happy"]) ➞ false
// "ho" and "h" are ambiguous and can identify either "house" or "hope"

uniquely(["x", "l", "t"], ["xavier", "loves", "tesh"]) ➞ true

uniquely(["s", "t", "v"], ["stamina", "television", "vindaloo"]) ➞ true

uniquely(["bi", "ba", "bat"], ["big", "bard", "battery"]) ➞ false

uniquely(["mo", "ma", "me"], ["moment", "many", "mean"]) ➞ true
_____



[Notes]

Abbreviations will be a substring from [0, n] from the original string.


[higher_order_functions] [strings] 



-------------------------------------------------------------------
[Resources]
_________
startsWith() Method
https://www.geeksforgeeks.org/java-lang-string-startswith-java/
There are two variants of startswith() method.This article depicts about all of them, as follows: 1. String startsWith() : This method tests if a string starts with the …
_________

*/
//Your code should go here:

