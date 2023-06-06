"""
####  Bridge Shuffle  ####

Create a function to bridge shuffle two lists. To bridge shuffle, you interleave the elements from both lists in an alternating fashion, like so:
___
List 1 = ["A", "A", "A"]
List 2 = ["B", "B", "B"]

Shuffled List = ["A", "B", "A", "B", "A", "B"]
_____

This can still work with two lists of uneven length. We simply tack on the extra elements from the longer list, like so:
___
List 1 = ["C", "C", "C", "C"]
List 2 = ["D"]

Shuffled List = ["C", "D", "C", "C", "C"]
_____

Create a function that takes in two lists and returns the bridge-shuffled list.


[Examples]

___
bridge_shuffle(["A", "A", "A"], ["B", "B", "B"]) ➞ ["A", "B", "A", "B", "A", "B"]

bridge_shuffle(["C", "C", "C", "C"], ["D"]) ➞ ["C", "D", "C", "C", "C"]

bridge_shuffle([1, 3, 5, 7], [2, 4, 6]) ➞ [1, 2, 3, 4, 5, 6, 7]
_____



[Notes]

___
*) Elements in both lists can be strings or integers.
*) If two lists are of unequal length, add the additional elements of the longer list to the end of the shuffled list.
*) Always start your shuffle with the first element of List 1.
___



[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
How to switch position of two items in a list?
https://stackoverflow.com/questions/2493920/how-to-switch-position-of-two-items-in-a-python-list
I haven’t been able to find a good solution for this problem on the net (probably because switch, position, list and Python are all such overloaded words). It’s rather …
_________
_________
How can I get the concatenation of two lists without modifying either one?
https://stackoverflow.com/questions/4344017/how-can-i-get-the-concatenation-of-two-lists-in-python-without-modifying-either
In Python, the only way I can find to concatenate two lists is list.extend, which modifies the first list. Is there any concatenation function that returns its result w …
_________
_________
Itertools.zip_longest()
https://www.geeksforgeeks.org/python-itertools-zip_longest/#:~:text=Itertools.zip_longest%20%28%29%20This%20iterator%20falls%20under%20the%20category,filled%20by%20the%20values%20assigned%20to%20fillvalue%20parameter.
This iterator falls under the category of Terminating Iterators. It prints the values of iterables alternatively in sequence. If one of the iterables is printed fully, …
_________

"""
#Your code should go here:

