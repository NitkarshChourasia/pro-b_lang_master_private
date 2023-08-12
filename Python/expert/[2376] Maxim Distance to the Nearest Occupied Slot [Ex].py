"""
####  Maxim Distance to the Nearest Occupied Slot  ####

The function is given a string consisting from "0", "1" characters. The string represents a parking area:
___
*) "1" - the slot is occupied,
*) "0" - the slot is vacant.
___

Find a vacant slot such that it has the maximum distance from an occupied one. It can be at the ends of the area or between two "1"s. Return the maximum distance as integer.


[Examples]

___
max_distance("01") ➞ 1
# Only the first slot is vacant. Take it. The distance is 1.

max_distance("100") ➞ 2
# Take the last slot on the right. The distance is 2.

max_distance("100000101") ➞ 3
# Take the slot at index 3. The distance is 3.

max_distance("000010000001001") ➞ 4
# Take the slot at index 0. The distance is 4.
# The other possible slots at indices 7, 8 have distance 3.
_____



[Notes]

N/A


[algorithms] [logic] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python String split() Method
https://www.w3schools.com/python/ref_string_split.asp
The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.
_________

"""
#Your code should go here:

