"""
####  Diagonal Matrices  ####

Write a function that diagonally orders numbers in a n x n matrix, depending on which of the four corners you originate from: upper-left (ul), upper-right (ur), lower-left (ll), lower-right (lr).


[Examples]

___
diagonalize(3, "ul") ➞ [
  [0, 1, 2],
  [1, 2, 3],
  [2, 3, 4]
]

diagonalize(4, "ur") ➞ [
  [3, 2, 1, 0],
  [4, 3, 2, 1],
  [5, 4, 3, 2],
  [6, 5, 4, 3]
]

diagonalize(3, "ll") ➞ [
  [2, 3, 4],
  [1, 2, 3],
  [0, 1, 2]
]

diagonalize(5, "lr") ➞ [
  [8, 7, 6, 5, 4],
  [7, 6, 5, 4, 3],
  [6, 5, 4, 3, 2],
  [5, 4, 3, 2, 1],
  [4, 3, 2, 1, 0]
]
_____



[Notes]

N/A


[arrays] [functional_programming] 



-------------------------------------------------------------------
[Resources]
_________
List Slicing
https://www.learnbyexample.org/python-list-slicing/
To access a range of items in a list, you need to slice a list. One way to do this is to use the simple slicing operator...
_________

"""
#Your code should go here:

