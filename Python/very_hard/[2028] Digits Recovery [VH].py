"""
####  Digits Recovery  ####

Mubashir shuffled a given string of letters by mistake. Some letters in the input string are representing a digit (from zero to nine). Help him to recover all the digits.
___
*) Only consecutive letters can be used. "OTNE" cannot be recovered to 1.
*) Every letter has to start with an increasing index. "ONENO" results to 11, because E can be used two times.
*) You can ignore all letters in the string if they don't end-up in a digit.
*) If no digits can be found, return "No digits found"
*) Take care about the order! "ENOWT" will be recovered to 12 and not to 21.
*) The input string consists only UpperCase letters.
___



[Examples]

___
digits_recovery("NEO") ➞ "1"

digits_recovery("ONETWO") ➞ "12"

digits_recovery("ZYX") ➞ "No digits found"

digits_recovery("NEOTWONEINEIGHTOWSVEEN") ➞ "12219827"
_____



[Notes]

You can use dictionary in the code tab.


[algorithms] [logic] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string. A string must be specified as the separator.
_________
_________
Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
Are used to store data values in key: value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
_________
_________
map() Function
https://www.geeksforgeeks.org/python-map-function/
Returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
_________

"""
#Your code should go here:

