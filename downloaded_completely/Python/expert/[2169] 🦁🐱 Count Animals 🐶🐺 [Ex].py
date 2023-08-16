"""
####  🦁🐱 Count Animals 🐶🐺  ####

Mubashir needs your help to find out number of animals hidden in a given string txt.
You are provided with an array of animals given below:
___
animals = ["dog", "cat", "bat", "cock", "cow", "pig",
"fox", "ant", "bird", "lion", "wolf", "deer", "bear",
"frog", "hen", "mole", "duck", "goat"]
_____

Rule: Return the maximum number of animal names. See the below example:
___
txt = "goatcode"

count_animals(txt) ➞ 2
# First animal = "dog"
# Remaining string = "atcoe",
# Second animal = "cat".
# count = 2 (correct)

# If you got a "goat" first time
# remaining string = "code",
# no animal will be found during next time.
# count = 1 (wrong)
_____



[Examples]

___
count_animals("goatcode") ➞ 2
# "dog", "cat"

count_animals("cockdogwdufrbir") ➞ 4
# "cow", "duck", "frog", "bird"

count_animals("dogdogdogdogdog") ➞ 5
_____



[Notes]

N/A


[language_fundamentals] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
reduce() Method
https://www.geeksforgeeks.org/reduce-in-python/
Used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” mo …
_________

"""
#Your code should go here:

