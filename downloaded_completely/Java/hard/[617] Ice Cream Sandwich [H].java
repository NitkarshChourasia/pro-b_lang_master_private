/*
####  Ice Cream Sandwich  ####

An ice cream sandwich is a string that is formed by two identical ends and a different middle.

___
"AABBBAA"

"3&&3"

"yyyyymmmmmmmmyyyyy"

"hhhhhhhhmhhhhhhhh"
_____

Notice how left and right ends of the sandwich are identical in both length and in repeating character. The middle section is distinctly different.

___
"BBBBB"
// You can't have just plain icecream.

"AAACCCAA"
// You can't have unequal sandwich ends.

"AACDCAA"
// You can't have more than one filling.

"A"
// You can't have fewer than 3 characters.
_____

Write a function that returns true if a string is an ice cream sandwich and false otherwise.


[Examples]

___
isIcecreamSandwich("CDC") ➞ true

isIcecreamSandwich("AAABB") ➞ false

isIcecreamSandwich("AA") ➞ false
_____



[Notes]

An ice cream sandwich must have a minimum length of 3 characters, and at least two of these characters must be distinct (you can't only have the filling!).


[language_fundamentals] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
java.util.HashMap.containsKey() Method
https://www.geeksforgeeks.org/hashmap-containskey-method-in-java/?ref=rp
Is used to check whether a particular key is being mapped into the HashMap or not. It takes the key element as a parameter and returns True if that element is mapped in …
_________

*/
//Your code should go here:

