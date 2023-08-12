"""
####  Asteroid Collision  ####

You are given a list asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


[Examples]

___
asteroid_collision([-2, -1, 1, 2]) ➞ [-2, -1, 1, 2]

asteroid_collision([-2, 1, 1, -2]) ➞ [-2, -2]

asteroid_collision([1, 1, -2, -2]) ➞ [-2, -2]

asteroid_collision([10, 2, -5]) ➞ [10]

asteroid_collision([8, -8]) ➞ []
_____



[Notes]

BONUS: Use only one loop (either for or while).


[arrays] [games] [loops] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Useful Array Methods
https://www.w3schools.com/python/python_ref_list.asp
Python has a set of built-in methods that you can use on lists/arrays.
_________
_________
Lists
https://www.w3schools.com/python/python_lists.asp
When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meani …
_________
_________
Conditions
https://www.w3schools.com/python/python_conditions.asp
In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that …
_________

"""
#Your code should go here:

