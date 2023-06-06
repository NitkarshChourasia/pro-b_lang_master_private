"""
####  Alt Facts, Semi Facts  ####

The factorial of a positive number n is the product of all numbers from 1 to n.
___
5! = 5 x 4 x 3 x 2 x 1 = 120
_____

The semifactorial (also known as the double factorial) of a positive number n is the product of all numbers from 1 to n that have the same parity (i.e. odd or even) as n.
___
12!! = 12 x 10 x 8 x 6 x 4 x 2 = 46,080

7!! = 7 x 5 x 3 x 1 = 105
_____

The alternating factorial of a positive number n is the sum of the consecutive factorials from n to 1, where every other factorial is multiplied by -1.
Alternating factorial of 1:
___
af(1) = 1!
_____

Alternating factorial of 2:
___
af(2) = 2! + (-1)x(1!) = 2! - 1! = 2 -1 = 1
_____

Alternating factorial of 3:
___
af(3) = 3! - 2! + 1! = 6 - 2 + 1 = 5
_____

Create a function that takes a number n and returns the difference between the alternating factorial and semifactorial of n.


[Examples]

___
alt_semi(1) ➞ 0

alt_semi(2) ➞ -1

alt_semi(3)➞ 2
_____



[Notes]

N/A


[algebra] [math] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Alternating Factorial
https://en.wikipedia.org/wiki/Alternating_factorial
Is the absolute value of the alternating sum of the first n factorials of positive integers.
_________
_________
Alternating Sums of Factorials
https://www.johndcook.com/blog/2015/12/12/alternating-sums-of-factorials/
If we let f(n) be the alternating factorial sum starting with n, f(n) is prime for n = 3, 4, 5, 6, 7, 8, but not for n = 9. So the alternating sums aren’t all prime. Is …
_________

"""
#Your code should go here:

