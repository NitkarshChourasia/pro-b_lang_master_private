/*
####  Connecting Words  ####

Write a function that connects each previous word to the next word by the shared letters. Return the resulting string (removing duplicate characters in the overlap) and the minimum number of shared letters across all pairs of strings.


[Examples]

___
join(["oven", "envier", "erase", "serious"]) ➞ ["ovenvieraserious", "2"]

join(["move", "over", "very"]) ➞ ["movery", "3"]

join(["to", "ops", "psy", "syllable"]) ➞ ["topsyllable", "1"]

// "to" and "ops" share "o" (1)
// "ops" and "psy" share "ps" (2)
// "psy" and "syllable" share "sy" (2)
// the minimum overlap is 1

join(["aaa", "bbb", "ccc", "ddd"]) ➞ ["aaabbbcccddd", "0"]
_____



[Notes]

More specifically, look at the overlap between the previous words ending letters and the next word's beginning letters.


[higher_order_functions] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Concatenate Strings
https://beginnersbook.com/2017/10/java-string-join-method/
In Java 8 we have a new Method join() in the Java String class. Java String join() method concatenates the given Strings and returns the concatenated String. Java 8 als …
_________
_________
indexOf() Method
https://www.geeksforgeeks.org/java-string-indexof/
There are four variants of indexOf() method. This article depicts about all of them, as follows: 1.int indexOf() : This method returns the index within this string of …
_________

*/
//Your code should go here:

