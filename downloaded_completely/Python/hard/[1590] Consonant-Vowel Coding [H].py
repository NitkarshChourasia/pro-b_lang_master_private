"""
####  Consonant-Vowel Coding  ####

Create a function that takes in a sentence and returns a running list of consonants per word and vowels per word.


[Examples]

___
string_code("Happy Birthday To Me!")
➞ ["4 6 1 1", "1 2 1 1"]

# Consonants - 4 : [H, p, p, y], 6 : [B, r, t, h, d, y], 1: [T], 1 : [M]
# Vowels - 1: [a], 2 : [i, a], 1: [o], 1: [e]

string_code("I'd like to drink my first glass of champagne.")
➞ [ "1 2 1 4 2 4 4 1 6", "1 2 1 1 0 1 1 1 3"]

string_code("The first man to walk on the moon was Neil Armstrong.")
➞ [ "2 4 2 1 3 1 2 2 2 2 7", "1 1 1 1 1 1 1 2 1 2 2" ]
_____



[Notes]

___
*) Count y as a consonant.
*) Capitalization does not matter.
*) Only count letters and disregard all other characters (e.g. numbers, punctuation, etc).
*) A space between numbers is required (["1 2 3", "4 5 6"] vs. ["1,2,3", "4,5,6"]).
___



[higher_order_functions] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Count and Display Vowels in a String
https://www.geeksforgeeks.org/python-count-display-vowels-string/
In this program, we need to count the number of vowels present in a string and display those vowels. This can be done using various methods. In this article, we will go …
_________

"""
#Your code should go here:

