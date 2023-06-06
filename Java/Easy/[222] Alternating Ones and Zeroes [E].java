/*
####  Alternating Ones and Zeroes  ####

Write a function that returns true if the binary string can be rearranged to form a string of alternating 0s and 1s.


[Examples]

___
canAlternate("0001111") ➞ true
// Can make: "1010101"

canAlternate("01001") ➞ true
// Can make: "01010"

canAlternate("010001") ➞ false

canAlternate("1111") ➞ false
_____



[Notes]

___
*) No substring of the output may contain more than one consecutive repeating character (e.g. 00 or 11 are not allowed).
*) Return false if a string only contains 0s or only contains 1s.
___



[logic] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
countMatches Medthod
https://commons.apache.org/proper/commons-lang/apidocs/org/apache/commons/lang3/StringUtils.html#countMatches-java.lang.CharSequence-char-
Counts how many times the char appears in the given string.
_________
_________
Check if it is possible to rearrange a binary string with alternate 0s and 1s
https://www.geeksforgeeks.org/check-is-it-possible-to-rearrange-a-binary-with-alternate-0s-and-1s/
Given a binary string of length at-least two. We need to check if it is possible to rearrange a binary string such that there alternate 0’s and 1’s. If possible then ou …
_________

*/
//Your code should go here:

