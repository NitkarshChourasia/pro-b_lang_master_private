"""
####  Dance for Cash  ####

Your local bank has decided to upgrade its ATM machines by incorporating motion sensor technology. The machines now interpret a series of consecutive dance moves in place of a PIN number.
Create a function that converts a customer's PIN number to its dance equivalent. There is one dance move per digit in the PIN number. A list of dance moves is given in the code.


[Examples]

___
dance_convert("0000") ➞ ["Shimmy", "Shake", "Pirouette", "Slide"]

dance_convert("3856") ➞ [ "Slide", "Arabesque", "Pop", "Arabesque" ]

dance_convert("9999") ➞ [ "Arabesque", "Shimmy", "Shake", "Pirouette" ]

dance_convert("32a1") ➞ "Invalid input."
_____



[Notes]

___
*) Each dance move will be selected from a list by index based on the current digit's value plus that digit's index value. If this value is greater than the last index value of the dance list, it should cycle to the beginning of the list.
*) Valid input will always be a string of four digits. Output will be a list of strings.
*) If the input is not four valid integers, return the string, "Invalid input."
___



[arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
enumerate() Method
http://book.pythontips.com/en/latest/enumerate.html
Enumerate is a built-in function of Python. It’s usefulness can not be summarized in a single line. Yet most of the newcomers and even some advanced programmers are una …
_________
_________
List, Set and Dict Comprehensions
https://www.youtube.com/watch?v=3dt4OGnU5sM
How they work and why you should be using them
_________
_________
isdigit() Method
https://www.tutorialspoint.com/python/string_isdigit.htm
Checks whether the string consists of digits only.
_________

"""
#Your code should go here:

