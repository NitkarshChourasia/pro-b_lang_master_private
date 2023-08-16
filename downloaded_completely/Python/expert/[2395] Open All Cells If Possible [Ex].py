"""
####  Open All Cells If Possible  ####

The function is given a list of lists of certain length n. Each element in the list is a cell marked by the list index from 0 to n - 1. Each cell contains keys - as list of integers - to other cells in the list. The cell 0 is open; that is where you find first keys to other cells. Open those cells and find new keys again. Go open other cells with new keys. Keep on repeating opening new cells while you discover new keys. Given the keys placement in different cells, determine if it is possible to open all cells, return True / False.


[Examples]

___
open_all([[1], [0]]) ➞ True
# Cell_0 has a key to cell_1. It is possible to open all two cells.

open_all([[1], [2], [3], []]) ➞ True
# The placement allows to open all cells in a row.

open_all([[1, 3], [3, 0, 1], [2], [0]]) ➞ False
# It is not possible to open cell_2.

open_all([[2, 1], [1], [2], [4], [0, 1]]) ➞ False
# It is possible to open only cells 0, 1, 2. Cells 3, 4 stay closed.
_____



[Notes]

It is possible that a cell contains keys to already open cells. This is fine; just try to open as many cells as possible.


[algorithms] [arrays] [games] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Sets
https://www.w3schools.com/python/python_sets.asp
Are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, an …
_________

"""
#Your code should go here:

