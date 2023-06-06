"""
####  K-th Element of a Binary Sorted List  ####

Given two positive integers n and k, generate all binaries between the integers 0 and (2^n) - 1 , inclusives. These binaries will be sorted in descending order according to the number of existing 1s on it, if there is a tie, we choose the lowest numerical value. Return the k-th element from the sorted list created.
For n = 3 and k = 5 for exemple, the numbers from 0 to 7 (7 = (2^3) - 1), make the binary list:
___
["0b0", "0b1", "0b10", "0b11", "0b100", "0b101", "0b110", "0b111"]
_____

When sorted by the rules, we have:
___
["0b111", "0b11", "0b101", "0b110", "0b1", "0b10", "0b100", "0b0"]
_____

And "0b1" is the fifth element on it.


[Examples]

___
k_th_binary_inlist(3, 5) ➞ "0b1"
# ["0b111", "0b11", "0b101", "0b110", "0b1", "0b10", "0b100", "0b0"]

k_th_binary_inlist(4, 10) ➞ "0b1010"
# ["0b1111", "0b111", "0b1011", "0b1101", "0b1110", "0b11", "0b101", "0b110", "0b1001", "0b1010", "0b1100", "0b1", "0b10", "0b100", "0b1000", "0b0"]

k_th_binary_inlist(5, 16) ➞ "0b11100"
# ["0b11111", "0b1111", "0b10111", "0b11011", "0b11101", "0b11110", "0b111", "0b1011", "0b1101", "0b1110", "0b10011", "0b10101", "0b10110", "0b11001", "0b11010", "0b11100", "0b11", "0b101", "0b110", "0b1001", "0b1010", "0b1100", "0b10001", "0b10010", "0b10100", "0b11000", "0b1", "0b10", "0b100", "0b1000", "0b10000", "0b0"]
_____



[Notes]

N/A


[algorithms] [data_structures] [logic] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
bin() Method
https://www.programiz.com/python-programming/methods/built-in/bin
Converts and returns the binary equivalent string of a given integer. If the parameter isn't an integer, it has to implement __index__() method to return an integer.
_________
_________
sorted() Function
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
count() Method
https://www.programiz.com/python-programming/methods/string/count
In this tutorial, we will learn about the Python String count() method with the help of examples.
_________
_________
How to Use sorted() and sort() Functions
https://realpython.com/python-sort/
In this step-by-step tutorial, you’ll learn how to sort in Python. You'll know how to sort various types of data in different data structures, customize the order, and …
_________
_________
sort() Method
https://www.programiz.com/python-programming/methods/list/sort
In this tutorial, we will learn about the Python sort() method with the help of examples.
_________

"""
#Your code should go here:

