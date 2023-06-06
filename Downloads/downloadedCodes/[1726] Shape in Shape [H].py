"""
####  Shape in Shape  ####

For math class, Matt needs to find out if a shape can fit inside another shape, based solely on their area. The only problem is, HE SUCKS AT MATH! He has asked you, his older brother, to make a program that will answer all his math questions.
Write a function that takes two shapes, with different inputs, and returns True if the second shape has an area smaller than the first.
The inputs will be in a standardized format per shape:
___
*) "Circle, radius"
*) "Triangle, Base, Height"
*) "Rectangle, Width, Length (if different than Width) "
*) "Pentagon, Side"
___



[Examples]

___
shape_in_shape("Circle, 3", "Rectangle, 3, 14") ➞ False

shape_in_shape("Triangle, 10, 5", "Circle, 2") ➞ True

shape_in_shape("Pentagon, 10", "Circle, 10") ➞ False
_____



[Notes]

Remember, the first item in each string will be the name of the shape, and all relevant data will be provided following said name.


[algebra] [geometry] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How can I find the area of a pentagon just with the side lengths and not using trigonometry?
https://www.quora.com/How-can-I-find-the-area-of-a-pentagon-just-with-the-side-lengths-and-not-using-trigonometry
For a regular pentagon. Draw the two diagonals from the top vertex of the pentagon. These divide the pentagon into three isosceles triangles. You can find the altitude …
_________
_________
How to Find the Area of a Regular Pentagon
https://www.wikihow.com/Find-the-Area-of-a-Regular-Pentagon
A pentagon is a polygon with five straight sides. Almost all problems you'll find in math class will cover regular pentagons, with five equal sides. There are two commo …
_________
_________
Area of a Triangle
https://www.mathgoodies.com/lessons/vol1/area_triangle
Formula for finding the area of a triangle.
_________
_________
Area of a Pentagon
https://www.google.com/search?q=area+of+a+pentagon&rlz=1CATATK_enGB853&oq=area+of+a+pentagon&aqs=chrome..69i57j0l5.2624j0j4&sourceid=chrome&ie=UTF-8
Area of a regular pentagon = pa/2, where p = the perimeter and a = the apothem. If you don't know the perimeter, calculate it from the side length: p = 5s, where s is t …
_________
_________
Area of a Circle
https://www.mathsisfun.com/geometry/circle-area.html
Formula for finding the area of a circle.
_________
_________
Area of a Rectangle
https://www.mathgoodies.com/lessons/vol1/area_rectangle
Formula for the area of a rectangle or square.
_________

"""
#Your code should go here:

