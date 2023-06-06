"""
####  Add Dollar Bills  ####

Create a function that takes a string containing money in dollars and pounds sterling (seperated by comma) and returns the sum of dollar bills only, as an integer.
For the input string:
___
*) Each amount is prefixed by the currency symbol: $ for dollars and £ for pounds.
*) Thousands are represented by the suffix k.
___

i.e. $4k = $4,000 and £40k = £40,000


[Examples]

___
add_bill("d20,p40,p60,d50") ➞ 20 + 50 = 70

add_bill("p30,d20,p60,d150,p360") ➞ 20  + 150 = 170

add_bill("p30,d2k,p60,d200,p360") ➞ 2 * 1000 + 200 = 2200
_____



[Notes]

There is at least one dollar bill in string.


[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
replace() Method
https://www.geeksforgeeks.org/python-string-replace/
Is an inbuilt function in Python programming language that returns a copy of the string where all occurrences of a substring are replaced with another substring.
_________
_________
Python Lists
https://developers.google.com/edu/python/lists
Python has a great built-in list type named "list". List literals are written within square brackets [ ]. Lists work similarly to strings -- use the len() function and …
_________
_________
split() Method
https://www.w3schools.com/python/ref_string_split.asp
Splits a string into a list.
_________

"""
#Your code should go here:

