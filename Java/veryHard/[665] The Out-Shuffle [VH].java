/*
####  The Out-Shuffle  ####

An out-shuffle, also known as an out faro shuffle or a perfect shuffle, is a controlled method for shuffling playing cards. It is performed by splitting the deck into two equal halves and interleaving them together perfectly, with the condition that the top card of the deck remains in place.
Using an array to represent a deck of cards, an out-shuffle looks like:
___
[1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]
// Card 1 remains in the first position.
_____

If we repeat the process, the deck eventually returns to original order.
Shuffle 1:
___
[1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]
_____

Shuffle 2:
___
[1, 5, 2, 6, 3, 7, 4, 8] ➞ [1, 3, 5, 7, 2, 4, 6, 8]
_____

Shuffle 3:
___
[1, 3, 5, 7, 2, 4, 6, 8] ➞ [1, 2, 3, 4, 5, 6, 7, 8]
// Back where we started.
_____

Write a function that takes a positive even integer representing the number of the cards in a deck, and returns the number of out-shuffles required to return the deck to its original order.


[Examples]

___
shuffleCount(8) ➞ 3

shuffleCount(14) ➞ 12

shuffleCount(52) ➞ 8
_____



[Notes]

___
*) The number of cards is always even and greater than one. Thus, the smallest possible deck size is two.
*) A recursive version of this challenge can be found via this link.
___



[logic] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Java.util.Arrays.equals() Method
https://www.geeksforgeeks.org/java-util-arrays-equals-java-examples/
Today we are going to discuss the simplest way to check whether two arrays are equal or not. Two arrays are considered equal if both arrays contain the same number of e …
_________

*/
//Your code should go here:

