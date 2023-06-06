"""
####  Find Repeating  ####

Create a function that accepts a string and groups repeated, consecutive values. The groups should have the following structure: [[value, first_index, last_index, times_repeated], ..., [value, first_index, last_index, times_repeated]].
___
*) value: Character being assessed.
*) first_index: Index of characters first appearance.
*) last_index: Index of characters last appearance.
*) times_repeated: Number of consecutive times character repeats.
___



[Examples]

___
find_repeating("a") ➞ [["a", 0, 0, 1]]

find_repeating("aabbb") ➞ [["a", 0, 1, 2], ["b", 2, 4, 3]]

find_repeating("1337") ➞ [["1", 0, 0, 1], ["3", 1, 2, 2], ["7", 3, 3, 1]]

find_repeating("aabbbaabbb") ➞ [["a", 0, 1, 2], ["b", 2, 4, 3], ["a", 5, 6, 2], ["b", 7, 9, 3]]
_____



[Notes]

___
*) An empty string should return an empty list: "" ➞ []
*) Non-repeated values should start and end on the same index.
___



[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
append() Method
https://www.tutorialspoint.com/python/list_append.htm
Appends a passed obj into the existing list.
_________
_________
Pythonic way to identify consecutive duplicates in a list?
https://stackoverflow.com/questions/6352425/whats-the-most-pythonic-way-to-identify-consecutive-duplicates-in-a-list
I've got a list of integers and I want to be able to identify contiguous blocks of duplicates: that is, I want to produce an order-preserving list of duples where each …
_________
_________
How do I use itertools.groupby()?
https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby
I haven't been able to find an understandable explanation of how to actually use Python's itertools.groupby() function. groupby objects yield key-group pairs where the …
_________

"""
#Your code should go here:

