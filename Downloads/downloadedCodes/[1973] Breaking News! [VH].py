"""
####  Breaking News!  ####

A local news station needs your help to generate the scrolling text for the headlines!
Create a function that returns a list of strings, where each string contains a single frame of what the scrolling text will look like.
___
*) Text will scroll from right to left.
*) The screen will have a width of n characters.
*) Start and stop when no letters appear on the screen.
___

The example below will demonstrate the output when the screen width is 10.


[Examples]

___
news_at_ten("edabit", 10) ➞ [
  "          ",
  "         e",
  "        ed",
  "       eda",
  "      edab",
  "     edabi",
  "    edabit",
  "   edabit ",
  "  edabit  ",
  " edabit   ",
  "edabit    ",
  "dabit     ",
  "abit      ",
  "bit       ",
  "it        ",
  "t         ",
  "          "
]
_____



[Notes]

___
*) Every string should be n characters long, so you should pad the string with spaces if the text isn't long enough.
*) Similarly, if the text is too long for the screen width, then it's only possible to display a fraction of the text at a time.
*) See the Tests tab for more examples.
___



[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
range() Type
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
len() Function
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
Multiply Strings
https://www.pythoncentral.io/use-python-multiply-strings/
We've already gone over how to use multiplication in Python, but did you know that Python can be used to multiply things other than numbers? In fact, you can use Python …
_________
_________
When to Use a List Comprehension
https://realpython.com/list-comprehension-python/
List comprehensions make it easy to create lists while performing sophisticated filtering, mapping, and conditional logic on their members. In this tutorial, you'll lea …
_________

"""
#Your code should go here:

