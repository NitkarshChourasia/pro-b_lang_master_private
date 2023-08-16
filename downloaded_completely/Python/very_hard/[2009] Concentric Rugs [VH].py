"""
####  Concentric Rugs  ####

Create a function that takes in parameter n and generates an n x n (where n is odd) concentric rug.
The center of a concentric rug is 0, and the rug "fans-out", as show in the examples below.


[Examples]

___
generate_rug(1) ➞ [
  [0]
]

generate_rug(3) ➞ [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]

generate_rug(5) ➞ [
  [2, 2, 2, 2, 2],
  [2, 1, 1, 1, 2],
  [2, 1, 0, 1, 2],
  [2, 1, 1, 1, 2],
  [2, 2, 2, 2, 2]
]

generate_rug(7) ➞ [
  [3, 3, 3, 3, 3, 3, 3],
  [3, 2, 2, 2, 2, 2, 3],
  [3, 2, 1, 1, 1, 2, 3],
  [3, 2, 1, 0, 1, 2, 3],
  [3, 2, 1, 1, 1, 2, 3],
  [3, 2, 2, 2, 2, 2, 3],
  [3, 3, 3, 3, 3, 3, 3]
]
_____



[Notes]

___
*) n >= 0.
*) Always increment by 1 each "layer" outwards you travel.
___



[arrays] [functional_programming] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Python map() function
https://www.geeksforgeeks.org/python-map-function/
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.
_________

"""
#Your code should go here:

