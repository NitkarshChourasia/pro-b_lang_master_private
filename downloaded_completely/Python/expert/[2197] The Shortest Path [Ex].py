"""
####  The Shortest Path  ####

Given a rectangular grid of m by n spaces, signaled by 0s, and a number of points, signaled by 1, 2, 3..., return the number of moves for the shortest path that starts at 1 and goes over all the other points in ascending order.


[Examples]

___
shortest_path([
  ("001"),
  ("002"),
  ("003")
]) ➞ 2

shortest_path([
  ("00000"),
  ("01006"),
  ("02000"),
  ("30050"),
  ("00004")
]) ➞ 13

shortest_path([
  ("00020000"),
  ("01000000")
]) ➞ 3
_____



[Notes]

___
*) Only horizontal and vertical movements are allowed.
*) All movements from one place to an adjacent one count as 1 regardless of direction.
*) The points range from 1 to at most 9 with no repeating or missing digits.
___



[arrays] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Enumerate
https://book.pythontips.com/en/latest/enumerate.html
Is a built-in function of Python. Its usefulness can not be summarized in a single line. Yet most of the newcomers and even some advanced programmers are unaware of it. …
_________

"""
#Your code should go here:

