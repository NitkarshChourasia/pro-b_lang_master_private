"""
####  Track the Robot (Part 2)  ####

This robot roams around a 2D grid. It starts at (0, 0) facing North. After each time it moves, the robot rotates 90 degrees clockwise. Given the amount the robot has moved each time, you have to calculate the robot's final position.
To illustrate, if the robot is given the movements 20, 30, 10, 40 then it will move:
___
*) 20 steps North, now at (0, 20)
*) 30 steps East, now at (30, 20)
*) 10 steps South. now at (30, 10)
*) 40 steps West, now at (-10, 10)
___

...and will end up at coordinates (-10, 10).


[Examples]

___
track_robot(20, 30, 10, 40) ➞ [-10, 10]

track_robot() ➞ [0, 0]
# No movement means the robot stays at (0, 0).

track_robot(-10, 20, 10) ➞ [20, -20]
# The amount to move can be negative.
_____



[Notes]

Each movement is an integer (whole number).


[conditions] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
*args and **kwargs
https://book.pythontips.com/en/latest/args_and_kwargs.html
Describes how to manage a varying amount of variables being inputted into a function.
_________
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
Used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
_________

"""
#Your code should go here:

