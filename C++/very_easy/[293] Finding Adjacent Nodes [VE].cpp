/*
####  Finding Adjacent Nodes  ####

A graph is a set of nodes and edges that connect those nodes.

There are two types of graphs; directed and undirected. In an undirected graph, the edges between nodes have no particular direction (like a two-way street) whereas in a directed graph, each edge has a direction associated with it (like a one-way street).
For two nodes in a graph to be considered adjacent to one another, there must be an edge between them. In the example given above, nodes 0 and 1 are adjacent, but nodes 0 and 2 are not.
We can encode graphs using an adjacency matrix. An adjacency matrix for a graph with "n" nodes is an "n * n" matrix where the entry at row "i" and column "j" is a 0 if nodes "i" and "j" are not adjacent, and 1 if nodes "i" and "j" are adjacent.
For the example above, the adjacency matrix would be as follows:
___
[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]
_____

A one indicates that a connection is true and a zero indicates a connection is false.
Here is how the above model might be written out:
___
*) On the first row, node 0 does not connect to itself, but it does connect to node 1. It does not connect to node 2 or node 3. The row is written as 0, 1, 0, 0.
*) On the second row, node 1 connects to node 0, node 2 and node 3, but it does not connect to itself. The row is written as 1, 0, 1, 1.
*) On the third row, node 2 does not connect to node 0, but it does connect to node 1, does not connect to itself, and it does connect to node 3. The row is written as 0, 1, 0, 1
*) On the fourth row, node 3 does not connect to node 0, but it does connect to node 1 and node 2. It does not connect to itself. The row is written as 0, 1, 1, 0.
___

Your task is to determine if two nodes are adjacent in an undirected graph when given the adjacency matrix and the two nodes.


[Examples]


Adjacency Matrix:
___
[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]
_____

___
*) Nodes 0,1 should return true.
*) Nodes 0,2 should return false.
___


___
[
  [ 0, 1, 0, 1, 1 ],
  [ 1, 0, 1, 0, 0 ],
  [ 0, 1, 0, 1, 0 ],
  [ 1, 0, 1, 0, 1 ],
  [ 1, 0, 0, 1, 0 ]
]
_____

___
*) Nodes 0,3 should return true.
*) Nodes 1,4 should return false.
___



[Notes]

___
*) Graphs may have between 0 and 25,000 nodes.
*) Time Limit: 100 milliseconds.
___



[algorithms] [arrays] [data_structures] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Adjacency Matrix
https://mathworld.wolfram.com/AdjacencyMatrix.html
Is a matrix with rows and columns labeled by graph vertices, with a 1 or 0 in position (v_i,v_j) according to whether v_i and v_j are adjacent or not. For a simple grap …
_________
_________
Graph Theory
https://en.wikipedia.org/wiki/Graph_theory
Is the study of graphs, which are mathematical structures used to model pairwise relations between objects. A graph in this context is made up of vertices (also called …
_________
_________
Adjacency Matrix in Java or C++ to Find Connected Nodes
https://stackoverflow.com/questions/349446/adjacency-matrix-in-java-or-c-to-find-connected-nodes
I am given a problem where I have been given N nodes in a graph that are interconnected to each other then given a matrix which lists down a node being connected to ano …
_________
_________
Examples of Adjacency Matrices
https://www.bookofproofs.org/branches/examples-of-adjacency-matrices/
The following figure shows a digraph D with 6 vertices and some edges. This digraph has the adjacency matrix. Please note that an adjacency matrix of a digraph is …
_________

*/
//Your code should go here:

