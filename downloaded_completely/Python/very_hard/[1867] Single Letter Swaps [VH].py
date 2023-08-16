"""
####  Single Letter Swaps  ####

Given an array of strings and an original string, write a function to output an array of boolean values - True if the word can be formed from the original word by swapping two letters only once and False otherwise.


[Examples]

___
validate_swaps(["BACDE", "EBCDA", "BCDEA", "ACBED"], "ABCDE")
➞ [True, True, False, False]

# Swap "A" and "B" from "ABCDE" to get "BACDE".
# Swap "A" and "E" from "ABCDE" to get "EBCDA".
# Both "BCDEA" and "ACBED" cannot be formed from "ABCDE" using only a single swap.

validate_swaps(["32145", "12354", "15342", "12543"], "12345")
➞ [True, True, True, True]

validate_swaps(["9786", "9788", "97865", "7689"], "9768")
➞ [True, False, False, False]
_____



[Notes]

Original string will consist of unique characters.


[arrays] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Using the zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________
_________
Set Operations
https://www.geeksforgeeks.org/python-set-operations-union-intersection-difference-symmetric-difference/
This article demonstrates different operations on Python sets.
_________

"""
#Your code should go here:

