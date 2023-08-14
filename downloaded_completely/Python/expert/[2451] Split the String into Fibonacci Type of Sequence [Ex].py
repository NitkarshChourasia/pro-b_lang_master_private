"""
####  Split the String into Fibonacci Type of Sequence  ####

The function is given a string of digits. Make a list of numbers from these digits such that:
___
*) The length of the list is at least three.
*) All numbers put together make the original string. (Thus one can only cut the string without permutations).
*) Starting from the third number, each number equal to the sum of two previous numbers, i.e. lst[i - 2] + lst[i - 1] == lst[i]
*) A number cannot have a leading zero, unless this number is zero. (0 - allowed, 01 - not allowed)
*) Each number in the list is less than 2^31 (to make this challenge compatible with strongly-typed languages).
___

Find the list of numbers that satisfy the above properties and return it. If a Fibonacci look-alike sequence cannot be found, return an empty list [].


[Examples]

___
split_fibonacci("11235813") ➞ [1, 1, 2, 3, 5, 8, 13]

split_fibonacci("112358130") ➞ []

split_fibonacci("123456579") ➞ [123, 456, 579]

split_fibonacci("0000") ➞ [0, 0, 0, 0]
_____



[Notes]

Multiple solutions to some tests are possible. That is why there is a helper function in the Tests window to check that the output list satisfies the requirements. This allows freedom to finding a sequence.


[algorithms] [arrays] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

