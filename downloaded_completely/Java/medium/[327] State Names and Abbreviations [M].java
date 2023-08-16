/*
####  State Names and Abbreviations  ####

Create a function that filters out an array of state names into two categories based on the second parameter.



[Examples]

___
filterStateNames(["Arizona", "CA", "NY", "Nevada"], "abb")
➞ ["CA", "NY"]

filterStateNames(["Arizona", "CA", "NY", "Nevada"], "full")
➞ ["Arizona", "Nevada"]

filterStateNames(["MT", "NJ", "TX", "ID", "IL"], "abb")
➞ ["MT", "NJ", "TX", "ID", "IL"]

filterStateNames(["MT", "NJ", "TX", "ID", "IL"], "full")
➞ []
_____



[Notes]

State abbreviations will always be in uppercase.


[arrays] [formatting] [loops] 



-------------------------------------------------------------------
[Resources]
_________
toCollection() Method
https://www.geeksforgeeks.org/java-stream-collectors-tocollection-in-java/
Used to create a Collection using Collector. It returns a Collector that accumulates the input elements into a new Collection, in the order in which they are passed.
_________
_________
Is there a Util to convert US State Name to State Code. eg. Arizona to AZ?
https://stackoverflow.com/questions/11005751/is-there-a-util-to-convert-us-state-name-to-state-code-eg-arizona-to-az
I need to convert full state name to its official state address code. For example from the String New York, I need to produce NY. Now I could put this all in a hashmap, …
_________
_________
Convert an ArrayList of String to a String array in Java
https://www.geeksforgeeks.org/convert-an-arraylist-of-string-to-a-string-array-in-java/
Given an ArrayList of String, the task is to convert the ArrayList to String array in Java.
_________
_________
filter() Method
https://www.geeksforgeeks.org/stream-filter-java-examples/
Returns a stream consisting of the elements of this stream that match the given predicate. This is an intermediate operation.
_________

*/
//Your code should go here:

