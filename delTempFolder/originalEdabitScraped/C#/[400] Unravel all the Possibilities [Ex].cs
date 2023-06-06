/*
####  Unravel all the Possibilities  ####

Write a function that takes in a string and returns all possible combinations. Return the final result in alphabetical order as a string[].


[Examples]

___
Unravel("a[b|c]") ➞ { "ab", "ac" }

Unravel("a[b|c]de[f|g]") ➞ { "abdef", "acdef", "abdeg", "acdeg" }

Unravel("a[b]c[d]") ➞ { "abcd" }

Unravel("a[b|c|d|e]f") ➞ { "abf", "acf", "adf", "aef" }

Unravel("apple [pear|grape]") ➞ { "apple grape", "apple pear" }
_____



[Notes]

Think of each element in every block (e.g. [a|b|c]) as a fork in the road.


[logic] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Regular Expression Tester & Debugger
https://regex101.com/
With highlighting for PHP, Python, Golang and JavaScript.
_________

*/
//Your code should go here:

