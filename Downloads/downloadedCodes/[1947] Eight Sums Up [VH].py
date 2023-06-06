"""
####  Eight Sums Up  ####

Create a function that gets every pair of numbers from an array that sums up to eight and returns it as an array of pairs (sorted ascendingly). See the following examples for more details.


[Examples]

___
sums_up([1, 2, 3, 4, 5]) ➞ {"pairs": [[3, 5]]}

sums_up([1, 2, 3, 7, 9]) ➞ {"pairs": [[1, 7]]}

sums_up([10, 9, 7, 2, 8]) ➞ {"pairs": []}

sums_up([1, 6, 5, 4, 8, 2, 3, 7]) ➞ {"pairs": [[2, 6], [3, 5], [1, 7]]}
# [6, 2] first to complete the cycle (to sum up to 8)
# [5, 3] follows
# [1, 7] lastly
# the pair that completes the cycle is always found on the left
# [2, 6], [3, 5], [1, 7] sorted according to cycle completeness, then pair-wise.
_____



[Notes]

___
*) Return a dictionary with the key "pairs" and a value of the array.
*) Remember the idea of "completes the cycle first" when getting the sort order of the pairs.
*) Only unique numbers are present in the array.
*) Return an empty array if nothing sums up to eight.
___



[algorithms] [arrays] [numbers] [objects] 



-------------------------------------------------------------------
[Resources]
_________
When to Use a List Comprehension in Python
https://realpython.com/list-comprehension-python/
Python list comprehensions make it easy to create lists while performing sophisticated filtering, mapping, and conditional logic on their members. In this tutorial, you …
_________

"""
#Your code should go here:

