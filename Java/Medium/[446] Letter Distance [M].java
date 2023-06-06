/*
####  Letter Distance  ####

Given two words, the letter distance is calculated by taking the absolute value of the difference in character codes and summing up the difference.
If one word is longer than another, add the difference in lengths towards the score.
To illustrate:
___
letterDistance("house", "fly") = dist("h", "f") + dist("o", "l") + dist("u", "y") + dist(house.length, fly.length)

= |104 - 102| + |111 - 108| + |117 - 121| + |5 - 3|
= 2 + 3 + 4 + 2
= 11
_____



[Examples]

___
letterDistance("sharp", "sharq") ➞ 1

letterDistance("abcde", "Abcde") ➞ 32

letterDistance("abcde", "bcdef") ➞ 5
_____



[Notes]

___
*) Always start comparing the two strings from their first letter.
*) Excess letters are not counted towards distance.
*) Capital letters are included.
___



[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Math.abs() Method
https://www.geeksforgeeks.org/java-math-abs-method-examples/
Returns the absolute value of a given argument. If the argument is not negative, the argument is returned. If the argument is negative, the negation of the argument is …
_________

*/
//Your code should go here:

