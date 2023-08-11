"""
####  RegEx Exercise #2: HTML Tags  ####

Write three regular expressions:
___
*) One called opening_tags that will match all HTML opening tags including attributes.
*) One called closing_tags that will match all HTML closing tags.
*) One called all_tags that will match all HTML tags opening or closing, their attributes and their content (as long as their content is in the same line). Please, check the example below to see the expected result.
___



[Example]

___
index = '''
<html>
<head>
    Hi! I'm a text in the head.
    I probably shouldn't be here.
    <title>edabit.com</title>
</head>
<body>
    Hi! I'm a text in the body.
    <p>This is a parragraph and <a href="https://edabit.com">this is a link</a>.</p>
    Here comes a fake tag: <>.
</body>
</html>
'''

opening_tags = "yourregularexpressionhere"
closing_tags = "yourregularexpressionhere"
all_tags = "yourregularexpressionhere"

re.findall(opening_tags, index) ➞ ["<html>", "<head>", "<title>", "<body>", "<p>", "<a href="https://edabit.com">"]

re.findall(closing_tags, index) ➞ ["</title>", "</head>",  "</a>", "</p>", "</body>", "</html>"]

re.findall(all_tags, index) ➞ ["<html>", "<head>", "<title>edabit.com</title>", "</head>", "<body>", "<p>This is a parragraph and <a href="https://edabit.com">this is a link</a>.</p>", "</body>", "</html>"]
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[regex] 



-------------------------------------------------------------------
[Resources]
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________
_________
Online RegEx Tester and Debugger
https://regex101.com/
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
Python RegEx Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
Regular expression cheatsheet.
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________

"""
#Your code should go here:

