"""
####  Number of Connected Regions  ####

The function is given a square matrix of relations n by n. Each element is numbered from 0 to n - 1. An element i is directly connected to an element j if relations[i][j] == 1. Element A is connected to element B and element B is connected to C, then A is indirectly connected to C. A region consists of all directly and indirectly connected elements. Find the number of separate regions in the given matrix of relations.


[Examples]

___
n_regions([
  [1, 1, 0], [1, 1, 0], [0, 0, 1]
]) ➞ 2

# Elements 0 and 1 are connected, element 2 is not connected
# to any other. Thus 2 separate regions.
_____

___
n_regions([
  [1, 0, 0], [0, 1, 0], [0, 0, 1]
]) ➞ 3

# The three elements are not connected. Thus 3 regions.
_____

___
n_regions([
  [1, 0, 0, 1],
  [0, 1, 1, 0],
  [0, 1, 1, 1],
  [1, 0, 1, 1]
]) ➞ 1

# Element 0 is connected to 3, 1 and 2 are connected, 3 is
# connected to 2. Thus all are indirectly connected.
# Thus only 1 region.
_____



[Notes]

The relations matrix is symmetric because if i is connected to j, then j is connected to i. Diagonal elements relations[i][i] == 1.


[algorithms] [arrays] [conditions] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Depth-first search
https://en.wikipedia.org/wiki/Depth-first_search
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node …
_________
_________
Breadth-first search
https://en.wikipedia.org/wiki/Breadth-first_search
Breadth-first search (BFS) is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all n …
_________

"""
#Your code should go here:

