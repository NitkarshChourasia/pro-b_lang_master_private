/*
####  Recursion: Flatten the Curves  ####

The nesting of arrays can be viewed indirectly as curves and barriers of the real data embedded in arrays, thus, defeats the very purpose of directly accessing them thru indexes and slices. Write a recursive function to flatten those curves (i.e. level, iron, compress, raze, topple) and expose those data as a single array other than an array of arrays.


[Examples]

___
flatten(["Tesh", 121317, ["Love", "of", ["my", ["life", ["and", "my", ["world"], "entirely"]]]]])
➞ ["Tesh", 121317, "Love", "of", "my", "life", "and", "my", "world", "entirely"]

flatten([[[[[["direction"], [372], ["one"], [[[[[["Era"]]]], "Sruth", 3337]]], "First"]]]])
➞ ["direction", 372, "one", "Era", "Sruth", 3337, "First"]

flatten([[4666], [5394], [466], [[["Saskia", [[[[["DXTD"]], "Lexi"]]]]]]])
➞ [4666, 5394, 466, "Saskia", "DXTD", "Lexi"]

flatten([[696], ["friend"], ["power"], [[[["Marcus"]]]], ["philus"]])
➞ [696, "friend", "power", "Marcus", "philus"]

flatten([[["deep"], [[["ocean"]]], [["Marge"]], ["rase", 876]]])
➞ ["deep", "ocean", "Marge", "rase", 876]
_____



[Notes]

___
*) Every array has at least one element.
*) You are expected to solve this challenge via a recursive approach.
*) You can check on the Resources tab for more details about recursion in Java.
*) A similar version of this challenge can be found via this link.
*) A collection of challenges that deals on recursion can be found via this link.
___



[arrays] [objects] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Recursion
https://www.geeksforgeeks.org/recursion-in-java/
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called as recursive function. Using recursive …
_________
_________
Determining If an Object Is an Array in Java
https://www.tutorialspoint.com/determining-if-an-object-is-an-array-in-java
In order to determine if an object is an Object is an array in Java, we use the isArray() and getClass() methods.The isArray() method checks whether the passed ...
_________
_________
Recursion
https://introcs.cs.princeton.edu/java/23recursion/
The idea of calling one function from another immediately suggests the possibility of a function calling itself. The function-call mechanism in Java supports this possi …
_________
_________
Recursion
https://www.baeldung.com/java-recursion
Learn the fundamental concepts of recursion in Java with examples.
_________

*/
//Your code should go here:

