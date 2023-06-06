"""
####  RegEx Exercise #4: Edit the Body Element  ####

Write three regular expressions that will be passed to re.sub() in order to modify the body element in our HTML file:
___
*) One called body_insert that will be used to add elements immediately after the body element opening tag: <body>.
*) One called body_append that will be used to add elements immediately before the body element closing tag: </body>.
*) One called body_rewrite that will be used to replace the content of the body element: <body>content</body>.
___

Details to take into account:
___
*) The opening tag <body> will be followed by line break \n, you should match after the line break.
*) The closing tag </body> will be preceded by line break \n, you should match before the line break.
*) You do not need to worry about the inserted elements' formatting, it's already been taken care of.
*) body_rewrite should match the content of the body element, but not the body tags.
*) The content of the body element may be in more than one line.
___



[Example]

___
index = '''
<body>
    <p>This is a paragraph and <a href="https://edabit.com">this is a link</a>.</p>
</body>
'''

body_insert = "yourregularexpressionhere"
body_append = "yourregularexpressionhere"
body_rewrite = "yourregularexpressionhere"
_____



[body_insert]

___
re.sub(body_insert, '    <p>Pre-Paragraph</p>\n', index) ➞
'''
<body>
    <p>Pre-Paragraph</p>
    <p>This is a paragraph and <a href="https://edabit.com">this is a link</a>.</p>
</body>
'''
_____



[body_append]

___
re.sub(body_append, '\n    <p>Post-Paragraph</p>', index) ➞
'''
<body>
    <p>This is a paragraph and <a href="https://edabit.com">this is a link</a>.</p>
    <p>Post-Paragraph</p>
</body>
'''
_____



[body_rewrite]

___
re.sub(body_rewrite, '    <p>Anti-Paragraph</p>', index) ➞
'''
<body>
    <p>Anti-Paragraph</p>'
</body>
'''
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) If you get stuck, check Comments for some helpful hints.
*) Find more info on RegEx in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[regex] 



-------------------------------------------------------------------
[Resources]
_________
Online RegEx Tester and Debugger
https://regex101.com/
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
Python RegEx Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
Regular expression cheatsheet.
_________

"""
#Your code should go here:

