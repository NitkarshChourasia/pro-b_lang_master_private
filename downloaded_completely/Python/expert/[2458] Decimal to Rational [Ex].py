"""
####  Decimal to Rational  ####

Find rational representation of a decimal number. The input number is given as string in the form whole.between(period). The output should be a tuple numerator, denominator such that gcd(numerator, denominator) == 1.


[Examples]

___
find_fraction("0.4") ➞ (2, 5)

find_fraction("0.1(6)") ➞ (1, 6)

find_fraction("0.(3)") ➞ (1, 3)

find_fraction("0.(142857)") ➞ (1, 7)

find_fraction("0.(012987)") ➞ (1, 77)
_____



[Notes]

___
*) The length of a periodic fraction can be larger than 20 digits.
*) The function should be efficient.
___



[math] [numbers] [regex] 



-------------------------------------------------------------------
[Resources]
_________
Regex Tester and Debugger
https://regex101.com
With highlighting for PHP, PCRE, Python, Golang, and JavaScript.
_________

"""
#Your code should go here:

