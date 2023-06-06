/*
####  N-Length Letter Groups  ####

Write a function that returns an array of strings populated from the slices of n-length characters of the given word (a slice after another while n-length applies onto the word).


[Examples]

___
collect("intercontinentalisationalism", 6)
➞ ["ationa", "interc", "ntalis", "ontine"]

collect("strengths", 3)
➞ ["eng", "str", "ths"]

collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15)
➞ ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"]
_____



[Notes]

___
*) Ensure that the resulting array is lexicographically ordered.
*) Return an empty array if the given string is less than n.
*) Try to solve this challenge using Java Streams API in lieu of custom loops.
*) A recursive version of this challenge can be found via this link.
___



[arrays] [sorting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Getting Substring
https://beginnersbook.com/2013/12/java-string-substring-method-example/
Getting the Substring may help to extract the n-sized parts of the String.
_________

*/
//Your code should go here:

