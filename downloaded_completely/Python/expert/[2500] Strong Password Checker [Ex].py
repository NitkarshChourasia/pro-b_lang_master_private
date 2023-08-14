"""
####  Strong Password Checker  ####

A password is considered strong if all the following conditions are met:

Write a function that takes a string txt and return the MINIMUM change required to make it a strong password. If it's already strong, return 0.


[Examples]

___
password_checker("Edabit!") ➞ 1
# 7 characters total, need to add one more digit for a strong password.
# 1 minimum change.

password_checker("edabit1!") ➞ 1
# 8 characters total, need to add an uppercase letter.
# 1 minimum change.

password_checker("EDABITEDABITEDABITEDA") ➞ 3
# 21 characters total, only uppercase letters, need to delete one
# character and replace two characters, 1 with a digit, 1 with a
# lowercase letter.
# 3 minimum changes.

password_checker("Edaaaabit!!1") ➞ 1
# Contains more than 3 repeating characters in a row - "aaaa", need
# to replace an "a" with a different character (e.g. "a3aa" or in some
# cases add a character in the middle "aa2aa".
# 1 minimum change.

password_checker("000aaaBBBccccDDDDeeeee") ➞ 6
# 22 characters, and 6 sets of repeating characters.
# 2 characters need to be removed, and one change is needed in each set.
# removing one 0 and one a, and replacing one of the middle characters
# in each of the four BBB,cccc,DDDD,eeeee blocks does the trick
# 6 minimum changes.
_____



[Notes]

___
*) Insertion, deletion or replacement of any one character is considered one change.
*) Spaces will be ignored for this challange.
___



[functional_programming] [higher_order_functions] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Check If a String Has Both Uppercase and Lowercase Letters
https://stackoverflow.com/questions/39991064/in-python-how-do-you-check-if-a-string-has-both-uppercase-and-lowercase-letters
Your question is simple to answer. You are returning things of the form return('steps' == True) which is always going to return false. So just replace those with return …
_________

"""
#Your code should go here:

