"""
####  Directionally Challenged  ####

Suppose you are directionally challenged, and get lost easily. As a result, sometimes you walk in circles or make U-turns. You might take a sub-optimal route. Create a function that returns the difference in length between your path and the optimal path. Both paths reach the same destination.
You start at (0,0) and reach your destination by the end of the input list.
A demonstration:
___
Your route: ["N", "S", "E", "W", "E", "E", "E", "N"]  // 8
Optimal route: ["E", "E", "E", "N"] (or ["N", "E", "E", "E"], etc.) // 4
# Difference in length: 8 - 4 = 4

# Explanation: Your "S" cancels out your "N" and your "W" cancels out your "E" leaving you back at (0,0)
_____



[Examples]

___
route_diff(["N", "E", "S", "W"]) ➞ 4
# You"ve just walked in a circle! You are back at the origin. Your optimal path was `[]`.

route_diff(["N", "N", "N", "E", "N", "E"]) ➞ 0
# No improvements here!

route_diff(["N", "S", "N", "S", "E", "W", "E", "E"]) ➞ 6
_____



[Notes]

Remember that a N cancels out a S, and an E cancels out a W.


[arrays] [control_flow] 



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.geeksforgeeks.org/python-string-count/
Returns an integer that denotes number of times a substring occurs in a given string. Below is the Python implementation of the count() method without optional parameters.
_________

"""
#Your code should go here:

