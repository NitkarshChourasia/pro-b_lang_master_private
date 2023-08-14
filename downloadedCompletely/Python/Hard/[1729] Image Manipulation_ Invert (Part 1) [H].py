"""
####  Image Manipulation: Invert (Part 1)  ####

Images can be described as a 3D list.
___
# This image has only one white pixel:

[
  [[255, 255, 255]]
]
_____

___
# This one is a 2 by 2 black image:

[
  [[0, 0, 0], [0, 0, 0]],
  [[0, 0, 0], [0, 0, 0]]
]
_____

Your task is to create a function that takes a 3D list representation of an image and returns the inverse of that.
For example, white becomes black, black becomes white, etc.


[Examples]

___
invert([
  [[255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], [255, 255, 255]]
]) ➞ [
  [[0, 0, 0], [0, 0, 0]],
  [[0, 0, 0], [0, 0, 0]]
]
_____



[Notes]

___
*) A valid RGB value ranges from 0 to 255 (inclusive).
*) If the given list contains out of bound values, convert them to the nearest valid one.
___



[arrays] [data_structures] [logic] [loops] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

