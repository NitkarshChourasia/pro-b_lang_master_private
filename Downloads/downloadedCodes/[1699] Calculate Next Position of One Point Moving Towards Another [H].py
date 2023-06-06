"""
####  Calculate Next Position of One Point Moving Towards Another  ####

A point on the screen (pt1) wants to move a certain distance (dist) closer to another point on the screen (pt2) The function has three arguments, two of which are dictionaries with x & y values, and the third being the distance, e.g. {'x':50, 'y':60}, {'x': 100, 'y': 100}, 10. The expected result is a similar dictionary with the new co-ordinate.


[Examples]

___
get_next_position({"x": 50, "y": 60}, {"x": 100, "y": 100}, 10) ➞ {"x": 58, "y": 66}

get_next_position({"x": 0, "y": 0}, {"x": 100, "y": 0}, 10) ➞ {"x": 10, "y": 0}

get_next_position({"x": 0, "y": 0}, {"x": 100, "y": 100}, 10) ➞ {"x": 7, "y": 7}

get_next_position({"x": 250, "y": 10}, {"x": -20, "y": 35}, 55) ➞ {"x": 195, "y": 15}
_____



[Notes]

___
*) The returned x & y values should be rounded to the closest integer
*) If the distance between the two points is less than distance wanting to be traveled, then the returned co-ordinate should overshoot the mark, e.g. {"x": 50, "y": 0}, {"x": 70, "y": 0}, 30) ➞ {"x": 80, "y": 0}.
___



[algebra] [games] [math] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Vectors - Normalizing
http://www.fundza.com/vectors/normalize/
Normalize a vector in order to multiply by a magnitude to find a new vector.
_________
_________
sqrt() Method
https://www.tutorialspoint.com/python/number_sqrt.htm
Returns the square root of x for x > 0.
_________
_________
Data Structures
https://docs.python.org/3/tutorial/datastructures.html
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.ins …
_________

"""
#Your code should go here:

