/*
####  Plant the Grass  ####

You will be given a matrix representing a field g and two numbers x, y coordinate.
There are three types of possible characters in the matrix:
___
*) x representing a rock.
*) . representing a blank space.
*) + representing a grassed space.
___

You have to simulate grass growing from the position (x, y). Grass can grow in all four directions (up, left, right, down). Grass can only grow on blank spaces and can't go past rocks.
Return the simulated matrix.


[Examples]

___
simulateGrass({
  "xxxxxxx",
  "x.....x",
  "xxxx..x", 
  "x...xxx", 
  "xxxxxxx"
}, 1, 1) ➞ {
  "xxxxxxx",
  "x+++++x",
  "xxxx++x", 
  "x...xxx", 
  "xxxxxxx"
}
_____



[Notes]

N/A


[algorithms] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Depth-first Search
https://en.wikipedia.org/wiki/Depth-first_search
Is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the …
_________

*/
//Your code should go here:

