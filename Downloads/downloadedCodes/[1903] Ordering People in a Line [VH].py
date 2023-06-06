"""
####  Ordering People in a Line  ####

Create a function that takes in the size of the line and the number of people waiting and places people in an S-shape ordering. The demonstration below will make it clear:
___
# Ordering numbers 1-15 in a [5,3] space.

order_people([5, 3], 15) ➞ [
  [1, 2, 3],
  [6, 5, 4],
  [7, 8, 9],
  [12, 11, 10],
  [13, 14, 15]
]
_____

If there is extra room, leave those spots blank with a 0 filler.
___
# Ordering numbers 1-5 in a [4, 3] space.

order_people([4, 3], 5) ➞ [
  [1, 2, 3],
  [0, 5, 4],
  [0, 0, 0],
  [0, 0, 0]
]
_____

If there are too many people for the given dimensions, return "overcrowded".
___
order_people([4, 3], 20) ➞ "overcrowded"
_____



[Examples]

___
order_people([3, 3], 8) ➞ [
  [1, 2, 3],
  [6, 5, 4],
  [7, 8, 0]
]

order_people([2, 4], 5) ➞ [
  [1, 2, 3, 4],
  [0, 0, 0, 5]
]

order_people([2, 4], 10) ➞ "overcrowded"
_____



[Notes]

___
*) Always start the ordering on the upper-left corner.
*) If the S-shape concept doesn't make sense, try writing down some of these examples on a piece of paper and tracing a pencil through the numbers in order.
___



[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Split List Into Chunks
https://www.delftstack.com/howto/python/python-split-list-into-chunks/
A Python list can be divided into different chunks of equal sizes. It can be done by using user-defined functions, list comprehension, itertools, lambda, lambda and isl …
_________

"""
#Your code should go here:

