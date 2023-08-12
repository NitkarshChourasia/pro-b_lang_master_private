"""
####  Translate from Human to Programmer  ####

Replace the numbers in a string with their binary form.


[Examples]

___
replace_nums("I have 2 sheep.") ➞ "I have 10 sheep."

replace_nums("My father was born in 1974.10.25.") ➞ "My father was born in 11110110110.1010.11001."

replace_nums("10hell76o4 boi") ➞ "1010hell1001100o100 boi"
_____



[Notes]

___
*) There are possibly two or more numbers in a single word (I do not recommend splitting the text at spaces, it surely won't help).
*) Anything separates two numbers, even spaces ("2 2" --> "10 10").
___



[algorithms] [loops] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
bin() Method
https://www.programiz.com/python-programming/methods/built-in/bin
Converts and returns the binary equivalent string of a given integer. If the parameter isn't an integer, it has to implement __index__() method to return an integer.
_________
_________
Regular Expressions: Regexes in Python
https://realpython.com/regex-python/
In previous tutorials in this series, you've seen several different ways to compare string values with direct character-by-character comparison. In this tutorial, you'l …
_________
_________
Python RegEx (With Examples)
https://www.programiz.com/python-programming/regex
In this tutorial, you will learn about regular expressions (RegEx), and use Python's re module to work with RegEx (with the help of examples).
_________
_________
re.sub Examples
https://lzone.de/examples/Python%20re.sub
Take care to always prefix patterns containing \ escapes with raw strings (by adding an r in front of the string). Otherwise the \ is used as an escape sequence and the …
_________
_________
Cannot Use '\1' Backreference to Capture-Group in a Function Call in re.sub()
https://stackoverflow.com/questions/48697161/cant-use-1-backreference-to-capture-group-in-a-function-call-in-re-sub-rep
As it turns out, calling the re.sub method is a decent way to replace a capture in a string, but manipulating it as a number is a challenge due to the way regex evaluat …
_________

"""
#Your code should go here:

