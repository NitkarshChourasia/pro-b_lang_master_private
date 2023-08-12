"""
####  Secret Function 3.0  ####

Create a function based on the input and output. Look at the examples, there is a pattern.


[Examples]

___
secret("div>p.a$$*2") ➞ `<div><p class='a01'></p><p class='a02'></p></div>`
# Only whitespace in the entire string ===  One whitespace before each class. Total " " === 2

secret("ul>li.b$*3") ➞ `<ul><li class='b1'></li><li class='b2'></li><li class='b3'></li></ul>`
# Only whitespace in the entire string === One whitespace before each class. Total " " === 3

secret("p>h1.c$$$*2") ➞ `<p><h1 class='c001'></h1><h1 class='c002'></h1></p>`
# Only whitespace in the entire string === One whitespace before each class. Total " " === 2
_____



[Notes]

Input is a string.


[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
A Guide to the Newer Python String Format Techniques
https://realpython.com/python-formatted-output/
In the last tutorial in this series, you learned how to format string data using the string modulo operator. In this tutorial, you'll see two more items to add to your …
_________

"""
#Your code should go here:

