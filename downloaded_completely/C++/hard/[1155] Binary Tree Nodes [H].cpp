/*
####  Binary Tree Nodes  ####

We have two arrays N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

Write a function to find the node type of the node within this Binary Tree, ordered by the value of the node. Output one of the following:
___
*) Root: If node is root node.
*) Leaf: If node is leaf node.
*) Inner: If node is neither root nor leaf node.
*) Not exist: If node not exist.
___

___
nodeType([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5) ➞ "Root"

nodeType([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 6) ➞ "Leaf"

nodeType([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2) ➞ "Inner"

nodeType([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10) ➞ "Not exist"
_____




[Notes]

All values of N array are unique.


[algorithms] [arrays] [conditions] [interview] 



-------------------------------------------------------------------
[Resources]
_________
Binary Tree Data Structure
https://www.geeksforgeeks.org/binary-tree-data-structure/
A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and …
_________
_________
Edabit - Binary Tree Nodes
https://www.youtube.com/watch?v=HXJHQjjXviI&feature=youtu.be
This problem involves working with a Binary Tree represented in an array format. We find when a given node is a root, inner, or leaf node.
_________

*/
//Your code should go here:

