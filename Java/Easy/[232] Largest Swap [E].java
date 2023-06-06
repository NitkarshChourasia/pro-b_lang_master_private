/*
####  Largest Swap  ####

Write a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.
To illustrate:
___
largestSwap(27) ➞ false

largestSwap(43) ➞ true
_____

If 27 is our input, we should return false because swapping the digits gives us 72, and 72 > 27. On the other hand, swapping 43 gives us 34, and 43 > 34.


[Examples]

___
largestSwap(14) ➞ false

largestSwap(53) ➞ true

largestSwap(99) ➞ true
_____



[Notes]

Numbers with two identical digits (third example) should yield true (you can't do better).


[logic] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Convert int to String
https://www.javatpoint.com/java-int-to-string
We can convert int to String in java using String.valueOf() and Integer.toString() methods. Alternatively, we can use String.format() method, string concatenation opera …
_________
_________
Convert String to int
https://mkyong.com/java/java-convert-string-to-int/
In Java, you can use Integer.parseInt() to convert a String to int.
_________
_________
How to swap digits in Java?
https://stackoverflow.com/questions/30740126/how-to-swap-digits-in-java
I am trying to practice java over the summer and i'm stuck on this problem. I need to swap the 2 letters in a integer in java. For example in my main method I make a me …
_________

*/
//Your code should go here:

