"""
####  Neighboring Letters  ####

Create a function that takes a string and checks if every single character is preceded and followed by a character adjacent to it in the english alphabet.
Example: "b" should be preceded and followed by ether "a" or "c" (abc || cba || aba || cbc == True but abf || zbc == False).


[Examples]

___
neighboring("aba") ➞ True

neighboring("abcdedcba") ➞ True

neighboring("efghihfe") ➞ False

neighboring("abc") ➞ True

neighboring("qrstuv") ➞ True

neighboring("mnopqrstsrqponm") ➞ True
_____



[Notes]

All test cases will consist of lower case letters only.


[formatting] [higher_order_functions] [language_fundamentals] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
zip() Function
https://www.w3schools.com/python/ref_func_zip.asp
Returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator …
_________
_________
all() Method
https://www.programiz.com/python-programming/methods/built-in/all
Returns True when all elements in the given iterable are true. If not, it returns False.
_________
_________
enumerate() Method
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________
_________
ord() Method
https://www.programiz.com/python-programming/methods/built-in/ord
Returns an integer representing the Unicode character.
_________

"""
#Your code should go here:

