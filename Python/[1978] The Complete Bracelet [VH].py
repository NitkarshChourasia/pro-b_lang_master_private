"""
####  The Complete Bracelet  ####

A complete bracelet is a list with at least one subsequence (pattern) repeating at least two times, and completely - the subsequence cannot be cut-off at any point. The subsequence must have length two or greater.
Complete bracelets:
___
[1, 2, 3, 3, 1, 2, 3, 3]  # Pattern: [1, 2, 3, 3]

[1, 2, 1, 2, 1, 2, 1, 2]  # Pattern: [1, 2] or [1, 2, 1, 2]

[1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7]  # Pattern: [1, 1, 6, 1, 1, 7]

[4, 4, 3, 4, 4, 4, 4, 3, 4, 4]  # Pattern: [4, 4, 3, 4, 4]
_____

Incomplete bracelets:
___
[1, 2, 2, 2, 1, 2, 2, 2, 1]  # Incomplete (chopped off)

[1, 1, 6, 1, 1, 7]  # Incomplete (subsequence repeats only once)
_____

Create a function that returns True if a bracelet is complete, and False otherwise.


[Examples]

___
complete_bracelet([1, 2, 2, 1, 2, 2]) ➞ True

complete_bracelet([5, 1, 2, 2]) ➞ False

complete_bracelet([5, 5, 5]) ➞ False
# potential pattern [5, 5] cut-off (patterns >= 2)
_____



[Notes]

___
*) Patterns must be at least two integers in length.
*) See Comments for a hint if you are stuck.
___



[arrays] [loops] [scope] [validation] 



-------------------------------------------------------------------
[Resources]
_________
any() Function
https://www.w3schools.com/python/ref_func_any.asp
Check if any of the items in a list are True.
_________
_________
all() Function
https://www.w3schools.com/python/ref_func_all.asp
Check if all items in a list are True.
_________

"""
#Your code should go here:

