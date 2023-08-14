"""
####  Left, Right Shift  ####

Create two functions: a left-shift function and a right-shift function. Each function will take in a list and a single parameter: the number of shifts.
___
[1, 2, 3, 4, 5]

[2, 3, 4, 5, 1]  # left shift of 1
[5, 1, 2, 3, 4]  # left shift of 4

[5, 1, 2, 3, 4]  # right shift of 1
[3, 4, 5, 1, 2]  # right shift of 3
_____



[Examples]

___
left_shift([1, 2, 3, 4], 1) ➞ [2, 3, 4, 1]

right_shift([1, 2, 3, 4], 1) ➞ [4, 1, 2, 3]

left_shift([1, 2, 3, 4, 5], 3) ➞ [4, 5, 1, 2, 3]

left_shift([1, 2, 3, 4, 5], 5) ➞ [1, 2, 3, 4, 5]
# You have fully shifted the list, you end up back where you began.

left_shift([1, 2, 3, 4, 5], 6) ➞ [2, 3, 4, 5, 1]
# You should be able to take in numbers greater than the length.
# Think of the length of the list as a modulo.
_____



[Notes]

___
*) n might be higher than the number of values in the list.
*) n will never be negative.
___



[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
How to move characters in string by X amount?
https://stackoverflow.com/questions/33192395/python-how-to-move-characters-in-string-by-x-amount
In python how can I move characters in string by x amount? For example lets say the input was "hello" How can I move each character in the string by 1 so the output I …
_________
_________
Move All Elements of a List to the Right by One
https://stackoverflow.com/questions/34279048/python-move-all-elements-of-a-list-to-the-right-by-one
So I want to move all the elements to the right so for example if I had a list of [1, 2, 3, 4, 5] it would become [5, 1, 2, 3, 4]. So basically the rightmost element wr …
_________

"""
#Your code should go here:

