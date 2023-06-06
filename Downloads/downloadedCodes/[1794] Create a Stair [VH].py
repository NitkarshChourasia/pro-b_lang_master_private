"""
####  Create a Stair  ####

Write a function which takes an integer steps and returns a string representing an upward stair with steps representing the number of the steps in the stair. Each step will be represented by combinations of underscore(s), newline(s), and vertical line(s).
So, if you print the result for a stair with three steps, it will look something like this:
___
      _
    _|
  _|
_|
_____

It's a crude and rickety stair, but challenging yourself in your favorite programming language is worth it.


[Examples]

___
stair(1)  ➞ "  _\n_|"
# 2 spaces, 1 underscore, 1 newline, 1 underscore, 1 vertical line

stair(2)  ➞ "    _\n  _|\n_|"
# 4 spaces, 1 undescore, 1 newline, 2 spaces, 1 underscore,
# 1 vertical line, 1 newline, 1 underscore, 1 vertical line

stair(3) ➞ "      _\n    _|\n  _|\n_|"
# 6 spaces, 1 undescore, 1 newline, 4 spaces, 1 underscore,
# 1 vertical line, 1 newline, 2 spaces, ...

stair(4) ➞ "        _\n      _|\n    _|\n  _|\n_|"
# 8 spaces, 1 undescore, 1 newline, 6 spaces, 1 underscore,
# 1 vertical line,  ...
_____



[Notes]

___
*) Since the stair is upward, the beginning of the code is the top of the stair.
*) All numbers are positive.
*) For zero, return ___ (three underscores).
___



[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String Formatting
https://www.w3schools.com/python/python_string_formatting.asp
To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method.
_________

"""
#Your code should go here:

