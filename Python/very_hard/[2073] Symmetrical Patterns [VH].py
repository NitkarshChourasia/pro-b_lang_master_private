"""
####  Symmetrical Patterns  ####

Kathleen owns a beautiful rug store. She likes to group the rugs into 4 mutually exclusive categories.
___
*) imperfect
*) horizontally symmetric
*) vertically symmetric
*) perfect
___

An imperfect rug is one that is neither horizontally nor vertically symmetric. Here is an example of an imperfect rug:
___
[
  ["a", "a", "a", "a"],
  ["a", "a", "a", "a"],
  ["a", "a", "b", "b"]
]
_____

The following is an horizontally symmetric rug. You could "fold" the rug across a hypothetical x-axis, and both sides would be identical. A horizontally symmetric rug is not vertically symmetric (otherwise this rug would be classified as perfect ).
___
[
  ["c", "a", "a", "a"],
  ["b", "b", "b", "b"],
  ["c", "a", "a", "a"]
]
_____

The following is a vertically symmetric rug. You could "fold" the rug across a hypothetical y-axis, and both sides would be identical. A vertically symmetric is not horizontally symmetric (otherwise this rug would be classified as perfect ).
___
[
  ["a", "b", "a"],
  ["b", "b", "b"],
  ["a", "b", "a"],
  ["a", "b", "a"]
]
_____

Finally, a perfect rug is one that is both vertically and horizontally symmetric. That is, folded either length-wise or width-wise will yield two identical pieces.
___
[
  ["a", "b", "b", "a"],
  ["b", "b", "b", "b"],
  ["a", "b", "b", "a"]
]
_____

Given a rug of m x n dimension, determine whether it is imperfect, horizontally symmetric, vertically symmetric or perfect. Rugs are represented using a two-dimensional list.


[Examples]

___
classify_rug([
  ["a", "a"],
  ["a", "a"]
]) ➞ "perfect"

classify_rug([
  ["a", "a", "b"],
  ["a", "a", "a"],
  ["b", "a", "a"]
]) ➞ "imperfect"

classify_rug([
  ["b", "a"],
  ["b", "a"]
]) ➞ "horizontally symmetric"

classify_rug([
  ["a", "a"],
  ["b", "b"]
]) ➞ "vertically symmetric"
_____



[Notes]

You can consider a 1 x n rug as being trivially horizontally symmetric, an n x 1 rug as being trivially vertically symmetric, and a 1 x 1 rug as being trivially perfect.


[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
range() Method
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________

"""
#Your code should go here:

