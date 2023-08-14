"""
####  Simplified Linear Partial Fractions  ####

A fraction like 5x-4/(x-2)(x+1) can be expressed as the sum of 2 partial fractions of the form A/(x-2), B/(x+1) where A and B are non-zero integers. When added together, the partial fractions are equivalent to the original.
Given a fraction input as a string (e.g. 5x-4/(x-2)(x+1)), write a function that returns a list of partial fractions in string form such that A and B are replaced by the appropriate non-zero integers to correctly create the appropriate partial fraction.


[Example]

___
partial_fractions("5x-4/(x-2)(x+1)") -> ["2/(x-2)", "3/(x+1)"]

# 5x-4/(x-2)(x+1) = A/(x-2) + B/(x+1)
# 5x-4 = A(x+1) + B(x-2)
# Multiply through by denominator to remove fractions.
# Use substitution into x to set to zero one term at a time to find the
# constants A & B:
#   Set x = 2, then B(x-2)=0 so A = 5(2)-4 / 3 = 2
#   Set x = -1, then A(x+1)=0 so B = 5(-1)-4 / -3 = 3
_____



[Notes]

The input numerator will always be a single term. It can be a non zero integer or a linear expression in x: either ax+b or ax-b or b-ax where a and b are non zero integers and a is positive in the b-ax form and b positive in the ax-b form. It can also be a term in x such as ax, where a is a non-zero integer.
The input denominator will be a minimum of 2 and a maximum of 3 terms. Each term is enclosed in parentheses, and each term is a linear expression in x as defined in the previous paragraph. There will be no repeated terms in the denominator, so you can always use the substitution method safely (see example above).
The partial fractions should be returned in the order their denominators appear in the denominator of the input fraction. If a partial fraction is negative, it should commence with a - character (e.g. test case 1).
Do not use spaces within a partial fraction expression. The input fraction will not have spaces either; the denominator is signaled by a /.
If you are unsure of the mathematics, the Resources should help.


[algebra] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Introduction to Partial Fractions
https://www.mathsisfun.com/algebra/partial-fractions.html
The part down to Partial Fractions Decomposition is all that is required for this challenge. You can ignore the other sections which deal with more complex scenarios.
_________

"""
#Your code should go here:

