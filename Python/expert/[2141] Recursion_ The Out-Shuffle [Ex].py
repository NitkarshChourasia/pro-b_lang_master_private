"""
####  Recursion: The Out-Shuffle  ####

An out-shuffle, also known as an out faro shuffle or a perfect shuffle, is a controlled method for shuffling playing cards. It is performed by splitting the deck into two equal halves and interleaving them together perfectly, with the condition that the top card of the deck remains in place.
Using an array to represent a deck of cards, an out-shuffle looks like:
___
[1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]
// Card 1 remains in the first position.
_____

If we repeat the process, the deck eventually returns to original order:
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
shuffle_count(8) ➞ 3

shuffle_count(14) ➞ 12

shuffle_count(52) ➞ 8
_____



[Notes]

___
*) The number of cards is always even and greater than one. Thus, the smallest possible deck size is two.
*) An iterative version of this challenge can be found here.
___



[logic] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Operators
https://www.programiz.com/python-programming/operators
In this tutorial, you'll learn everything about different types of operators in Python, their syntax and how to use them with examples.
_________
_________
Faro Shuffle
https://en.wikipedia.org/wiki/Faro_shuffle
Is a method of shuffling playing cards, in which half of the deck is held in each hand with the thumbs inward, then cards are released by the thumbs so that they fall t …
_________
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________

"""
#Your code should go here:

