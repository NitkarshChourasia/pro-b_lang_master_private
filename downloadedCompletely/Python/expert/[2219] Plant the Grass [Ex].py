"""
####  Plant the Grass  ####

You will be given a matrix representing a field g and two numbers x, y coordinate.
There are three types of possible characters in the matrix:
___
*) x representing a rock.
*) o representing a dirt space.
*) + representing a grassed space.
___

You have to simulate grass growing from the position (x, y). Grass can grow in all four directions (up, left, right, down). Grass can only grow on dirt spaces and can't go past rocks.
Return the simulated matrix.


[Examples]

___
simulate_grass([
  "xxxxxxx",
  "xooooox",
  "xxxxoox"
  "xoooxxx"
  "xxxxxxx"
], 1, 1) ➞ [
  "xxxxxxx",
  "x+++++x",
  "xxxx++x"
  "xoooxxx"
  "xxxxxxx"
]
_____



[Notes]

There will always be rocks on the perimeter


[algorithms] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Python if...else Statement
https://www.programiz.com/python-programming/if-elif-else
In this tutorial, you will learn about the Python if...else statement with the help of examples to create decision-making programs.
_________

"""
#Your code should go here:

