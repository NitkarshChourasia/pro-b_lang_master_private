"""
####  Sales Season  ####

A retailer is having a store-wide "buy 2, get 1 free" sale. For legal reasons, they can't charge their customers $0 for an article so a discount is applied to all products instead. For example, if a customer gets three products a, b and c:

She gets the cheapest one for free, so she ends up paying $15.99 + $23.50 = $39.49, but what her receipt says is:
___
*) Product A: $15.99 − Special Discount = $12.57
*) Product B: $23.50 − Special Discount = $18.47
*) Product C: $10.75 − Special Discount = $8.45
*) Total: $39.49
___

Create a function that takes in a list of prices for a customer's shopping cart and returns the prices with the discount applied. Round all prices to the cent.


[Examples]

___
discount([2.99, 5.75, 3.35, 4.99]) ➞[2.47, 4.74, 2.76, 4.12]
# First product for free.

discount([10.75, 11.68]) ➞ [10.75, 11.68]
# No discounts applied.

discount([68.74, 17.85, 55.99]) ➞ [60.13, 15.62, 48.98]
# Second product for free.

discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]) ➞ [5.16, 13.45, 33.06, 10.91, 22.71, 5.16, 5.16, 5.16]
# First and sixth products for free (see second note).
_____



[Notes]

___
*) The discount is calculated in percentual terms.
*) The deal applies to sets of three products: if a customer gets 9 products, she will get the three cheapest ones for free, but if she gets 10 or 11 products, she will still get three for free. Buying a 12th product would get her a fourth free product.
*) No cart splitting allowed.
___



[arrays] [math] 



-------------------------------------------------------------------
[Resources]
_________
round() Function
https://www.programiz.com/python-programming/methods/built-in/round
Returns a floating-point number rounded to the specified number of decimals. In this tutorial, we will learn about Python round() in detail with the help of examples.
_________
_________
Modulo Operator and Floor Division
https://blog.tecladocode.com/pythons-modulo-operator-and-floor-division/
Learn about the some less well-known operators in Python: modulo and floor division—as well as how they interact with each other and how they're related!
_________
_________
How to Calculate Percentages
https://www.dummies.com/education/math/basic-math/how-to-calculate-percentages/
Calculating percentages can be an easy task. There are numerous percentage calculators online that can help with task by simply searching for “percentage calculator.” H …
_________
_________
sum() Function
https://www.geeksforgeeks.org/sum-function-python/
Sum of numbers in the list is required everywhere. Python provide an inbuilt function sum() which sums up the numbers in the list.
_________
_________
sorted() Function
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________

"""
#Your code should go here:

