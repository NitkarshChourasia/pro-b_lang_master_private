"""
####  Finding the Inside Angle  ####

This challenge concerns non-convex polygons, such as the two polygons depicted below. 
One special property of non-convex polygons is that, for some of their vertices, the angle around that vertex that is contained inside the polygon is a reflex angle, i.e. an angle of more than 180 degrees. For this reason:
___
*) In the left polygon above we say that (1, 1), (3, 1) are reflex vertices (since the angle inside the polygon is a reflex angle) while (0, 0), (4, 0), (2, 5) are regular vertices.
*) In the right polygon we say that (1, 1) is a reflex vertex while all the other vertices are regular vertices.
___

Write a function which given:
___
*) A polygon described as a list of vertices where each vertex connects to the next and the last connects to the first (e.g. the polygons above are described by [(0, 0), (4, 0), (3, 1), (2, 5), (1, 1)] and [(0, 0), (4, 0), (3, 1), (1, 1), (2, 5)]) and ...
*) One of the vertices of the polygon.
___

Determines if the given vertex is a "regular" vertex or a "reflex" vertex.


[Examples (using the polygons depicted above)]

___
which_side([(0, 0), (4, 0), (3, 1), (2, 5), (1, 1)], (3, 1)) ➞ "reflex"

which_side([(0, 0), (4, 0), (3, 1), (2, 5), (1, 1)], (0, 0)) ➞ "regular"

which_side([(0, 0), (4, 0), (3, 1), (1, 1), (2, 5)], (3, 1)) ➞ "regular"

which_side([(0, 0), (4, 0), (3, 1), (1, 1), (2, 5)], (1, 1)) ➞ "reflex"
_____



[Notes]

___
*) The order of the vertices is important when specifying the polygon and thus affects whether each vertex is reflex or not (e.g. the two polygons above have the exact same vertices, but (3,1) is reflex in the left polygon and regular in the right polygon).
*) In both examples above the vertices of the polygons are listed in counter-clockwise order, but the tests will include both clockwise and counter-clockwise order cases.
___



[algebra] [math] [trigonometry] 



-------------------------------------------------------------------
[Resources]
_________
Angle
https://en.wikipedia.org/wiki/Angle
Is the figure formed by two rays, called the sides of the angle, sharing a common endpoint, called the vertex of the angle. Angles formed by two rays lie in a plane, bu …
_________

"""
#Your code should go here:

