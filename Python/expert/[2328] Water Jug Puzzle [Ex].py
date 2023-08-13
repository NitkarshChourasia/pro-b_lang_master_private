"""
####  Water Jug Puzzle  ####

Given a set of 3 jugs of water that have capacities of a, b, and c liters, find the minimum number of operations performed before each jug has x, y, and z liters. Only jug C will start completely filled.
An operation is any of the following: A jug is emptied, a jug is filled, or water is poured from one jug to another until one of the jugs is either empty or full.
For example, jugs "A", "B", and "C" with capacities of 3, 5, and 8, where jugs "A" and "B" start empty and "C" has the full 8, require 2 operations to reach the state of 0, 3, and 5 liters in the jugs.
Create a function that, given an array of jug capacities [A, B, C] and an goal state array [x, y, z], returns the minimum number of operations needed to reach the goal state. If the inputs are invalid or there is no solution, return "No solution."


[Examples]

___
waterjug([3, 5, 8], [0, 3, 5]) ➞ 2

waterjug([1, 3, 4],  [0, 2, 2]) ➞ 3

waterjug([8, 17, 20], [0, 10, 10]) ➞ 9

waterjug([4, 17, 22], [2, 5, 15]) ➞ "No solution."

waterjug([3, 5, 8], [0, 0, 9]) ➞ "No solution."
_____



[Notes]

___
*) The amount of water in a jug can never exceed the capacity of that jug.
*) The total liters in the goal state must be equal to the capacity of jug "C".
___



[algorithms] [conditions] [data_structures] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Breadth-first Search
https://en.wikipedia.org/wiki/Breadth-first_search
Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, som …
_________
_________
Hint On DFS
http://stackoverflow.com/questions/2137731/depth-first-search-in-python#2137789
The (a) solution to this problem follows a general pattern. If you can formulate this problem as a depth first search, you can implement the pseudocode in this link.
_________

"""
#Your code should go here:

