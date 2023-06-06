/*
####  Adjacent Nodes  ####

A graph is a set of nodes along with a set of edges connecting the nodes.

Graphs can be directed or undirected. In a directed graph, each edge has a direction whereas, in an undirected graph, edges do not have direction. The graph above is an undirected graph.
Two nodes in a graph are adjacent if there is an edge between them. In the above example, nodes 0 and 1 are adjacent, but 0 and 2 are not adjacent.
We can encode graphs using an adjacency matrix. An adjacency matrix for a graph with "n" nodes is an "n * n" matrix where the entry at row "i" and column "j" is a 0 if nodes "i" and "j" are not adjacent, and 1 if nodes "i" and "j" are adjacent.
In the example above, the adjacency matrix looks like:
___
{
  { 0, 1, 0, 0 },
  { 1, 0, 1, 1 },
  { 0, 1, 0, 1 },
  { 0, 1, 1, 0 }
}
_____

Your task is to determine if two nodes are adjacent in an undirected graph when given the adjacency matrix and the two nodes.


[Examples]


Adjacency Matrix:
___
{
  { 0, 1, 0, 0 },
  { 1, 0, 1, 1 },
  { 0, 1, 0, 1 },
  { 0, 1, 1, 0 }
}
_____

___
*) Nodes 0,1 should return true.
*) Nodes 0,2 should return false.
___


___
{
  { 0, 1, 0, 1, 1 },
  { 1, 0, 1, 0, 0 },
  { 0, 1, 0, 1, 0 },
  { 1, 0, 1, 0, 1 },
  { 1, 0, 0, 1, 0 }
}
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
https://stackoverflow.com/questions/349446/adjacency-matrix-in-java-or-c-to-find-connected-nodes
You can implement this using a 2-dimensional array of booleans. So, if node i is connected to node j, then myarray[i][j] would be true. If your edges are not directiona …
_________
_________
Examples of Adjacency Matrices
https://www.bookofproofs.org/branches/examples-of-adjacency-matrices/
Explains how an adjacency matrix for nodes works.
_________
_________
Graph Theory
https://en.wikipedia.org/wiki/Graph_theory
Is the study of graphs, which are mathematical structures used to model pairwise relations between objects. A graph in this context is made up of vertices (also called …
_________

*/
//Your code should go here:

