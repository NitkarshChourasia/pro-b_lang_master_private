"""
####  Strong Password Checker (Version 2.0)  ####

This challenge is based on Strong Password Checker. See Notes at the bottom of this page for info on the adaptation.
In this challenge, a password is considered strong if the following three conditions are met:

Write a function that takes a string txt and returns the minimum number of changes required to make it into a strong password, where each change consists of either deleting a character, or replacing a character (note that swapping characters is not allowed; each change affects one character and one character only).
If the password is already strong, return 0.


[Examples]

___
password_checker("EDABITEDABITEDABITEDA") ➞ 3
# 21 characters total, only uppercase letters, need to delete one
# character and replace two characters, onewith a digit, one with a
# lowercase letter.
# 3 minimum changes.


password_checker("000aaaBBBccccDDDDeeeee") ➞ 6
# 22 characters, and 6 sets of repeating characters.
# 2 characters need to be removed, and one change is needed in each set.
# Removing one 0 and one a, and replacing one of the middle characters
# in each of the four BBB, cccc, DDDD, eeeee blocks does the trick.
# 6 minimum changes.
_____



[Notes]

___
*) The input will always have at least 20 characters.
*) The algorithm have to be extremely efficient.
*) I believe that only time complexity O(n) can pass the tests.
___



[functional_programming] [higher_order_functions] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

