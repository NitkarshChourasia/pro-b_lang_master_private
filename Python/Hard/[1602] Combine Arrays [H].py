"""
####  Combine Arrays  ####

Create a function that takes three lists and returns one list where all passed arrays are combined into nested lists.
These lists should be combined based on indexes: the first nested list should contain only the items on index 0, the second list on index 1, and so on.
If any list contains fewer items than necessary, supplement the missing item with "*".


[Examples]

___
combine_lists([False, "False"], ["True", True, "bool"], ["None", "undefined"]) ➞ [[False, "True", "None"], ["False", True, "undefined"], ["*", "bool", "*"]]

combine_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]) ➞ [[1, 4, 7], [2, 5,  8], [3, 6, 9]]

combine_lists(["Jack", "Joe", "Jill"], ["Stuart", "Sammy", "Silvia"], ["Rick", "Raymond", "Riri"]) ➞ [["Jack", "Stuart", "Rick"], ["Joe", "Sammy",  "Raymond"], ["Jill", "Silvia", "Riri"]]
_____



[Notes]

N/A


[arrays] [data_structures] [loops] 



-------------------------------------------------------------------
[Resources]
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other program …
_________
_________
Making Equal Size Lists in Python
https://stackoverflow.com/questions/43336837/making-equal-size-lists-in-python/43336948
I have 3 different lists of unequal length. I want to append the shorter lists with "X" and make sizes equal to the length of the longest list.
_________

"""
#Your code should go here:

