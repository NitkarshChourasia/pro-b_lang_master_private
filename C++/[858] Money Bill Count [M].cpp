/*
####  Money Bill Count  ####

Create a function billCount that takes two arguments. The first argument is the amount of money the user has and the second is the array of money bills available. Return the minimum count of money bills required to equal the user money amount.
___
billCount(1001, [1, 10, 20])
# User Money = €1000 and Bills Available = [€1, €10, €20]

billCount(1001, [1, 10, 20]) -> 51 because 20*50+ 1*1 = 1001
# We require 50  20€ bill and 1 1€ bill to equal €1001.
# Therefore, Minimum Count Money Bills is 50 + 1 = 51.
_____



[Examples]

___
billCount(100, [1, 10, 20]) ➞ 5
# Because 20 * 5 = 100

billCount(1050, [1, 10, 20, 100]) ➞ 13
# Because 100 * 10 + 20 * 2 + 10 * 1 = 1050

billCount(3, [1, 10]) ➞ 3
# Because 3 * 1 = 3

billCount(55, [1, 5, 10, 50]) ➞ 2
# Because 50 * 1 + 5 * 1 = 55
_____



[Notes]

Money amount and bills are all valid.


[logic] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Operators
https://www.w3schools.com/cpp/cpp_operators.asp
Are used to perform operations on variables and values. In the example below, we use the + operator to add together two values.
_________

*/
//Your code should go here:

