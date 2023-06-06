/*
####  Difference Cipher  ####

It's time to send and receive secret messages.
Create two functions that take a string and an array and returns a coded or decoded message.
The first letter of the string, or the first element of the array represents the Character Code of that letter. The next elements are the differences between the characters: e.g. A +3 --> C or z -1 --> y.


[Examples]

___
encrypt("Hello") ➞ [72, 29, 7, 0, 3]
// H = 72, the difference between the H and e is 29 (upper- and lowercase).
// The difference between the two l's is obviously 0.

decrypt([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]) ➞ "Hi there!"

encrypt("Sunshine") ➞ [83, 34, -7, 5, -11, 1, 5, -9]
_____



[Notes]

___
*) The input of the encrypt function will always be a string.
*) The input of the decrypt function will always be an array with numbers.
___



[arrays] [cryptography] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Ascii Table
http://www.asciitable.com/
Complete tables including hex, octal, html, decimal conversions.
_________
_________
Find ASCII Value of a Character
https://www.programiz.com/java-programming/examples/ascii-value-character
In this program, you'll learn to find and display the ASCII value of a character in Java. This is done using type-casting and normal variable assignment operations.
_________
_________
Stream mapToInt() Function
https://www.geeksforgeeks.org/stream-maptoint-java-examples/
Returns an IntStream consisting of the results of applying the given function to the elements of this stream. Stream mapToInt(ToIntFunction mapper) is an intermediate …
_________
_________
StringBuilder
https://docs.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html
The principal operations on a StringBuilder are the append and insert methods, which are overloaded so as to accept data of any type. Each effectively converts a giv …
_________

*/
//Your code should go here:

