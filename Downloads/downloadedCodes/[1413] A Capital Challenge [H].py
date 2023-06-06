"""
####  A Capital Challenge  ####

Given two strings, s1 and s2, select only the characters in each string where the character in the same position in the other string is in uppercase. Return these as a single string.
To illustrate, given the strings s1 = "heLLo" and s2 = "GUlp", we select the letters "he" from s1, because "G" and "U" are uppercase. We then select "lp" from s2, because "LL" is in uppercase. Finally, we join these together and return "help".


[Examples]

___
select_letters("heLLO", "GUlp") ➞ "help"

select_letters("1234567", "XxXxX")  ➞ "135"

select_letters("EVERYTHING", "SomeThings") ➞  "EYSomeThings"
_____



[Notes]

___
*) The strings don't have to be the same length.
*) Strings can contain non-alphabetic characters.
___



[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
enumerate() Method
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________
_________
upper() Method
https://www.w3schools.com/python/ref_string_upper.asp
Returns a string where all characters are in upper case. Symbols and Numbers are ignored.
_________

"""
#Your code should go here:

