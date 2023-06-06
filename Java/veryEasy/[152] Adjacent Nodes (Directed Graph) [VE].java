/*
####  Adjacent Nodes (Directed Graph)  ####

A directed graph is like an undirected graph except that edges have direction. Each edge goes from a source node to a target node.


[Examples]


Here, node 0 is adjacent to node 1, but node 1 is not adjacent to node 0, for example. Here is what the graph above would look like if it were undirected:

In directed graphs, the edge direction matters. For example, the following two graphs are different:


With undirected graphs, the adjacency matrix is symmetric about the main diagonal, but in a directed graph, it is not always the case. In particular, a 1 in row i and column j indicates that there is an edge from i to j.

The following graph would have the following adjacency matrix:
___
{
  {0, 1, 1, 0, 0},
  {0, 0, 0, 0, 0},
  {0, 1, 0, 0, 0},
  {0, 0, 1, 0, 1},
  {1, 0, 0, 0, 0}
}
_____

We can see that node 1 has no edges coming out of it. That is reflected by its row being all zeros. A node with no edges going into it would have a column of all zeros.

Your task is to, given the adjacency matrix of a directed graph and two nodes, determine whether or not the first node is adjacent to the second node.

___
*) Graphs may have between 0 and 25000 nodes.
*) Time limit: 100 milliseconds.
___



[algorithms] [arrays] [math] 



-------------------------------------------------------------------
[Resources]
_________
Graphs
https://www.baeldung.com/java-graphs
In this tutorial, we'll understand the basic concepts of a graph as a data structure.
_________

*/
//Your code should go here:

