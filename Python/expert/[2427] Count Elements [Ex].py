"""
####  Count Elements  ####

Write a function that counts the number of separate elements in the region.


[Input]

A rectangular matrix, list of lists, with zero/one in each cell. A connected element is a collection of ones that share the border via an edge. Separate elements do not touch each other even via a corner. The elements don’t have holes.


[Output]

The number of separate elements.


[Examples]

___
region = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 1, 1, 0],
  [0, 1, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 1, 1, 0],
  [0, 1, 1, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0],
]

count_shapes(region) ➞ 3
_____



[Notes]

___
*) How to locate different elements can be learned from the Chain Reaction series.
*) It takes up to 4 seconds to assemble the input regions in the tests. Solutions with O(rows * columns) complexity allow us to pass the tests in the remaining 8 seconds (3.5 seconds is enough).
*) The main goal of this challenge is to come up with an efficient solution.
___



[algorithms] [arrays] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
Depth-first search
https://en.wikipedia.org/wiki/Depth-first_search
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node …
_________

"""
#Your code should go here:

