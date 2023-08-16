"""
####  Swapping Cards  ####

Two players draw a pair of numbered cards so that both players can form a 2 digit number. A winner can be decided if one player's number is larger than the other.
However, there is a rule where a player can swap any one of their cards with any one of the other player's cards in a gamble to get a higher number! Note that it is illegal to swap the order of your own cards. That means if you draw a 1 then a 9, you cannot swap them to get 91.

Paul's strategy is to always swap his lowest number with the opponent's ten's digit. Return whether this results in Paul winning the round.
___
*) n1 is Paul's number
*) n2 is his opponent's number
___



[Worked Example]

___
swap_cards(41, 79) ➞ True
# Paul's lowest number is 1
# The opponent's ten's digit is 7
# After the swap: 47 > 19
# Paul wins the round
_____



[Examples]

___
swap_cards(41, 98) ➞ True

swap_cards(12, 28) ➞ True

swap_cards(67, 53) ➞ False

swap_cards(77, 54) ➞ False
_____



[Notes]

___
*) If both of Paul's digits are the same, swap the ten's digit with the opponent's (paul likes to live riskily).
*) The cards don't include the number 0.
___



[algorithms] [games] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
replace() Method
https://www.w3schools.com/python/ref_string_replace.asp
Replaces a specified phrase with another specified phrase.
_________

"""
#Your code should go here:

