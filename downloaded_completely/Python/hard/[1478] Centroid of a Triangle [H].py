"""
####  Centroid of a Triangle  ####

If you have a triangular shape cut from a piece of cardboard, the centroid of the triangle would be the spot where it balances on the point of a pencil. The location of the centroid is easy to calculate if you know the x, y coordinates of the vertices:
___
*) The x coordinate of the centroid is at (x1 + x2 + x3) / 3
*) The y coordinate of the centroid is at (y1 + y2 + y3) / 3
___

x1, y1, x2, y2, x3, y3 are the coordinates of the three vertices.
Create a function that calculates the position of the centroid given the coordinates of the vertices. Round the answers to two decimal places. If the three points given do not form a triangle, return False.


[Examples]

___
centroid(0, 0, 3, 0, 3, 3) ➞ (2.0, 1.0)

centroid(2, 2, 8, -2, 0, -3) ➞ (3.33, -1.0)

centroid(1, 1, 2, 2, 3, 3) ➞ False
_____



[Notes]

___
*) The arguments are given in the order shown above: x1, y1, x2, y2, x3, y3.
*) If the three points do not form a triangle, they must lie in a straight line.
___



[algebra] [math] 



-------------------------------------------------------------------
[Resources]
_________
Collinear
http://mathworld.wolfram.com/Collinear.html
Three or more points are said to be collinear if they lie on a single straight line . A line on which points lie, especially if it is related to a geometric figure such …
_________
_________
Centroid of a Triangle
https://brilliant.org/wiki/triangles-centroid/
The centroid of a triangle is the intersection of the three medians, or the "average" of the three vertices. It has several important properties and relations with othe …
_________

"""
#Your code should go here:

