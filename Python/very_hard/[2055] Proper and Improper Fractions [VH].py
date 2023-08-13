"""
####  Proper and Improper Fractions  ####

Mubashir was reading about Proper and Improper Fractions on Wikipedia. He concluded that if n is the numerator and d is the denominator of a given fraction, the fraction can be called as Proper Fraction if and only if GCD(n,d)==1.
For example 5/16 is a proper fraction, while 6/16 is an improper fraction, as both 6 and 16 are divisible by 2, thus the fraction can be reduced to 3/8.
Create a function that takes a denominator number d and returns the total number of proper fractions which can be built using d as a denominator.
See below example for given denominator d = 15:
___
proper_fractions(15) ➞ 8

# A total of 8 different proper fractions are possible between 0 and 1
# 1/15, 2/15, 4/15, 7/15, 8/15, 11/15, 13/15 and 14/15.
_____



[Examples]

___
proper_fractions(1) ➞ 0

proper_fractions(2) ➞ 1

proper_fractions(5) ➞ 4

proper_fractions(25) ➞ 20
_____



[Notes]

You can expect big numbers.


[language_fundamentals] [logic] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Proper and Improper Fractions
https://en.wikipedia.org/wiki/Fraction#Proper_and_improper_fractions
Common fractions can be classified as either proper or improper. When the numerator and the denominator are both positive, the fraction is called proper if the numerato …
_________
_________
Euler's Totient Function
https://en.wikipedia.org/wiki/Euler%27s_totient_function
Counts the positive integers up to a given integer n that are relatively prime to n.
_________

"""
#Your code should go here:

