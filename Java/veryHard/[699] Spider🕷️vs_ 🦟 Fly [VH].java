/*
####  Spider🕷️vs. 🦟 Fly  ####

A spider web is defined by rings numbered from 0-4 from the center and radials labeled clock-wise from the top as A-H.
Create a function that takes the coordinates of spider and fly and returns the shortest path for the spider to get to the fly.
It's worth noting that the shortest path should be calculated "geometrically", not by counting the number of points that path goes through. We could arrange that:
___
*) Angle between every pair of radials is the same (45 degrees).
*) Distance between every pair of rings is always the same (let's say "x").
___


In the above picture, spider coordinates are "H3" and fly coordinates are "E2". The spider will follow the shortest path "H3-H2-H1-A0-E1-E2" to reach the fly.


[Examples]

___
spiderVsFly("H3", "E2") ➞ "H3-H2-H1-A0-E1-E2"

spiderVsFly("A4", "B2") ➞ "A4-A3-A2-B2"

spiderVsFly("A4", "C2") ➞ "A4-A3-A2-B2-C2"
_____



[Notes]

The center of the web will always be A0.


[algorithms] [logic] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
If ... Else
https://www.w3schools.com/java/java_conditions.asp
Java supports the usual logical conditions from mathematics. You can use these conditions to perform different actions for different decisions. Java has the following c …
_________
_________
While Loops
https://www.w3schools.com/java/java_while_loop.asp
Loops can execute a block of code as long as a specified condition is reached. Loops are handy because they save time, reduce errors, and they make code more readable.
_________
_________
String charAt() Method
https://www.w3schools.com/java/ref_string_charat.asp#:~:text=The%20charAt()%20method%20returns,is%201%2C%20and%20so%20on.
Returns the character at the specified index in a string. The index of the first character is 0, the second character is 1, and so on.
_________
_________
Java Strings
https://www.w3schools.com/java/java_strings.asp
Strings are used for storing text. A String variable contains a collection of characters surrounded by double quotes:
_________

*/
//Your code should go here:

