"""
####  Index Parity of Largest Even  ####

Write a function that returns the largest even integer in a list with its corresponding index and the parity of that index, but determining the parity of that index is limited to not using the modulo operator %.


[Output Structure:]

You have to return a Dictionary.
___
{"@odd|even index " + index_of_largest: largest_integer}
_____



[Examples]

___
bitwise_index([107, 19, 36, -18, -78, 24, 97]) ➞ {"@even index 2": 36}

bitwise_index([31, 7, 2, 13, 7, 9, 10, 13]) ➞ {"@even index 6": 10}

bitwise_index([4, 4, 4, 4, 4, 4]) ➞ {"@even index 0": 4}

bitwise_index([-31, -7, -13, -7, -9, -13]) ➞ "No even integer found!"
_____



[Notes]

___
*) The use of index() and max() are restricted.
*) If there are no even integers, return "No even integer found!".
*) The set of limitations imposed on this challenge dictates the level of difficulty.
*) Another version of this challenge that deals with recursion can be found here.
___



[arrays] [bit_operations] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Check a Number Is Odd or Even Without Modulus Operator
https://www.geeksforgeeks.org/3-ways-check-number-odd-even-without-using-modulus-operator-set-2-can-merge-httpswww-geeksforgeeks-orgcheck-whether-given-number-even-odd/
Check a number is odd or even without modulus operator.
_________
_________
enumerate() Method
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________

"""
#Your code should go here:

