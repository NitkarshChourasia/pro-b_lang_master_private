"""
####  Postman Harry  ####

Harry is a postman. He's got a post office with a size of n*m(a matrix / 2D list). Each slot at the 2D list represents the number of letters in that spot. Harry can only go right and down. He starts at (0, 0), and ends at (n-1, m-1). n represents the height, and m the length. Return the maximum amount of letters he can pick up. He can only pick up letters if he is on that spot.


[Examples]

___
harry([[5, 2], [5, 2]]) ➞ 12
# (5+5+2)


harry([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15]
]) ➞ 72
# (1+6+11+12+13+14+15)


harry([[]]) ➞ -1
_____



[Notes]

Like you saw in example 3, if the matrix is empty, return -1.


[arrays] [logic] [math] 



-------------------------------------------------------------------
[Resources]
_________
zip() Function
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
_________
_________
max() Function
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.
_________

"""
#Your code should go here:

