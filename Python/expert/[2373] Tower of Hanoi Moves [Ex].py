"""
####  Tower of Hanoi Moves  ####

Create a function (given the number of discs and the move number) that returns as a tuple the towers with their correct disks in order.


[What is Tower of Hanoi?]

Tower of Hanoi is a problem in occursion, where you have to move a certain amount of discs from one peg (or tower) to the final peg. The discs are stacked on pegs with each disc being smaller than the last, as to create a pyramid like shape.

To illustrate, lets take tower_of_hanoi(4, 3). The first move you would make would be to move the 1 disc from the 1st tower to the 3rd tower. So move one would result in:
___
([4, 3, 2], [], [1])
_____

Then you would move the 2 disk from the 1st tower to the 2nd peg. Resulting in:
___
([4, 3], [2], [1])
_____

Then the final move would be to move the 1 disk onto the 2nd peg:
___
([4, 3], [2, 1], [])
_____

Then that would be your answer!


[Examples]

___
tower_of_hanoi(1, 1) ➞ ([], [], [1])

tower_of_hanoi(4, 3) ➞ ([4, 3], [], [2, 1])

tower_of_hanoi(7, 12) ➞ ([7, 6, 5, 2, 1], [4, 3], [])
_____



[Notes]

The universal solution for the Tower of Hanoi differs if the number of discs is even or odd (check the Resources tab for help).


[algebra] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Wikipedia article on Tower of Hanoi
https://en.wikipedia.org/wiki/Tower_of_Hanoi
Gives the universal solution in an easy and understandable way
_________

"""
#Your code should go here:

