"""
####  The Primiera  ####

Primiera (from the french word prime, "prize") is a combination of cards of Scopa, a popular Italian card game.
For establishing the value of the Primiera, a separate point scale is used for selecting the best cards in the player's deck, in each of the four suits and totaling those four cards point values. A Primiera requires at least one card for each suit, otherwise, it can't be calculated.
This is the Primiera points scale:
___
*) 7 is worth 21 points.
*) 6 is worth 18 points.
*) Ace is worth 16 points.
*) Cards from 2 to 5 are worth 10 points plus the card value.
*) Face cards (Jack, Queen and King) are worth 10 points.
___

Create a function that takes in a list representing a cards deck and returns the value of the Primiera.


[Examples]

___
get_primiera_score(["Ad", "7d", "5h", "2c", "Ks"]) ➞ 58
# In the diamonds set 7 is higher than Ace (21 > 16).

get_primiera_score(["2d", "Jd", "7h", "Qc", "5s", "As"]) ➞ 59
# In the diamonds set 2 is higher than Jack (12 > 10), while in
# the spades set Ace is higher than 5 (16 > 15 ).

get_primiera_score(["2d", "Jd", "Qc", "5s", "As"]) ➞ 0
# There aren't cards in the hearts set, so Primiera can't be
# calculated.
_____



[Notes]

___
*) Notation: Ace, card numbers from 2 to 7, Jack, Queen or King + diamonds, hearts, clubs or spades.
*) If one or more seeds are missing from the deck the value of the Primiera is equal to 0.
___



[arrays] [conditions] [games] 



-------------------------------------------------------------------
[Resources]
_________
Dictionaries in Python
https://realpython.com/python-dicts/
In this Python dictionaries tutorial we'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, you …
_________
_________
Python Dictionary (With Examples)
https://www.programiz.com/python-programming/dictionary
In this tutorial, you'll learn everything about Python dictionaries; how they are created, accessing, adding, removing elements from them and various built-in methods.
_________
_________
max() Method
https://www.programiz.com/python-programming/methods/built-in/max
Returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters.
_________
_________
Scopa
https://en.wikipedia.org/wiki/Scopa
Is an Italian card game, and one of the two major national card games in Italy, the other being Briscola. It is also popular in Argentina and Brazil, brought in by Ital …
_________

"""
#Your code should go here:

