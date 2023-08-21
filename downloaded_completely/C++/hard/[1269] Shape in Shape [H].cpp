/*
####  Shape in Shape  ####

For math class, Matt needs to find out if a shape can fit inside another shape, based solely on their area. The only problem is, HE SUCKS AT MATH! He has asked you, his older brother, to make a program that will answer all his math questions.
Write a function that takes two shapes, with different inputs, and returns true if the second shape has an area smaller than the first.
The inputs will be in a standardized format per shape:
___
*) "Circle, radius"
*) "Triangle, Base, Height"
*) "Rectangle, Width, Length (if different than Width) "
*) "Pentagon, Side"
___



[Examples]

___
shapeInShape("Circle, 3", "Rectangle, 3, 14") ➞ false

shapeInShape("Triangle, 10, 5", "Circle, 2") ➞ true

shapeInShape("Pentagon, 10", "Circle, 10") ➞ false
_____



[Notes]

Remember, the first item in each string will be the name of the shape, and all relevant data will be provided following said name.


[algebra] [geometry] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

