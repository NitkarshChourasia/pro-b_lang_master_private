"""
####  Blackjack  ####

Create a function that takes a list of card numbers and checks if the sum of their value exceeds 21. If the sum exceeds 21, return True and if the sum is under or equal to 21, return False. Values of the cards are as follows:
___
*) 2-10 are their value.
*) J-K (face cards) count as 10.
*) Aces count either as 1 or 11 - play conservatively, so that if giving an ace a value of 11 causes you to lose and 1 allows you to win, then go with 1.
___



[Examples]

___
over_twenty_one([2, 8, "J"]) ➞ False

over_twenty_one(["A", "J", "K"]) ➞ False

over_twenty_one([5, 5, 3, 9]) ➞ True

over_twenty_one([2, 6, 4, 4, 5]) ➞ False

over_twenty_one(["J", "Q", "K"]) ➞ True
_____



[Notes]

There will be a maximum of one ace in each hand.


[arrays] [conditions] [games] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Blackjack Rules
https://bicyclecards.com/how-to-play/blackjack/
If you don't know when the user wins or not, see the "Object of the Game" section, so you can understand how to use Aces.
_________
_________
isdigit() Method
https://www.programiz.com/python-programming/methods/string/isdigit
Returns True if all characters in a string are digits. If not, it returns False.
_________
_________
Python for Loop
https://www.programiz.com/python-programming/for-loop
In this article, you'll learn to iterate over a sequence of elements using the different variations of for loop.
_________
_________
sum() Method
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum.
_________

"""
#Your code should go here:

