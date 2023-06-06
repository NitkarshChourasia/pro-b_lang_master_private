/*
####  Designing Rugs  ####

Write a function that accepts the width and height (m, n) and an optional proc s and generates an array with m elements. Each element is a string consisting of either:
___
*) The default character (hash #) repeating n times (if null is given).
*) The character passed in through the proc repeating n times.
___



[Examples]

___
makeRug(2, 1, "tct") ➞ [
  "tct",
  "tct"
]

makeRug(3, 5, null) ➞ [
  "#####",
  "#####",
  "#####"
]

makeRug(3, 5, "$")  ➞ [
  "$$$$$",
  "$$$$$",
  "$$$$$"
]

makeRug(2, 6, "A")  ➞ [
  "AAAAAA",
  "AAAAAA"
]
_____



[Notes]

The use of Optional container object is required for this challenge.


[arrays] [language_fundamentals] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Optional
https://www.baeldung.com/java-optional
In this tutorial, we're going to show the Optional class that was introduced in Java 8. The purpose of the class is to provide a type-level solution for representing op …
_________

*/
//Your code should go here:

