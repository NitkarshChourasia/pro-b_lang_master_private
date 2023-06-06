"""
####  Cannon Fire  ####

A cannon sits in an open field ready to fire. You know the location of the cannon in cartesian coordinates. You know the direction that the barrel is pointed as a clockwise bearing from the north. You also know the distance that the cannonball will travel.
Devise a function that finds the coordinates of the spot where the cannonball strikes its target. Round to the nearest integer.
___
cannon(location, angle, distance) ➞ target location
_____

A clockwise bearing from the north simply means that at 0 degrees the cannon is pointing north, at 90 degrees it is pointing east, at 180 degrees it is pointing south, and at 270 degrees it is pointing west.


[Examples]

___
cannon((0, 0), 0, 10) ➞ (0, 10)

cannon((0, 0), 270, 10) ➞ (-10, 0)

cannon((0, 0), 45, 10) ➞ (7, 7)

cannon((-12, -2), 193, 9) ➞ (-14, -11)
_____



[Notes]

The distance here is the length along the ground that the cannonball travels, not its arc above ground, so treat this as a plane trigonometry problem.


[math] [trigonometry] 



-------------------------------------------------------------------
[Resources]
_________
degrees() and radians()
https://www.geeksforgeeks.org/degrees-and-radians-in-python/
Often one is in need to handle mathematical computation of conversion of radians to degrees and vice-versa, especially in the field of geometry. Python offers inbuilt m …
_________
_________
Trigonometry
https://www.mathsisfun.com/algebra/trigonometry.html
We can't reach the top of the tree, so we walk away and measure an angle (using a protractor) and distance (using a laser).
_________
_________
Polar and Cartesian Coordinates
https://www.mathsisfun.com/polar-cartesian-coordinates.html
When we know a point in Cartesian Coordinates (x,y) and we want it in Polar Coordinates (r,θ) we solve a right triangle with two known sides.
_________

"""
#Your code should go here:

