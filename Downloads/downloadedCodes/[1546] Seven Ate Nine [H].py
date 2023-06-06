"""
####  Seven Ate Nine  ####

A number can eat the number to the right of it if it's smaller than itself. After eating that number, it becomes the sum of itself and that number. Your job is to create a function that returns the final list after the leftmost element has finished "eating".


[Examples]

___
[5, 3, 7] ➞ [8, 7] ➞ [15]

# 5 eats 3 to become 8
# 8 eats 7 to become 15
_____

___
[5, 3, 9] ➞ [8, 9]

# 5 eats 3 to become 8
# 8 cannot eat 9, since 8 < 9
_____

___
nom_nom([1, 2, 3]) ➞ [1, 2, 3]

nom_nom([2, 1, 3]) ➞ [3, 3]

nom_nom([8, 5, 9]) ➞ [22]
_____



[Notes]

Test input contains only a list of numbers.


[arrays] [logic] [math] 



-------------------------------------------------------------------
[Resources]
_________
append() Method
https://www.programiz.com/python-programming/methods/list/append
Adds an item to the end of the list.
_________
_________
For Loop
https://www.programiz.com/python-programming/for-loop
In this article, you'll learn to iterate over a sequence of elements using the different variations of for loop.
_________
_________
While Loop
https://www.programiz.com/python-programming/while-loop
Used to iterate over a block of code as long as the test expression (condition) is true.
_________
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________

"""
#Your code should go here:

