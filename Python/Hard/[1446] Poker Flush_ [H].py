"""
####  Poker Flush?  ####

Create a function that takes in two lists and determines whether there exists a flush.
___
*) The first list represents the 5 cards dealt on the table.
*) The second list represents the 2 cards in your hand.
___

Notation: card number and suit (abbreviated as S = Spades, H = Hearts, D = Diamonds, C = Clubs) separated by an underscore.


[Examples]

___
check_flush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]) ➞ True // diamond flush

check_flush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]) ➞ True // spade flush

check_flush(["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"]) ➞ False
_____



[Notes]

Hint: If there aren't at least 3 cards of the same suit on the table, there is zero chance of there being a flush.


[arrays] [conditions] [control_flow] [games] [regex] 



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
Returns the number of occurrences of an element in a list.
_________
_________
any() Method
https://www.programiz.com/python-programming/methods/built-in/any
Returns True if any element of an iterable is True. If not, any() returns False.
_________
_________
max() Function
https://www.programiz.com/python-programming/methods/built-in/max
Returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters.
_________
_________
What is a "flush" in poker?
https://en.wikipedia.org/wiki/List_of_poker_hands#Flush
A flush is a hand that contains five cards all of the same suit, not all of sequential rank.
_________
_________
set() Constructor
https://www.programiz.com/python-programming/methods/built-in/set
Constructs a Python set from the given iterable and returns it.
_________

"""
#Your code should go here:

