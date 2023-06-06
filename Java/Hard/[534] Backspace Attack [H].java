/*
####  Backspace Attack  ####

Suppose a hash # represents the BACKSPACE key being pressed. Write a function that transforms a string containing # into a string without any #.


[Examples]

___
erase("he##l#hel#llo") ➞ "hello"

erase("major# spar##ks") ➞ "majo spks"

erase("si###t boy") ➞ "t boy"

erase("####") ➞ ""
_____



[Notes]

___
*) In addition to characters, backspaces can also remove whitespaces.
*) If the number of hashes exceeds the previous characters, remove those previous characters entirely (see example #3).
*) If there only exist backspaces, return an empty string (see example #4).
___



[regex] [scope] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Stack (Java Platform SE 7 )
https://docs.oracle.com/javase/7/docs/api/java/util/Stack.html
A more complete and consistent set of LIFO stack operations is provided by the Deque interface and its implementations, which should be used in preference to this cla …
_________
_________
Try and Catch
https://www.w3schools.com/java/java_try_catch.asp
The try statement allows you to define a block of code to be tested for errors while it is being executed. The catch statement allows you to define a block of code to b …
_________

*/
//Your code should go here:

