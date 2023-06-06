"""
####  Capitalization Families  ####

Write a function that groups words by the number of capital letters and returns a dictionary of object entries whose keys are the number of capital letters and the values are the groups.


[Examples]

___
grouping(["HaPPy", "mOOdy", "yummy", "mayBE"]) ➞ {
  0: ["yummy"],
  2: ["mayBE", "mOOdy"],
  3: ["HaPPy"]
}

grouping(["eeny", "meeny", "miny", "moe"]) ➞ {
  0: ["eeny", "meeny", "miny", "moe"]
}

grouping(["FORe", "MoR", "bOR", "tOR", "sOr", "lor"]) ➞ {
  0: ["lor"],
  1: ["sOr"],
  2: ["MoR", "bOR", "tOR"],
  3: ["FORe"]
}
_____



[Notes]

___
*) The object entries have to be sorted by the number of capital letters.
*) The groups will be arrays of all words sharing the same number of capital letters.
*) The groups have to be sorted alphabetically (ignoring case).
*) Words will be unique.
___



[objects] [sorting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python Dictionaries
https://www.python-course.eu/python3_dictionaries.php
In this chapter of our online Python course we will present the dictionaries and the operators and methods on dictionaries. Python programs or scripts without lists and …
_________
_________
isupper() Method
https://www.w3schools.com/python/ref_string_isupper.asp
Check if all the characters in the text are in upper case.
_________
_________
lower() Method
https://www.w3schools.com/python/ref_string_lower.asp
Returns a string where all characters are lower case.
_________

"""
#Your code should go here:

