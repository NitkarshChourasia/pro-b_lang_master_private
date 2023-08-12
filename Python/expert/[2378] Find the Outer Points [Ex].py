"""
####  Find the Outer Points  ####

In this challenge, you will be given a set of points in the plane, which we can visualize as on the left below:

By connecting the points, one obtains a convex polygon containing all points, as on the right.
Write a function that, given a set of points, returns only the outer points (i.e. the vertices of the polygon (in the illustration, these are points circled in red)).


[Examples]

___
outer_points({(0,0), (2,0), (2,2), (0,2), (1,1)})
 ➞ {(0,0), (2,0), (2,2), (0,2)}

outer_points({(0,0), (1,0), (2,0), (0,1)})
 ➞ {(0,0), (2,0), (0,1)}

outer_points({(0,0), (0,1), (0,3), (2,1), (2,2), (3,0)})
 ➞ {(0,0), (0,3), (2,2), (3,0)}
_____



[Notes]

___
*) The points will be given in no particular order.
*) As in the illustration, some points may be on an edge of the polygon, but not be vertices of the polygon. Such points do not count as outer points.
*) The polygon described above is also called the convex hull of the set.
___



[algebra] [math] [trigonometry] 



-------------------------------------------------------------------
[Resources]
_________
Jarvis' Convex Hull Algorithm
https://en.wikipedia.org/wiki/Gift_wrapping_algorithm#Pseudocode
Pseudocode describing an algorithm for finding the convex hull of a set of points.
_________
_________
Convex Hull Algorithms: Jarvis's March
https://algorithmtutor.com/Computational-Geometry/Convex-Hull-Algorithms-Jarvis-s-March/
Uses a process called gift wrapping to find the convex hull. It is one of the simplest algorithms for computing convex hull. The working of Jarvis's march resembles the …
_________
_________
ConvexHull
https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html
Raised when Qhull encounters an error condition, such as geometrical degeneracy when options to resolve are not enabled.
_________

"""
#Your code should go here:

