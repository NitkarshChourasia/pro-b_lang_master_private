"""
####  Goldbach Conjecture  ####

Goldbach's Conjecture is amongst the oldest and well-known unsolved mathematical problems. In correspondence with Leonhard Euler in 1742, German mathematician Christian Goldbach made a conjecture, which states:
"Every even whole number greater than 2 is the sum of two prime numbers."
Even though it's been thoroughly tested and analyzed and seems to be true, it hasn't been proved yet (thus, remaining a conjecture.)
Create a function that takes a number and returns an array as per the following rules:
___
*) If the given number is odd and greater than two, return an empty array.
*) If the given number is even and greater than two, return an array of two prime numbers whose sum is the given input.
*) Both prime numbers must be the farthest (with the greatest difference).
___



[Examples]

___
goldbach_conjecture(1) ➞ []
# The given number is not greater than 2.

goldbach_conjecture(7) ➞ []
# The given number is not an even number.

goldbach_conjecture(14) ➞ [3, 11]
_____



[Notes]

Return list in sequence: [smaller, bigger]


[arrays] [logic] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Goldbach's Conjecture
https://en.wikipedia.org/wiki/Goldbach%27s_conjecture
One of the oldest and best-known unsolved problems in number theory and all of mathematics. It states that every even whole number greater than 2 is the sum of two prim …
_________
_________
Christian Goldbach
https://en.wikipedia.org/wiki/Christian_Goldbach
Was a German mathematician who also studied law. He is remembered today for Goldbach's conjecture.
_________
_________
Leonhard Euler
https://en.wikipedia.org/wiki/Leonhard_Euler
Was a Swiss mathematician, physicist, astronomer, geographer, logician and engineer who made important and influential discoveries in many branches of mathematics, such …
_________
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other program …
_________

"""
#Your code should go here:

