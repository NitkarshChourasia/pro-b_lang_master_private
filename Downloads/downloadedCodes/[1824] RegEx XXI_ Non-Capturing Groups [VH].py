"""
####  RegEx XXI: Non-Capturing Groups  ####

A non-capturing group will match "x" in (?:x), however the match won't be stored, meaning you won't be able to access it using backreference, and it won't be output separately when using re.findall().
Let's see an example of the difference between capturing and non-capturing groups:
___
txt = "red car, blue car, yellow car, green car, red car, red bike, blue bike"

pattern1 = "(red|blue) car"
pattern2 = "(?:red|blue) car"
pattern3 = "red|blue car"
pattern4 = "((red|blue) (car|bike))"
pattern5 = "((red|blue) (?:car|bike))"


re.findall(pattern1, txt) ➞ ["red", "blue", "red"]
re.findall(pattern2, txt) ➞ ["red car", "blue car", "red car"]
re.findall(pattern3, txt) ➞ ["red", "blue car", "red", "red"]
re.findall(pattern4, txt) ➞ [("red car", "red", "car"), ("blue car", "blue", "car"), ("red car", "red", "car"), ("red bike", "red", "bike"), ("blue bike", "blue", "bike")]
re.findall(pattern5, txt) ➞ [("red car", "red"), ("blue car", "blue"), ("red car", "red"), ("red bike", "red"), ("blue bike", "blue")]
_____

___
*) The first expression matches either "red" or "blue", as long as they're followed by " car".
*) The second expression matches either "red car" or "blue car".
*) The third expression matches either "red" or "blue car".
*) In the fourth expression matches one of the following possibilities: "red car", "red bike", "blue car", "blue bike". It will return a tuple for each match containing an element for each capturing group, in this case: the whole expression, the color and the vehicle type.
*) The fifth expression is similar to the fourth except the vehicle type is a non-capturing group. As you can see, it is not returned separately.
___

Write a regular expression to match any article + noun pair. The articles are either "a/an" or "the". Use non-capturing groups in your expression.


[Example]

___
txt = "There is an apple and a pen on the desk"
pattern = "yourregularexpressionhere"

re.findall(pattern, txt) ➞ ["an apple", "a pen", "the desk"]
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and non-capturing groups in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[regex] 



-------------------------------------------------------------------
[Resources]
_________
Regex Tutorial: Parentheses for Grouping and Capturing
https://www.regular-expressions.info/brackets.html
By placing part of a regular expression inside round brackets or parentheses, you can group that part of the regular expression together. This allows you to apply a qua …
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
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________

"""
#Your code should go here:

