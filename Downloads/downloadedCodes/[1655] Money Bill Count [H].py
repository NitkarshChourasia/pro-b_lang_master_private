"""
####  Money Bill Count  ####

Create a function bill_count that takes two arguments. The first argument is the amount of money the user has and the second is the list of money bills available. Return the minimum count of money bills required to equal the user money amount.
___
bill_count(1001, [1, 10, 20])
# User Money = €1000 and Bills Available = [€1, €10, €20]

bill_count(1001, [1, 10, 20]) -> 51 because 20*50+ 1*1 = 1001
# We require 50  20€ bill and 1 1€ bill to equal €1001.
# Therefore, Minimum Count Money Bills is 50 + 1 = 51.
_____



[Examples]

___
bill_count(100, [1, 10, 20]) ➞ 5
# Because 20 * 5 = 100

bill_count(1050, [1, 10, 20, 100]) ➞ 13
# Because 100 * 10 + 20 * 2 + 10 * 1 = 1050

bill_count(3, [1, 10]) ➞ 3
# Because 3 * 1 = 3

bill_count(55, [1, 5, 10, 50]) ➞ 2
# Because 50 * 1 + 5 * 1 = 55
_____



[Notes]

Money amount and bills are all valid.


[logic] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Find the Number of Notes against a Specified Amount
https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-21.php
Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount.
_________
_________
Find Minimum Number of Currency Notes and Values That Sum to Given Amount
https://www.geeksforgeeks.org/find-number-currency-notes-sum-upto-given-amount/
Given an amount, find the minimum number of notes of different denominations that sum upto the given amount. Starting from the highest denomination note, try to accommo …
_________

"""
#Your code should go here:

