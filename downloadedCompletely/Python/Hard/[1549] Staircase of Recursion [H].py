"""
####  Staircase of Recursion  ####

Write a function that returns the number of ways a person can climb n stairs, where the person may only climb 1 or 2 steps at a time.
To illustrate, if n = 4 there are 5 ways to climb:
___
[1, 1, 1, 1]
[2, 1, 1]
[1, 2, 1]
[1, 1, 2]
[2, 2]
_____



[Examples]

___
ways_to_climb(1) ➞ 1

ways_to_climb(2) ➞ 2

ways_to_climb(5) ➞ 8
_____



[Notes]

A staircase of height 0 should return 1.


[algorithms] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Fibonacci Numbers
https://mortada.net/fibonacci-numbers-in-python.html
It is possible to derive a general formula for Fn without computing all the previous numbers in the sequence. If a gemetric series (i.e. a series with a constant ratio …
_________
_________
How many distinct ways to climb stairs in 1 or 2 steps at a time?
https://math.stackexchange.com/questions/789804/how-many-distinct-ways-to-climb-stairs-in-1-or-2-steps-at-a-time
I came across an interesting puzzle: You are climbing a stair case. It takes 𝑛 steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many dist …
_________
_________
Count Ways to Reach the Nth Stair
https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the per …
_________

"""
#Your code should go here:

