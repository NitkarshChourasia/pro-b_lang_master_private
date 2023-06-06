"""
####  Checkerboard Generator  ####

Create a checker board generator, which takes as inputs n and 2 elements to generate an n x n checkerboard with those two elements as alternating squares.


[Examples]

___
checker_board(2, 7, 6) ➞ [
  [7, 6],
  [6, 7]
]

checker_board(3, "A", "B") ➞ [
  ["A", "B", "A"],
  ["B", "A", "B"],
  ["A", "B", "A"]
]

checker_board(4, "c", "d") ➞ [
  ["c", "d", "c", "d"],
  ["d", "c", "d", "c"],
  ["c", "d", "c", "d"],
  ["d", "c", "d", "c"]
]

checker_board(4, "c", "c") ➞ "invalid"
_____



[Notes]

___
*) Both elements can be either strings or integers.
*) The first element should be on the upper left corner of the checker board. e.g. "c", not "d" should be element [0][0] for example 3.
*) Return "invalid" if both inputs are identical (see example 4).
___



[arrays] [games] [higher_order_functions] 



-------------------------------------------------------------------
[Resources]
_________
range() Type
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
Ternary Operator
https://www.geeksforgeeks.org/ternary-operator-in-python/
Are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply allows to test a condition in a single …
_________
_________
Indexing and Slicing for Lists, Tuples, Strings, and other Sequential Types
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
List is arguably the most useful and ubiquitous type in Python. One of the reasons it’s so handy is Python slice notation. In short, slicing is a flexible tool to build …
_________

"""
#Your code should go here:

