"""
####  Free Range  ####

Create a function which converts an ordered number list into a list of ranges (represented as strings). Note how some lists have some numbers missing.


[Examples]

___
numbers_to_ranges([1, 2, 3, 4, 5]) ➞ ["1-5"]

numbers_to_ranges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]

numbers_to_ranges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]

numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]
_____



[Notes]

___
*) If there are no numbers consecutive to a number in the list, represent it as only the string version of that number (see example #4).
*) Return an empty list if the given list is empty.
___



[arrays] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Append
https://towardsdatascience.com/append-in-python-41c37453400#:~:text=The%20append()%20method%20in,the%20list%20increases%20by%20one.
When choosing a collection type, it is useful to understand the properties of each type and choosing the most appropriate type for a particular data set.
_________

"""
#Your code should go here:

