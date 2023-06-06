"""
####  Range of Rolled Dice  ####

You are playing a game of JavaScript & Jackalopes with your friends, and need to roll dice as part of the game. None of you actually own dice, but you do have a computer handy!
You'll be given a string representing the number of dice to roll, how many faces each die has, and a "modifier" to apply to the final result after adding up all the dice. For example, rolling a single six-sided die with no modifier might be represented by the string "1d6" — one die with six sides and values ranging from 1 through 6. If you wanted to add 2 to the result of rolling the same die, you might represent that as "1d6+2".
Create a function that takes a string representing a set of dice to be rolled as an argument, and returns a list of two numbers representing the minimum and maximum possible values that could be achieved.


[Examples]

___
dice_range("1d6") ➞ [1, 6]
# If a modifier is not given, assume that nothing will be
# added to/subtracted from the results.

dice_range("1d6+2") ➞ [3, 8]

dice_range("d6") ➞ [1, 6]
# If a number of dice is not provided, assume only one is
# being rolled.

dice_range("d6-2") ➞ [-1, 4]
# If a modifier is negative, the resulting values may be
# negative as well.

dice_range("2d6") ➞ [2, 12]

dice_range("2d6-1") ➞ [1, 11]
# The modifier should be added to/subtracted from the
# final result after rolling all the dice and adding up their
# results, not applied to each roll!

dice_range("0d6+1") ➞ [1, 1]
# If you roll no dice, the result will only be whatever the
# modifier's value is with no randomness.
_____



[Notes]

___
*) All inputs will be valid inputs for the function.
*) The number of dice to roll in each test will be either a positive integer, zero, or omitted (with a default assumed value of 1).
*) The number of sides of the dice to roll in each test will be a positive integer.
*) The modifier in each test will be either an integer (positive, negative, or zero) or omitted (with a default assumed value of 0).
___



[games] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Regular Expression Operations
https://docs.python.org/3/library/re.html
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________

"""
#Your code should go here:

