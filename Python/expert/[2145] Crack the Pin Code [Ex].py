"""
####  Crack the Pin Code  ####

Given a keypad that has the following layout:
___
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
_____

Your secret agent Mubashir has already given you a pincode. However, he also said it's possible that each of the digits he saw could be another adjacent digit (horizontally or vertically, but not diagonally).
Suppose the secret agent has given you the code: 46:
___
# Instead of the 4 it could also be 1, 5, or 7.
# Instead of the 6 it could also be 3, 5, or 9.

crack_pincode("46") ➞
["13","15","16","19","43","45","46","49","53","55","56","59","73","75","76","79"]
_____

Create a function that takes an argument of pincode informed by your secret agent and returns a list of all possible variations of the pin codes.


[Examples]

___
crack_pincode("0") ➞ ["0", "8"]

crack_pincode("2") ➞ ["1", "2", "3", "5"]

crack_pincode("007") ➞ ["004","007","008","084","087","088","804","807","808","884","887","888"]
_____



[Notes]

All pin codes must be strings, because of potentially leading 0s.


[algorithms] [games] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
List sort() Method
https://www.w3schools.com/python/ref_list_sort.asp
Sorts the list ascending by default.
_________
_________
Python Conditions and If statements
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. An "if stateme …
_________

"""
#Your code should go here:

