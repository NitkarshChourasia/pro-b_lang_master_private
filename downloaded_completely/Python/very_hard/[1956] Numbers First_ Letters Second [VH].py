"""
####  Numbers First, Letters Second  ####

Write a function that sorts list while keeping the list structure. Numbers should be first then letters both in ascending order.


[Examples]

___
num_then_char([
  [1, 2, 4, 3, "a", "b"],
  [6, "c", 5], [7, "d"],
  ["f", "e", 8]
]) ➞ [
  [1, 2, 3, 4, 5, 6],
  [7, 8, "a"],
  ["b", "c"], ["d", "e", "f"]
]

num_then_char([
  [1, 2, 4.4, "f", "a", "b"],
  [0], [0.5, "d","X",3,"s"],
  ["f", "e", 8],
  ["p","Y","Z"],
  [12,18]
]) ➞ [
  [0, 0.5, 1, 2, 3, 4.4],
  [8],
  [12, 18, "X", "Y", "Z"],
  ["a", "b", "d"],
  ["e", "f", "f"],
  ["p", "s"]
]
_____



[Notes]

Test cases will contain integer and float numbers and single letters.


[arrays] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
len() Function
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
List Methods & Functions
http://www.python-ds.com/python-3-list-methods
Extends the list by appending all the items from the iterable. This allows you to join two lists together. This method is equivalent to a[len(a):] = iterable.
_________
_________
sorted() Function
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
Check if Variable is a String
https://www.askpython.com/python/examples/python-check-if-variable-is-a-string
Since Python does not support static type checking (i.e type checking at compile type), if you ever want to check if a Python variable or object is a String or not; we …
_________

"""
#Your code should go here:

