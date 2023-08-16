"""
####  Distance to Nearest Vowel  ####

Write a function that takes in a string and for each character, returns the distance to the nearest vowel in the string. If the character is a vowel itself, return 0.


[Examples]

___
distance_to_nearest_vowel("aaaaa") ➞ [0, 0, 0, 0, 0]

distance_to_nearest_vowel("babbb") ➞ [1, 0, 1, 2, 3]

distance_to_nearest_vowel("abcdabcd") ➞ [0, 1, 2, 1, 0, 1, 2, 3]

distance_to_nearest_vowel("shopper") ➞ [2, 1, 0, 1, 1, 0, 1]
_____



[Notes]

___
*) All input strings will contain at least one vowel.
*) Strings will be lowercased.
*) Vowels are: a, e, i, o, u.
___



[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
range() Method
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
enumerate() Method
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________
_________
min() Method
https://www.programiz.com/python-programming/methods/built-in/min
Returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters.
_________
_________
abs() Method
https://www.programiz.com/python-programming/methods/built-in/abs
Returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.
_________

"""
#Your code should go here:

