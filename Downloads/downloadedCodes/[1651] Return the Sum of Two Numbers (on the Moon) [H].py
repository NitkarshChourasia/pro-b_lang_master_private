"""
####  Return the Sum of Two Numbers (on the Moon)  ####

When two numbers are added together, the strange Lunar arithmetic is used on the Moon. The Lunar sum of two numbers is not determined by the sum of their individual digits, but by the highest digit of the two taken into account at each step, in columnar form.
___
2  4  6  +
3  1  7  =
--------
3  4  7

# 3 > 2 | 4 > 1 | 7 > 6

1  3  4  +
   5  4  =
--------
1  5  4

#  1 > 0 | 5 > 3 | 4 == 4
# Blank spots in the columnar form are equals to 0

   2  0  +
1  4  0  =
-------
1  4  0

# 1 > 0 | 4 > 2 | 0 == 0
_____

Given two positive integers number1 and number2, implement a function that returns their sum as a new integer.


[Examples]

___
lunar_sum(246, 317) ➞ 347

lunar_sum(134, 54) ➞ 154

lunar_sum(20, 140) ➞ 140
_____



[Notes]

The given numbers will be always positive integers: no exceptions to handle.


[arrays] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How to pad a string with leading zeros?
https://stackoverflow.com/questions/39402795/how-to-pad-a-string-with-leading-zeros-in-python-3/39402910
When applied to a value, zfill() returns a value left-padded with zeros when the length of the initial string value less than that of the applied width value, otherwise …
_________
_________
Lunar Arithmetic
http://mathematics-in-europe.eu/?p=1656
One of the most popular expressions in Italy for giving strength to numbers is mathematics is not an opinion. The expression is exclusively Italian and mathematicians d …
_________
_________
itertools.zip_longest
https://www.geeksforgeeks.org/python-itertools-zip_longest/
This iterator falls under the category of Terminating Iterators. It prints the values of iterables alternatively in sequence. If one of the iterables is printed fully, …
_________

"""
#Your code should go here:

