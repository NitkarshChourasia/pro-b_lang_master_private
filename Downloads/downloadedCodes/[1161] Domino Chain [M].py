"""
####  Domino Chain  ####

Mubashir was playing with dominos. He concluded that:
___
*) If the first domino is pushed over, it will keep tipping next dominos to its right.
*) Reaction will stop if a domino is already tipped over, or if there is an empty space.
___


Create a function which takes a string of current status of the dominos and returns the string after dominos chain reaction.
___
*) "|" represents a standing domino.
*) "/" represents a tripped domino.
*) " " represents an empty space.
___



[Examples]

___
domino_chain("||| ||||//| |/") ➞ "/// ||||//| |/"
// A space will stop the reaction.

domino_chain("||//||") ➞ "////||"
// An already tripped domino will stop the reaction.

domino_chain("||||") ➞ "////"
_____



[Notes]

N/A


[algorithms] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
enumerate() function
https://www.w3schools.com/python/ref_func_enumerate.asp
Takes a collection (e.g. a tuple) and returns it as an enumerate object. The enumerate() function adds a counter as the key of the enumerate object.
_________

"""
#Your code should go here:

