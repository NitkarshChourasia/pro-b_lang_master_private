"""
####  To the Right, to the Right!  ####

Create a class that imitates a select screen. For simplicity, the cursor can only move right!
In the display method, return a string representation of the list, but with square brackets around the currently selected element. Also, create the method to_the_right, which moves the cursor one element to the right.
The cursor should start at index 0.


[Examples]

___
menu = Menu([1, 2, 3])
menu.display() ➞ "[[1], 2, 3]"
_____

___
menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"
_____



[Notes]

The cursor should wrap back round to the start once it reaches the end.


[arrays] [classes] [objects] 



-------------------------------------------------------------------
[Resources]
_________
How do you insert into a list by slicing?
https://stackoverflow.com/questions/2947872/python-how-do-you-insert-into-a-list-by-slicing
Give an example of how you can slice a list and insert something into it to make it bigger?
_________

"""
#Your code should go here:

