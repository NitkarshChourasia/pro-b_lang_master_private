/*
####  Generic Binary Tree  ####

A Binary Search Tree is a node-based tree data structure which has the following properties:
___
*) The left subtree of a node contains only nodes with data less than the node's data.
*) The right subtree of a node contains only nodes with data greater than the node’s data.
*) The left and right subtree each must also be a binary search tree (or null).
___

Create a generic class, Node<T> that can manage a binary search tree containing data of any type T which implements the IComparable interface. (The IComparable interface has a single method CompareTo(object other) which returns -1, 0, or 1 depending on whether other is greater than, equal to, or less than the implementing object). This means that instead of using <, == or > you must use CompareTo() to determine whether one object is less than or greater than another.
A skeleton of the class is provided for you in the Code tab and has the following members:
___
*) public Node(T data): A constructor with the data to be stored in the node.
*) public T Data: A property containing the data held in the node.
*) public Node<T> Left: A property returning the next node in the tree which is less than this node (or null if this node is the lowest).
*) public Node<T> Right: A property returning the next node in the tree which is greater than this node (or null if this node is the highest).
*) public IEnumerable<T> GetTreeData(): A method that returns an enumerable collection of objects of type T stored in the tree whose root is this Node in least to greatest order.
___



[Examples]

___
var root = new Node<int>(10) ➞ 10 is the root of the tree (first node in the tree)
root.Insert(5) ➞ a new node is created and added to the Left node of `root`
root.Insert(11) ➞ a new node is created and added to the Right node of  `root`
root.Insert(3) ➞ a new node is created and added to the Left node of `5`
root.Insert(6) ➞ a new node is created and added to the Right node of `root`
root.GetTreeData() ➞ [3, 5, 6, 10, 11]
root.Data ➞ 10
root.Left.Data ➞ 5
root.Right.Data ➞ 11
_____



[Notes]

___
*) Tests include multiple data types all of which implement the IComparable interface.
*) Only valid data will be used to test the class and there will be no duplicates (in other words you do not need to cater to CompareTo() == 0).
*) Based on a Python challenge published by @Gxsor.
___



[algorithms] [classes] [data_structures] [interview] 



-------------------------------------------------------------------
[Resources]
_________
Generic Classes
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/generic-classes
Encapsulate operations that are not specific to a particular data type. The most common use for generic classes is with collections like linked lists, hash tables, stac …
_________
_________
Binary Search Tree
https://www.geeksforgeeks.org/binary-search-tree-data-structure/
A node-based binary tree data structure which has the following properties: The left subtree of a node contains only nodes with keys lesser than the node’s key. The rig …
_________

*/
//Your code should go here:

