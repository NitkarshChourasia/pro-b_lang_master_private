"""
####  Four Vectors Part 1: Basic Operations  ####

This is the first challenge of the "Four Vectors" collection. Four Vectors are vectors with four components that are used to describe relativistic physics. For details please refer to this wiki entry.
In this challenge, create a class FourVector with the following properties:
___
*) If called with a list of length 4 as a parameter, it uses the list entries as components of the FourVector (FV) instance.
*) If called without a parameter, the components should be [0.0, 0.0, 0.0, 0.0].
*) Getter and Setter methods GetComponents and SetComponents, see test cases
*) Methods two add and subtract two FV instances.
*) Support comparing two Four Vectors.
*) Support printing a FV in the form (0.5, 1.0, -2.0, 10.0) where the components are rounded to three decimal places.
___

Consider using magic methods like __add__, __eq__ and __str__ to solve the last three bullet points.


[Examples]

___
v = FourVector([1, 2, 3, 4])
print(v) ➞ (1, 2, 3, 4)

v2 = FourVector([1, 0, 1, 0])
print(v + v2) ➞ (2, 2, 4, 4)
_____



[Notes]

Please save your FourVector class for later use, we will add new methods in upcoming challenges in this series!


[classes] [math] [physics] 



-------------------------------------------------------------------
[Resources]
_________
Object-Oriented Programming (OOP) in Python 3
https://realpython.com/python3-object-oriented-programming/
Learn all about object-oriented programming (OOP) in Python. You'll learn the basics of the OOP paradigm and cover concepts like classes and inheritance. You'll also se …
_________
_________
Classes and Objects
https://www.programiz.com/python-programming/class
In this tutorial, you will learn about the core functionality of Python objects and classes. You'll learn what a class is, how to create it and use it in your program.
_________
_________
Four-Vectors in Relativity
http://hyperphysics.phy-astr.gsu.edu/hbase/Relativ/vec4.html#:~:text=In%20the%20literature%20of%20relativity,is%20associated%20with%20physical%20ideas.
In the literature of relativity, space-time coordinates and the energy/momentum of a particle are often expressed in four-vector form. They are defined so that the leng …
_________
_________
Four-vector
https://en.wikipedia.org/wiki/Four-vector
Is an object with four components, which transform in a specific way under Lorentz transformation. Specifically, a four-vector is an element of a four-dimensional vecto …
_________
_________
__eq__
https://www.pythontutorial.net/python-oop/python-__eq__/
In this tutorial, you'll learn how to use the Python __eq__ method to compare two objects by their values.
_________

"""
#Your code should go here:

