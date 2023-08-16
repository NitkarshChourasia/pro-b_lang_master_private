"""
####  Image Manipulation: 255 Shades of Grey (Part 2)  ####

Images can be described as 3D lists.
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

Your task is to create a function that takes a 3D list representation of an image and returns the grayscale version of that.


[Examples]

___
grayscale([
  [[0, 0, 0], [0, 0, 157]],
  [[1, 100, 0], [0, 10, 0]]
]) ➞ [
  [[0, 0, 0], [52, 52, 52]],
  [[34, 34, 34], [3, 3, 3]]
]
_____



[Notes]

___
*) A valid RGB value ranges from 0 to 255 (inclusive).
*) If the given list contains out of bound values, convert them to the nearest valid one.
*) Grayscaling an image is adjusting to have the same amount of (Red, Green, Blue) from their combined average to produce different shades of gray.
___



[algorithms] [arrays] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
sum() Funtion
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
round() Function
https://www.programiz.com/python-programming/methods/built-in/round
Returns a floating-point number rounded to the specified number of decimals. In this tutorial, we will learn about Python round() in detail with the help of examples.
_________
_________
Grayscale to RGB Conversion
https://www.tutorialspoint.com/dip/grayscale_to_rgb_conversion.htm
We have already defined the RGB color model and grayscale format in our tutorial on Image types. Now we will convert a color image into a grayscale image.
_________
_________
RGB Color Codes Chart 🎨
https://www.rapidtables.com/web/color/RGB_Color.html
RGB color codes chart, RGB color picker, RGB color table.
_________
_________
Multidimensional Lists
https://www.ict.social/python/basics/multidimensional-lists-in-python
Intro to multidimensional lists in python and how to loop through them.
_________

"""
#Your code should go here:

