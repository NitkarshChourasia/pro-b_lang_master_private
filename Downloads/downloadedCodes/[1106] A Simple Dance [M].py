"""
####  A Simple Dance  ####

You will be given a list of dancing couples, with the woman first and man second, as well as a parameter "men" or "women".
___
*) If the parameter is "men", the men reverse their positions (first moves to last, last moves to first, etc), while women keep their positions.
*) If the parameter is "women", the women reverse their positions, while men keep their positions.
___



[Examples]

___
dance([
  [Ana, Bob],
  [Amy, Josh],
  [Lisa, Tim]
], men) ➞ [
  [Ana, Tim],
  [Amy, Josh],
  [Lisa, Bob]
]

dance([
  [Ana, Bob],
  [Amy, Josh],
  [Lisa, Tim]
], women) ➞ [
  [Lisa, Bob],
  [Amy, Josh],
  [Ana, Tim]
]
_____



[Notes]

Input lists will always be the same length.


[arrays] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
zip() Method
https://www.w3schools.com/python/ref_func_zip.asp
Returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator a …
_________
_________
How to reverse a list in Python?
https://www.quora.com/How-can-I-reverse-a-list-in-python
Reversing a list in Python is very easy. There are number of ways to perform this operation. Let’s see it 1 by 1 (In 4 ways) => 1) A direct way of reversing a list(It …
_________

"""
#Your code should go here:

