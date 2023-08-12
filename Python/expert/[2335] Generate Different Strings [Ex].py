"""
####  Generate Different Strings  ####

The function is given a string consisting from letters and digits. Each letter in the string can be changed to lower-case and upper-case; the digits stay as they are in their positions. Generate all possible strings and return them as set.


[Examples]

___
gen_strings("1A2") ➞ { "1A2", "1a2" }

gen_strings("a1B") ➞ { "A1B", "A1b", "a1B", "a1b" }

gen_strings("1a2bC3") ➞ { "1A2Bc3", "1a2Bc3", "1a2bC3", "1a2bc3", "1A2bC3", "1A2BC3", "1a2BC3", "1A2bc3" }

gen_strings("1") ➞ { "1" }

gen_strings("") ➞ {""}
_____



[Notes]

N/A


[algorithms] [conditions] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python – Itertools.Product() author anubhavraj_08 Read Discuss Courses Practice In the terms
https://www.geeksforgeeks.org/python-itertools-product/
In the terms of Mathematics Cartesian Product of two sets is defined as the set of all ordered pairs (a, b) where a belongs to A and b belongs to B. Consider the below …
_________

"""
#Your code should go here:

