"""
####  Poker Hand Ranking  ####

In this challenge, you have to establish which kind of Poker combination is present in a deck of five cards. Every card is a string containing the card value (with the upper-case initial for face-cards) and the lower-case initial for suits, as in the examples below:
___
"Ah" ➞ Ace of hearts
"Ks" ➞ King of spades
"3d" ➞ Three of diamonds
"Qc" ➞ Queen of clubs
_____

There are 10 different combinations. Here's the list, in decreasing order of importance:

Given a list hand containing five strings being the cards, implement a function that returns a string with the name of the highest combination obtained, accordingly to the table above.


[Examples]

___
poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]) ➞ "Royal Flush"

poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) ➞ "High Card"

poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) ➞ "Four of a Kind"
_____



[Notes]

___
*) For the purposes of this challenge, please consider Aces as high only.
___



[conditions] [data_structures] [games] 



-------------------------------------------------------------------
[Resources]
_________
Poker Hand Rankings
https://www.cardplayer.com/rules-of-poker/hand-rankings
Ranking poker hands.
_________
_________
Python String Methods
https://www.programiz.com/python-programming/methods/string
This page contains all String methods and built-in functions you can use in Python.
_________

"""
#Your code should go here:

