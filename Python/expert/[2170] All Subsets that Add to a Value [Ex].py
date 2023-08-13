"""
####  All Subsets that Add to a Value  ####

Create a function that returns all sublists in a list that sum to a particular value. Return the sublists in the following order:

The following example will illustrate:
___
get_subsets([-3, -2, -1, 0, 1, 2, 3], 2)
[ # All the subsets below sum to 2.
  [2],
  [-1, 3],
  [0, 2], # Same length: -1 < 0, so [-1, 3] goes before [0, 2]
  [-3, 2, 3],
  [-2, 1, 3],
  [-1, 0, 3],
  [-1, 1, 2],
  [-3, 0, 2, 3],
  [-2, -1, 2, 3],
  [-2, 0, 1, 3], # Same length + same first element: -1 < 0, so [-2, -1, 2, 3] goes before [-2, 0, 1, 3]
  [-1, 0, 1, 2],
  [-3, -1, 1, 2, 3],
  [-2, -1, 0, 2, 3],
  [-3, -1, 0, 1, 2, 3]
]
_____



[Examples]

___
get_subsets([-1, 0, 1, 2], 2) ➞ [[2], [0, 2], [-1, 1, 2], [-1, 0, 1, 2]]

get_subsets([-1, 0, 1, 2], 3) ➞ [[1, 2], [0, 1, 2]]

get_subsets([1, 2, 3, 4], 5) ➞ [[1, 4], [2, 3]]

get_subsets([-1, 0, 1, 2], 4) ➞ []
_____



[Notes]

___
*) Lists will have unique numbers.
*) Return an empty list if there does not a exist a subset whose numbers sum to that value (see fourth example).
___



[arrays] [higher_order_functions] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
itertools.combinations(iterable, r)
https://docs.python.org/2/library/itertools.html#itertools.combinations
Return r length subsequences of elements from the input iterable.
_________

"""
#Your code should go here:

