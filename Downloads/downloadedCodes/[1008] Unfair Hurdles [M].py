"""
####  Unfair Hurdles  ####

Unfair hurdles are hurdles which are either too high, or way too close together.
Create a function which takes in a list of strings, representing hurdles, and return whether they are unfair. For the purposes of this challenge, unfair hurdles are:
___
*) At least 4 characters tall.
*) Strictly less than 4 spaces apart.
___



[Examples]

___
# Hurdle are good distance apart but are way too tall.

is_unfair_hurdle([
  "#    #    #    #",
  "#    #    #    #",
  "#    #    #    #",
  "#    #    #    #"
]) ➞ True


# Hurdles are a fine height but are way too close together.

is_unfair_hurdle([
  "#  #  #  #",
  "#  #  #  #",
  "#  #  #  #"
]) ➞ True


# These hurdles are mighty splendid.

is_unfair_hurdle([
  "#      #      #      #",
  "#      #      #      #"
]) ➞ False
_____



[Notes]

___
*) Hurdles will be represented with a hashtag "#".
*) There will be the same spacing between hurdles.
*) Hurdles are always as high as the length of the list.
*) Hurdles are always evenly spaced.
___



[arrays] [logic] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Count the Number of Spaces in a String in Python
https://www.codespeedy.com/count-the-number-of-spaces-in-a-string-in-python/
In this tutorial, we will learn how to count the number of spaces in a given string in Python. Before proceeding to the solution, let us understand the problem first wi …
_________

"""
#Your code should go here:

