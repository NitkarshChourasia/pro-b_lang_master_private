"""
####  Generate N-Size Combinations from a List  ####

Create a function that returns all combinations of size n from a list. Sort the list in ascending lexicographical order.


[Examples]

___
combo([1, 2, 3, 4], 1) ➞ [[1], [2], [3], [4]]

combo([1, 2, 3, 4], 2) ➞ [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

combo([1, 2, 3, 4], 5) ➞ []

combo([1, 2, 3, 4], 0) ➞ [[]]
_____



[Notes]

___
*) Lexicographical order: Compare the first element: [1, 2] will be before [2, 4]. If both share the same first element, compare the second element: [1, 2] is before [1, 3], etc.
*) Return an empty list [] if n exceeds the length of the list.
*) Return [[]] if n is 0 (see example #4). (Since there is only one combination of length 0: an empty list).
___



[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
itertools.combinations(iterable, r)
https://docs.python.org/3/library/itertools.html#itertools.combinations
Return r length subsequences of elements from the input iterable. Combinations are emitted in lexicographic sort order. So, if the input iterable is sorted, the combina …
_________
_________
itertools.combinations()
https://www.hackerrank.com/challenges/itertools-combinations/problem
This tool returns the r length subsequences of elements from the input iterable. Combinations are emitted in lexicographic sorted order. So, if the input iterable is so …
_________
_________
random.sample() function
https://www.geeksforgeeks.org/python-random-sample-function/
Is an inbuilt function of random module in Python that returns a particular length list of items chosen from the sequence i.e. list, tuple, string or set. Used for rand …
_________

"""
#Your code should go here:

