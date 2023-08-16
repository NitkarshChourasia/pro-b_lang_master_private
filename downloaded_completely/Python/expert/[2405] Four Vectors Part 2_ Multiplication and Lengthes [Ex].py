"""
####  Four Vectors Part 2: Multiplication and Lengthes  ####

In this challenge, we extend the FourVector class we created in the first installment of the FourVector collection.
So, please add the following features to the class FourVector:
___
*) Support multiplication of Four Vectors (FV). This should include multiplication of two FVs as well as multiplications 'scalar times FV' and 'FV times scalar'. Think about magic methods like __mul__...
*) A method GetLength which returns the length of the FV. The length is the square root of the absolute value of the product of the FV with itself. Attention: contrasting to 'normal' vectors the product of a FV with itself may be negative! For details refer to the Wiki article (see resources).
*) A method GetCausalStructure. Let p the product of the FV with itself. The method then returns "lightlike" if p=0, "spacelike" if p<0 and "timelike" if p>0. The causal structure has an important meaning in special relativity: a lightlike FV can be connected to the origin (0, 0, 0, 0) by a ray a light, a timelike FV is connected to the origin by 'more time than space' which means there can be a causal connection (cause and effect) between the origin and the event represented by the FV. In contrast, for a spacelike FV there is 'more space than time' and there can't be a causal connection without violating the 'speed limit' of special relativity.
___



[Examples]

___
v1 = FourVector([1, 2, 3, 4])
v2 = FourVector([1, 0, 0, 1])
2 * v1 ➞ FourVector([2, 4, 6, 8])
v2 * 3 ➞ FourVector([3, 0, 0, 3])
v1 * v3 ➞ -3
v1.GetLength() ➞ 5.291502622129181
v1.GetCausalStructure() ➞ "spacelike"
_____



[Notes]

Please save your FourVector class for later use, we will add new methods in upcoming challenges in this series!


[classes] [math] [physics] 



-------------------------------------------------------------------
[Resources]
_________
Four-Vectors in Relativity
http://hyperphysics.phy-astr.gsu.edu/hbase/Relativ/vec4.html#:~:text=In%20the%20literature%20of%20relativity,is%20associated%20with%20physical%20ideas.
In the literature of relativity, space-time coordinates and the energy/momentum of a particle are often expressed in four-vector form. They are defined so that the leng …
_________
_________
Object-Oriented Programming (OOP) in Python
https://realpython.com/python3-object-oriented-programming/
In this tutorial, you'll learn all about object-oriented programming (OOP) in Python. You'll learn the basics of the OOP paradigm and cover concepts like classes and in …
_________
_________
Python Operator Overloading
https://www.programiz.com/python-programming/operator-overloading
You can change the meaning of an operator in Python depending upon the operands used. In this tutorial, you will learn how to use operator overloading in Python Object …
_________
_________
Four-vector
https://en.wikipedia.org/wiki/Four-vector
Is an object with four components, which transform in a specific way under Lorentz transformation. Specifically, a four-vector is an element of a four-dimensional vecto …
_________

"""
#Your code should go here:

