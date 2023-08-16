"""
####  Product of Digits of Sum  ####

Create a function that takes one, two or more numbers as arguments and adds them together to get a new number. The function then repeatedly multiplies the digits of the new number by each other, yielding a new number, until the product is only 1 digit long. Return the final product.


[Examples]

___
sum_dig_prod(16, 28) ➞ 6
# 16 + 28 = 44
# 4 * 4 =  16
# 1 * 6 = 6

sum_dig_prod(0) ➞ 0

sum_dig_prod(1, 2, 3, 4, 5, 6) ➞ 2
_____



[Notes]

The input of the function is at least one number.


[arrays] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
*args and **kwargs in Python
https://www.geeksforgeeks.org/args-kwargs-python/
The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-le …
_________
_________
YouTube Video by sentdex on *args and **kwargs
https://www.youtube.com/watch?v=gZB_ENJD34E
The idea behind *args and **kwargs is that there may be times when you have a function and you want to be able to handle an unknown number of arguments. The *args will …
_________

"""
#Your code should go here:

