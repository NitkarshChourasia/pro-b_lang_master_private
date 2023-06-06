"""
####  The Recursive Staircase Problem  ####

In the Recursive Staircase Problem, your task is to find the number of ways of climbing a staircase of n stairs, with a set s possible steps. The example below shows that if n was 2 and s was { 1, 2 }, the answer would be 2:
___
       _
   _ |2  You could either go from step 0-2 (because the set s contains 2), or
_ | 1    you could go from 0-1-2 (because the set s contains 1, taking one step at a time).
0
_____

More examples below.


[Examples]

___
num_ways(4, { 1, 2 }) ➞ 5

num_ways(3, { 1, 2, 3 }) ➞ 4

num_ways(10, { 1, 2, 3, 4 }) ➞ 401
_____



[Notes]

The more efficient your solution the better. Do not use unecessary recursion as this will mean the program needs far longer to complete the tests.


[conditions] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Count Ways to Reach the N'Th Stair
https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the per …
_________

"""
#Your code should go here:

