"""
####  Moving Particles Absorb Each Other after Collisions  ####

The function is given a list of particles. The absolute value represents the particle mass. The sign of value represents the direction of movement:
___
*) Positive values move to the right.
*) Negative values move to the left.
___

A positive value located on the left will collide with a negative value immediately located on the right. The particle with the greater mass will absorb the mass of another particle and continue to travel in its direction. If the negative is greater, the combined particle will continue to move to the left, if the positive mass is greater or equal, the combined particle will continue to move to the right. The mass of the combined particle is the sum of absolute values. Two particles moving in the same direction cannot collide because it is assumed that the speed is the same before and after collisions. The new combined particles can collide again. The total picture of remaining particles can evolve and evolve.
Eventually, the equilibrium is reached when all negative values are on the left and all positive values are on the right. The left group is moving away from the right group. Determine the equilibrium state of the transformed particles and return it as a list.


[Examples]

___
moving_particles([3, -1]) ➞ [4]
# 3 absorbs -1.

moving_particles([-1, 3, -1, 2]) ➞ [-1, 4, 2]
# -1 is moving to the left, 2 is moving to the right, 3 absorbs -1.

moving_particles([]) ➞ []
# No particles are in the list.

moving_particles([5, -1, -2, -9]) ➞ [-17]
# 5 absorbs -1, new 6 absorbs -2, new 8 is being absorbed by -9.
_____



[Notes]

The problem is not ideally symmetric. If the masses are the same, the positive mass absorbs the negative mass and continues moving to the right. This assumption is to account for all possibilities.


[algorithms] [games] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Python For Loops
https://www.w3schools.com/python/python_for_loops.asp
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other program …
_________

"""
#Your code should go here:

