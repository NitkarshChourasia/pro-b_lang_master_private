"""
####  Secret Agent Password  ####

Mubashir is going on a secret mission. He needs your help but you have to learn how to encode a secret password to communicate safely with other agents. Create a function that takes an argument message and returns the encoded password.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
secret_password("mubashirh") ➞ "hsajsi13u2"
_____

Step 1: Message length should be of nine characters containing only lowercase letters from 'a' to 'z'. If the argument doesn't meet this requirement you must return "BANG! BANG! BANG!" (Remember, there are no second chances in the spy world!)
Step 2: Divide the string into three equal parts of three characters each:
___
1 - mub
2 - ash
3 - irh
_____

Step 3: Convert the first and third letter to the corresponding number, according to the English alphabets (ex. a = 1, b = 2, c = 3 ... z = 26, etc).
___
mub = 13u2
_____

Step 4: Reverse the fourth, fifth, and sixth letters:
___
ash = hsa
_____

Step 5: Replace seventh, eighth, and ninth letter with next letter (z will be substituted with a).
___
irh = jsi
_____

Step 6: Return the string in the following order: "Part_2+Part_3+Part_1"
___
"hsajsi13u2"
_____

See the below examples for a better understanding:


[Examples]

___
secret_password("mubashirh") ➞ "hsajsi13u2"

secret_password("mattedabi") ➞ "detbcj13a20"

secret_password("HeLen-eda") ➞ "BANG! BANG! BANG!"
# Length is not equal to 9
# Contains characters other than lower alphabets
_____



[Notes]

N/A


[algorithms] [cryptography] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
str() Method
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object.
_________
_________
ord() Method
https://www.programiz.com/python-programming/methods/built-in/ord
Returns an integer representing the Unicode character.
_________
_________
all() Method
https://www.programiz.com/python-programming/methods/built-in/all
Returns True when all elements in the given iterable are true. If not, it returns False.
_________

"""
#Your code should go here:

