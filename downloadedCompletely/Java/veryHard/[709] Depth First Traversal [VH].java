/*
####  Depth First Traversal  ####

A depth-first search of a graph is one way of traversing the nodes of the graph along edges. When DFS reaches a node for the first time, it marks the node as being reached and then checks its neighbors. Once all of a node's neighbors have been checked, the node is marked as done. If the starting node is marked as done before all nodes of a graph are reached, an unmarked node is selected and the search continues. The order in which nodes are originally reached provides useful information about the graph. Another useful source of information is the order in which nodes are marked as done. This order is different.
The following are examples of graphs along with the order in which nodes are visited using DFS.








[Instructions]

Given a graph represented by an adjacency matrix, perform a depth-first search. When multiple options exist for which node to move to (either selecting a starting node or when a node has multiple neighbors), move to the lowest numbered, unvisited node.
Your program will output a 2-dimensional array with two rows. The first row will record the order in which nodes are initially reached while the second row indicates the order in which the nodes are marked as done. The columns represent the nodes, and the numbers indicate the order (beginning with 1) in which the nodes are originally visited/marked as done.


[Example #1]


___
{
  {0,1,1,0,0,0},
  {1,0,0,1,0,0},
  {1,0,0,0,1,1},
  {0,1,0,0,0,0},
  {0,0,1,0,0,0},
  {0,0,1,0,0,0}
} ➞ {
  {1,2,4,3,5,6},
  {6,2,5,1,3,4}
}
_____



[Example #2]


___
{
  {0,1,1,1,0,1},
  {1,0,0,1,1,0},
  {1,0,0,0,0,1},
  {1,1,0,0,1,0},
  {0,1,0,1,0,0},
  {1,0,1,0,0,0}
} ➞ {
  {1,2,5,3,4,6},
  {6,3,5,2,1,4}
}
_____



[Example #3]


___
{
  {0,1,1,0,0,0,0},
  {1,0,0,0,0,1,0},
  {1,0,0,0,0,1,0},
  {0,0,0,0,1,0,1},
  {0,0,0,1,0,0,1},
  {0,1,1,0,0,0,0},
  {0,0,0,1,1,0,0}
} ➞ {
  {1,2,4,5,6,3,7},
  {4,3,1,7,6,2,5}
}
_____



[Notes]

___
*) Graphs contain between 1 and 1000 nodes.
*) Time limit: 100 milliseconds.
___



[algorithms] [data_structures] [math] 



-------------------------------------------------------------------
[Resources]
_________
Depth-first search
https://en.wikipedia.org/wiki/Depth-first_search
Is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the …
_________

*/
//Your code should go here:

