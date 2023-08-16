"""
####  Four Vectors Part 3: Lorentz Transformations  ####

In this challenge, we extend the FourVector class we created in the first and second installment of the FourVector collection. We will now add Lorentz transformations namely "Pure Rotations" and "Pure Boosts". For details on this operation, please refer to the Wiki page linked in the Resources.
So, please add the following features to the class FourVector:
___
*) A helper method KroneckerDelta which takes two integers (say i and j) and returns 1 if i=j and 0 otherwise.
*) A helper method LeviCivitaSymbol which takes three integers (say i, j and k) and returns 1 if (i,j,k) is an even permutation of (1,2,3) (i.e. (i,j,k) is (1,2,3), (2,3,1) or (3,1,2)), -1if (i,j,k) is an odd permutation of (1,2,3) (i.e. (i,j,k) is (1,3,2), (2,1,3) or (3,2,1)) and 0 otherwise (i.e. if i=j or i=k or j=k).
*) A method PureRotation which takes a 3D-vector and an angle (in degrees) as arguments. It should perform a pure rotation (no boost) as specified here. In the test cases, the 3D-vector is not always a unit vector, so please normalize it. The return value is a new Four Vector, i.e. the original FV is not changed.
*) A method PureBoost which takes a 3D-vector as an argument representing a 3-velocity between the two reference frames as specified here. It should perform a pure boost (no rotation by the 3-velocity passed as argument). The return value is a new Four Vector, i.e. the original FV is not changed. Please use a value of 299792458 for the speed of light (in meters per second).
___



[Examples]

___
u1 = FourVector([0, 1, 0, 0])
u1.KroneckerDelta(1, 1) ➞ 1
u1.KroneckerDelta(1, 2) ➞ 0
u1.LeviCivitaSymbol(1, 3, 2) ➞ -1
u1.LeviCivitaSymbol(1, 3, 1) ➞ 0
u1.PureRotation([0, 1, 0], 90) ➞ FourVector([0.0, 0.0, 0.0, -1.0])
c = 299792458.0
u1.PureBoost([c/100., 0, 0]) ➞ FourVector([-0.010000500037503126, 1.0000500037503126, 0.0, 0.0])
_____



[Notes]

Please save your FourVector class for later use, we will add new features in upcoming challenges in this series! You may assume valid test cases (e.g. no boost with v=[0,0,0]).


[classes] [math] [physics] 



-------------------------------------------------------------------
[Resources]
_________
Lorentz Transformations, Rotations, and Boosts
http://home.ku.edu.tr/~amostafazadeh/phys517_518/phys517_2016f/Handouts/A_Jaffi_Lorentz_Group.pdf
In these notes we study rotations in R3 and Lorentz transformations in R4. First we analyze the full group of Lorentz transformations and its four distinct, connected c …
_________
_________
Four-vectors in Relativity
http://hyperphysics.phy-astr.gsu.edu/hbase/Relativ/vec4.html#:~:text=In%20the%20literature%20of%20relativity,is%20associated%20with%20physical%20ideas.
In the literature of relativity, space-time coordinates and the energy/momentum of a particle are often expressed in four-vector form. They are defined so that the leng …
_________
_________
Four Vector
https://en.wikipedia.org/wiki/Four-vector
Is an object with four components, which transform in a specific way under Lorentz transformation. Specifically, a four-vector is an element of a four-dimensional vecto …
_________

"""
#Your code should go here:

