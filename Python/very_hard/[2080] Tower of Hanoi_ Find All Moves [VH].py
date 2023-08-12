"""
####  Tower of Hanoi: Find All Moves  ####

You have three rods numbered from 1 to 3. A few disks of different sizes are strung on the first rod. Disks are ranged by size from the smallest one on top to the largest at the bottom.
Create a function that shows how to transfer the entire stack of n disks from first to the third rod, obeying the following rules:

The function should return a list of moves. Each move is represented by a tuple of two numbers: the number of the rod from which to take the disk, and the number of the rod where to put it.


[Examples]

___
hanoi(1) ➞ [(1, 3)]

hanoi(2) ➞ [(1, 2), (1, 3), (2, 3)]

hanoi(4) ➞ [(1, 2), (1, 3), (2, 3), (1, 2), (3, 1), (3, 2), (1, 2), (1, 3), (2, 3), (2, 1), (3, 1), (2, 3), (1, 2), (1, 3), (2, 3)]
_____



[Notes]

___
*) Function have to return an empty list if n == 0
*) The best way to solve this problem is to use recursion.
___




[logic] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
Tower of Hanoi
https://www.tutorialspoint.com/data_structures_algorithms/tower_of_hanoi.htm
Is a mathematical puzzle which consists of three towers (pegs) and more than one rings is as depicted...
_________

"""
#Your code should go here:

