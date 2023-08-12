"""
####  Broken Bridge  ####

A broken bridge can be represented by 1s and 0s, where contiguous 0s represent holes. You can walk across a bridge with a hole with a maximum width of 1, but any holes bigger than that you must fix first. For example, the bridge below is walkeable:
___
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1]
_____

This bridge is not:
___
[1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
_____

You own several wooden planks, each with different widths. You can patch the holes on the bridge with these planks. More specifically, a plank size n can fill a n-sized hole. If you had a plank of size 2, the un-walkeable bridge above could be filled in:
___
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
_____

But even if you only had a plank of size 1, you could still transform the unwalkeable bridge into a walkeable one:
___
[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
_____

Write a function that takes in a broken bridge, a list of plank sizes, and returns True if the bridge can be patched up enough to walk over, and False otherwise.


[Examples]

___
can_patch([1, 0, 0, 0, 0, 0, 0, 1], [5, 1, 2]) ➞ True
# You can use the 5 plank to transform the 6 hole to a 1 hole.
# Leftover planks [1, 2] are okay.

can_patch([1, 0, 0, 0, 0, 0, 0, 1], [4, 1, 2, 3, 4]) ➞ False
# None of your planks are long enough (you can't combine them).

can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 2]) ➞ True

can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 1]) ➞ False
_____



[Notes]

___
*) Individual planks may NOT be combined to form a longer plank.
*) Leftover planks are okay.
___



[arrays] [higher_order_functions] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python for Loop Statements
http://www.tutorialspoint.com/python/python_for_loop.htm
Used to iterate over the items of any sequence, such as a list or a string.
_________
_________
Video Walking Through the Challenge
https://www.youtube.com/watch?v=DgfGNztJUkw
In this video, you will learn how to solve these problems in Python: Intro of Edabit, Pair Management, Boolean to String Conversion, Broken Bridge...
_________

"""
#Your code should go here:

