"""
####  Look and Say Numbers  ####

Given an integer, return a new integer according to the rules below:
___
*) Split the number into groups of two digit numbers. If the number has an odd number of digits, return "invalid".
*) For each group of two digit numbers, concatenate the last digit to a new string the same number of times as the value of the first digit.
*) Return the result as an integer.
___

___
look_and_say(3132) ➞ 111222

# By reading the number digit by digit, you get three "1" and three "2".
# Therefore, you put three ones and three two's together.
# Remember to return an integer.
_____



[Examples]

___
look_and_say(95) ➞ 555555555

look_and_say(1213141516171819) ➞ 23456789

look_and_say(120520) ➞ 200

look_and_say(231) ➞ "invalid"
_____



[Notes]

___
*) Note that the number 0 can be included (see example #3).
*) Check the Resources tab for a TED-Ed video for extra clarity.
___



[algorithms] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Look and Say Sequences
https://www.youtube.com/watch?v=LpjX3kHXcR0
1, 11, 21, 1211, 111221. These are the first five elements of a number sequence. Can you figure out what comes next? Alex Gendler reveals the answer and explains how be …
_________

"""
#Your code should go here:

