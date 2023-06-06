"""
####  How Close to the Speed of Light?  ####

An ultrarelativistic particle is one whose speed v is very close to the speed of light c (or equivalently, one whose β = v/c is very close to 1). But a number like 0.9999999999999999999 is inconvenient to work with: calculators round it to 1, and trying to write it in scientific notation does the same (because any 9 you stop at gets rounded up by the following 9). It's better to work with the quantity (1 - β) instead.
Fortunately, we don't need to deal directly with β to calculate an ultrarelativistic particle's (1 - β). There are some other wieldier quantities that we can use to approximate (1 - β) with great precision. One of them is the particle's rapidity φ, which is related to β by the equation:
___
tanh φ = β
_____

(where tanh is the hyperbolic tangent function).
For an ultrarelativistic particle, the rapidity lets us approximate (1 - β) like this:
___
1 - β ≈ sech(2φ)
_____

(where sech is the hyperbolic secant).
Write a function that takes an ultrarelativistic particle's rapidity (a number) and uses the approximation formula given above to return the particle's (1 - β) to three significant figures. The output should be a string in scientific notation, formatted like "6.63e-34".


[Examples]

___
how_close_to_c(3.14) ➞ "3.75e-3"

how_close_to_c(42) ➞ "6.61e-37"

how_close_to_c(355) ➞ "8.95e-309"
_____



[Notes]

N/A


[algebra] [math] 



-------------------------------------------------------------------
[Resources]
_________
Golden Ratio
https://en.wikipedia.org/wiki/Golden_ratio
In mathematics, two quantities are in the golden ratio if their ratio is the same as the ratio of their sum to the larger of the two quantities. Expressed algebraically …
_________
_________
Print a Number in Scientific Notation
https://kite.com/python/answers/how-to-print-a-number-in-scientific-notation-in-python
Printing a number in scientific notation formats the number as a float, followed by "e+" and the appropriate power of 10. For example, printing 12300000 in scientific n …
_________
_________
Display Float in Scientific Notation
https://stackoverflow.com/questions/6913532/display-a-decimal-in-scientific-notation
How can I display this: Decimal('40800000000.00000000000000') as '4.08E+10'?
_________
_________
hyperbolic-functions
https://docs.python.org/2/library/math.html#hyperbolic-functions
sech x = 1/cosh x
_________

"""
#Your code should go here:

