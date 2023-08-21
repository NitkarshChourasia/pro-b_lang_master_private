/*
####  Sales Season  ####

A retailer is having a store-wide "buy 2, get 1 free" sale. For legal reasons, they can't charge their customers $0 for an article so a discount is applied to all products instead. For example, if a customer gets three products a, b and c:

She gets the cheapest one for free, so she ends up paying $15.99 + $23.50 = $39.49, but what her receipt says is:
___
*) Product A: $15.99 − Special Discount = $12.57
*) Product B: $23.50 − Special Discount = $18.47
*) Product C: $10.75 − Special Discount = $8.45
*) Total: $39.49
___

Create a function that takes an array of prices for a customer's shopping cart and returns the prices with the discount applied. Round all prices to the cent.


[Examples]

___
discount([2.99, 5.75, 3.35, 4.99]) ➞[2.47, 4.74, 2.76, 4.12]
// First product for free.

discount([10.75, 11.68]) ➞ [10.75, 11.68]
// No discounts applied.

discount([68.74, 17.85, 55.99]) ➞ [60.13, 15.62, 48.98]
// Second product for free.

discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]) ➞ [5.16, 13.45, 33.06, 10.91, 22.71, 5.16, 5.16, 5.16]
// First and sixth products for free (see second note).
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
Definition of Float
https://www.thoughtco.com/definition-of-float-958293#:~:text=Float%20is%20a%20shortened%20term,types%20include%20int%20and%20double.
Is a shortened term for "floating point." By definition, it's a fundamental data type built into the compiler that's used to define numeric values with floating decimal …
_________
_________
Rounding Floating Point Number To two Decimal Places
https://www.geeksforgeeks.org/rounding-floating-point-number-two-decimal-places-c-c/
How to round off a floatig point value to two places. For example, 5.567 should become 5.57 and 5.534 should become 5.53 First Method:- Using Float precision, Second M …
_________
_________
Ceil and Floor Functions
https://www.geeksforgeeks.org/ceil-floor-functions-cpp/
In mathematics and computer science, the floor and ceiling functions map a real number to the greatest preceding or the least succeeding integer, respectively. floor(x …
_________

*/
//Your code should go here:

