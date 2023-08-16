"""
####  Clockwise Cipher  ####

In Clockwise Cipher, encoding is done by placing message characters in the corner cells of a square and moving in a clockwise direction.
Create a function that takes an argument message, and returns the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "Mubashir Hassan"

clockwise_cipher(message) ➞ "Ms ussahr nHaaib"
_____

Step 1: Form a square large enough to fit all the message characters. Given message can fit in a 4 x 4 square.
Step 2: Starting with the top-left corner, place message characters in the corner cells moving in a clockwise direction. After the first cycle is complete, continue placing characters in the cells following the last one in its respective row/column. When the outer cells are filled, continue for the remaining inner squares:

Step 3: Return encoded message Rows-wise:
___
eMessage = "Ms ussahr nHaaib"
_____



[Example for a 5 x 5 Square]

___
[ 1  5  9 13  2]
[16 17 21 18  6]
[12 24 25 22 10]
[ 8 20 23 19 14]
[ 4 15 11  7  3]
_____



[Examples]

___
clockwise_cipher("Mubashir Hassan") ➞ "Ms ussahr nHaaib"

clockwise_cipher("Matt MacPherson") ➞ "M ParsoMc nhteat"

clockwise_cipher("Edabit is amazing") ➞ "Eisadng  tm    i   zbia a"
_____



[Notes]

___
*) Fill up any unused cells with a space character.
*) Message can contain spaces and special characters.
___



[algorithms] [cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other program …
_________
_________
Enumerate() in Python
https://www.geeksforgeeks.org/enumerate-in-python/
A lot of times when dealing with iterators, we also get a need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumer …
_________
_________
When to use yield instead of return in Python?
https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off. When …
_________
_________
floor() and ceil()
https://www.geeksforgeeks.org/floor-ceil-function-python/
Returns floor of x i.e., the largest integer not greater than x.
_________

"""
#Your code should go here:

