"""
####  Popping Blocks  ####

When two blocks of the same "type" are adjacent to each other, the entire contiguous block disappears (pops off). If this occurs, this can allow previously separated blocks to be in contact with each other, setting off a chain reaction. This will continue until each block is surrounded by a different block.
Here's a demonstration:
___
["A", "B", "C", "C", "B", "D", "A"]
# The two adjacent Cs pop off

["A", "B", "B", "D", "A"]
# Two adjacent Bs pop off

["A", "D", "A"]
# No more blocks can be popped off
_____

Another demonstration:
___
["A", "B", "A", "A", "A", "B", "B"]
# The three adjacent As will pop off
# (before the two adjacent Bs)

["A", "B", "B", "B"]
# 3 adjacent Bs pop off

["A"]
# Final result
_____



[Examples]

___
final_result(["B", "B", "A", "C", "A", "A", "C"]) ➞ ["A"]

final_result(["B", "B", "C", "C", "A", "A", "A"]) ➞ []

final_result(["C", "A", "C"]) ➞ ["C", "A", "C"]
_____



[Notes]

If the first round has multiple poppable blocks, pop starting from the left.


[arrays] [games] [loops] [regex] 



-------------------------------------------------------------------
[Resources]
_________
While Loops
https://www.python-course.eu/python3_loops.php
Many algorithms make it necessary for a programming language to have a construct which makes it possible to carry out a sequence of statements repeatedly. The code wi …
_________
_________
pop() Method
https://www.programiz.com/python-programming/methods/list/pop
Removes the item at the given index from the list. The method also returns the removed item.
_________
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

