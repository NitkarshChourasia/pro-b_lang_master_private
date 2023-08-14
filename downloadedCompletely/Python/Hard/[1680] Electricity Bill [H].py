"""
####  Electricity Bill  ####

Create a function that takes number of units consumed by the customer and returns calculated Electricity Bill as per following conditions:
___
*) First 100 Units will be charged at $1/unit.
*) Next 100 Units will be charged at $2/unit.
*) Next 100 Units will be charged at $3/unit.
*) Next 200 Units will be charged at $4/unit.
*) Next Units will be charged at $5/unit.
*) 10% tax to be added in final amount.
*) Extra $15 to be added for Meter Charge.
___



[Examples]

___
electricity_bill(100) ➞ 125
# 100 units at $1/unit = 100,
# 10% Tax = 10,
# $15 for Meter Charge = 15,
# Electricity Bill = 100 + 10 + 15

electricity_bill(225) ➞ 427.5
# 100 units at $1/unit = 100, 100 units at $2/unit = 200, 25 units at $3/unit = 75
# 10% Tax = 37.5,
# 15$ for Meter Charge = 15,
# Electricity Bill = 100 + 200 + 75 + 22.5 + 15 = 427.50

electricity_bill(300) ➞ 675
# 100 units at $1/unit = 100, 100 units at $2/unit = 200, 100 units at $3/unit = 300
# 10% Tax = 60,
# 15$ for Meter Charge = 15,
# Electricity Bill = 100 + 200 + 300 + 60 + 15 = 675
_____



[Notes]

Return final calculated Electricity Bill rounded up to two decimal places.


[conditions] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
floor() and ceil()
https://www.geeksforgeeks.org/floor-ceil-function-python/
floor() method in Python returns floor of x i.e., the largest integer not greater than x. The method ceil() in Python returns ceiling value of x i.e., the smallest inte …
_________
_________
Arithmetic Operators
https://www.learnpython.org/en/Basic_Operators
Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.
_________

"""
#Your code should go here:

