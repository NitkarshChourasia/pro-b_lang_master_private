"""
####  Mountains or Valleys  ####

A mountain is a list with exactly one peak.
___
*) All numbers to the left of the peak are increasing.
*) All numbers to the right of the peak are decreasing.
*) The peak CANNOT be on the boundary.
___

A valley is a list with exactly one trough.
___
*) All numbers to the left of the trough are decreasing.
*) All numbers to the right of the trough are increasing.
*) The trough CANNOT be on the boundary.
___

Some examples of mountains and valleys:
___
Mountain A:  [1, 3, 5, 4, 3, 2]   # 5 is the peak
Mountain B:  [-1, 0, -1]   # 0 is the peak
Mountain B:  [-1, -1, 0, -1, -1]   # 0 is the peak (plateau on both sides is okay)

Valley A: [10, 9, 8, 7, 2, 3, 4, 5]   # 2 is the trough
Valley B: [350, 100, 200, 400, 700]  # 100 is the trough
_____

Neither mountains nor valleys:
___
Landscape A: [1, 2, 3, 2, 4, 1]  # 2 peaks (3, 4), not 1
Landscape B: [5, 4, 3, 2, 1]  # Peak cannot be a boundary element
Landscape B: [0, -1, -1, 0, -1, -1]  # 2 peaks (0)
_____

Based on the rules above, write a function that takes in a list and returns either "mountain", "valley", or "neither".


[Examples]

___
landscape_type([3, 4, 5, 4, 3]) ➞ "mountain"

landscape_type([9, 7, 3, 1, 2, 4]) ➞ "valley"

landscape_type([9, 8, 9]) ➞ "valley"

landscape_type([9, 8, 9, 8]) ➞ "neither"
_____



[Notes]

___
*) A peak is not exactly the same as the max of a list. The max is a unique number, but a list may have multiple peaks. However, if there exists only one peak in a list, then it is true that the peak = max.
*) See comments for a hint.
___



[arrays] [functional_programming] [higher_order_functions] 



-------------------------------------------------------------------
[Resources]
_________
Max() function
https://www.w3schools.com/python/ref_func_max.asp
returns the item with the highest value, or the item with the highest value in an iterable. If the values are strings, an alphabetical comparison is done.
_________
_________
Min() function
https://www.w3schools.com/python/ref_func_min.asp
Used to retrieve the minimum value in a list or from multiple arguments.
_________

"""
#Your code should go here:

