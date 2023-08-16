"""
####  Center of Mass  ####

Implement the class Shape that receives perimeter and density function into __init__ method. The list of consecutive corners defines shape of a 2-dimensional object. The density function defines the mass distribution inside the shape. To compute mass in a certain point m(x, y) = small_square * density(x, y). The __init__ method calls other internal methods that compute three characteristics of the shape:
___
*) area
*) total mass
*) center of mass (xc, yc)
___

The computational grid has distance between two neighboring points as 2 * delta, the distance between a grid point and the perimeter wall is delta.


[Examples]

___
sh_ex1 = Shape([(1, 1), (3, 1), (3, 2), (1, 2)], lambda x, y: 100 + 100 * x)

sh_ex1.area ➞ 2.0

sh_ex1.mass ➞ 600.0

sh_ex1.mass_center ➞ (2.1, 1.5)
_____

The example can be verified via analytical integration. Other shapes in Tests are slightly more complicated and require numerical integration as illustrated here:



[Notes]

___
*) How to compute the center of mass is explained here.
*) Performance is not an issue as all tests can be computed within one second.
___



[classes] [physics] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

