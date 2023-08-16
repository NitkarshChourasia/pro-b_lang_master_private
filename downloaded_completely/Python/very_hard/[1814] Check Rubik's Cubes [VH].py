"""
####  Check Rubik's Cubes  ####

Matt wants to make Rubik Cubes. These Rubiks should be in the shape of a full cube, and it shouldn't have any missing parts.
This is a full cube:

This is not a full cube:

And he asks his friend to draw some patterns. When his friend gives him these Rubik's Cube patterns, he realizes that some of them are wrong or missing. Help him identify them!
The small cubes that make up the Rubik's Cube will be denoted by "O".
___
*) Return "Full" if the Rubik Cube is full and no part is missing.
*) Return "Non-Full" if the Rubik Cube is non-full and no part is missing.
*) Return "Missing {number of missing parts}" if the Rubik Cube has missing parts.
___



[Examples]

___
identify(
  ["O", "O", "O"],
  ["O", "O", "O"],
  ["O", "O", "O"]
) ➞ "Full"

# This is 3x3 full Rubik's Cube.
# So we should return "Full"
_____

___
identify(
  ["O", "O", "O"],
  ["O", "O", "O"]
) ➞ "Non-Full"

# This is a 2x3 Rubik's Cube.
# It's not full, so we should return "Non-Full".
_____

___
identify(
  ["O", "O"],
  ["O", "O", "O"],
  ["O", "O", "O"]
) ➞ "Missing 1"

# This is almost a 3x3 Rubik's Cube with one missing part.
# We should return "Missing 1".
_____



[Notes]

___
*) Every cubic (small part of a Rubik's Cube) will be denoted by "O". There won't be any other type.
*) Don't forget to return by paying attention to capital letters.
___



[algorithms] [arrays] [geometry] [math] 



-------------------------------------------------------------------
[Resources]
_________
sum() Method
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
*args and **kwargs
https://www.geeksforgeeks.org/args-kwargs-python/
In Python, we can pass a variable number of arguments to a function using special symbols. 1.)*args (Non-Keyword Arguments), 2.)**kwargs (Keyword Arguments).
_________
_________
Rubik's Cube
https://en.wikipedia.org/wiki/Rubik%27s_Cube
Is a 3-D combination puzzle invented in 1974 by Hungarian sculptor and professor of architecture Ernő Rubik.
_________

"""
#Your code should go here:

