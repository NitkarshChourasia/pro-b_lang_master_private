"""
####  Are Pairs Sufficient for a Clear Ordering?  ####

Create a function that returns True if an array of pairs are sufficient for a clear ordering of all items.
To illustrate:
___
clear_ordering([["D", "A"], ["C", "B"], ["A", "C"]]) ➞ True
# Since unequivocally: "D" < "A" < "C" < "B"
_____

On the other hand:
___
clear_ordering([["D", "A"], ["B", "A"], ["C", "D"]]) ➞ False
# Since we know that "C" < "D" < "A", and we know "B" < "A"
# but we don't know anything about "B"s relationship with "C" or "D".
_____



[Examples]

___
clear_ordering([["S", "T"], ["T", "U"], ["U", "V"]]) ➞ True

clear_ordering([["T", "S"], ["T", "U"], ["U", "V"], ["V", "W"]]) ➞ False
_____



[Notes]

See Comments for a good visualization of the question.


[arrays] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Topological Sorting of a Directed Acyclic Graph
https://en.wikipedia.org/wiki/Topological_sorting#Uniqueness
If the input is considered as describing a graph (where the letters are nodes, and the pairwise relations are directed edges), this question can be interpreted as wheth …
_________

"""
#Your code should go here:

