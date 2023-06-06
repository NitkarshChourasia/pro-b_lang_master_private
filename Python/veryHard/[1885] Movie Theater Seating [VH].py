"""
####  Movie Theater Seating  ####

A group of n friends are going to see a movie. They would like to find a spot where they can sit next to each other in the same row. A movie theater's seat layout can be represented as a 2-D matrix, where 0s represent empty seats and 1s represent taken seats.
___
[[1, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 0, 1],
[1, 1, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 0, 0, 0]]
_____

Create a function that, given a seat layout and the number of friends n, returns the number of available spots for all n friends to sit together. In the above example, if n = 3, there would be 2 spots (the first row and last row).


[Examples]

___
group_seats([
  [1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0],
  [0, 0, 1, 1, 1, 1, 1],
  [1, 0, 1, 1, 0, 0, 1],
  [1, 1, 1, 0, 1, 0, 1],
  [0, 1, 1, 1, 1, 0, 0]
], 2) ➞ 3

group_seats([
  [1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 0, 0, 0, 0],
], 4) ➞ 2
_____



[Notes]

Multiple free arrangements that overlap still count as distinct arrangements (see example #2).


[arrays] [higher_order_functions] [loops] 



-------------------------------------------------------------------
[Resources]
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum.
_________
_________
Count Overlapping Substring in a Given String
https://www.geeksforgeeks.org/python-count-overlapping-substring-in-a-given-string/
Given a string and a sub-string, the task is to get the count of overlapping substring from the given string.
_________
_________
String Slicing
https://www.geeksforgeeks.org/string-slicing-in-python/
Is about obtaining a sub-string from the given string by slicing it respectively from start to end.
_________

"""
#Your code should go here:

