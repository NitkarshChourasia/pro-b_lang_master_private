"""
####  Car Park Exit  ####

You are stuck in a multi-storey car parking lot. Your task is to exit the carpark using only the staircases. Exit is always at the bottom right of the ground floor.
Create a function that takes a two-dimensional list where:

... and returns a list of the quickest route out of the carpark.
___
arr = [
  [1, 0, 0, 0, 2],
  [0, 0, 0, 0, 0]
]

# Starting from 2, move to left 4 times = "L4"
# Go down from stairs 1 step = "D1"
# Move to right 4 times to exit from right bottom corner = "R4"

result = ["L4", "D1", "R4"]
_____

See the below examples to better understand:


[Examples]

___
parking_exit([
  [1, 0, 0, 0, 2],
  [0, 0, 0, 0, 0]
]) ➞ ["L4", "D1", "R4"]
_____

___
parking_exit([
  [2, 0, 0, 1, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0]
]) ➞ ["R3", "D2", "R1"]

# Starting from 2, move to right 3 times = "R3"
# Go down from stairs 2 steps = "D2"
# Move to right 1 step to exit from right bottom corner = "R1"
_____

___
parking_exit([[0, 0, 0, 0, 2]]) ➞ []
# You are already at right bottom corner.
_____



[Notes]

N/A


[arrays] [games] [logic] 



-------------------------------------------------------------------
[Resources]
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
Is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other programming langua …
_________

"""
#Your code should go here:

