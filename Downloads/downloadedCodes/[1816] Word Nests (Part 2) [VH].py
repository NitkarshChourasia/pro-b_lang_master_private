"""
####  Word Nests (Part 2)  ####

A word nest is created by taking a starting word, and generating a new string by placing the word inside itself. This process is then repeated.
Nesting 3 times with the word "incredible":
___
start  = incredible
first  = incre(incredible)dible
second = increin(incredible)credibledible
third  = increinincr(incredible)ediblecredibledible
_____

The final nest is increinincrincredibleediblecredibledible (depth = 3)
Valid word nests can always be collapsed to show the starting word, by reversing the process above:
___
word = "incredible"
nest = "increinincrincredibleediblecredibledible"

Steps:
=> "increinincrincredibleediblecredibledible" # starting nest
=> "increinincr(incredible)ediblecredibledible" # find word in nest
=> "increinincr            ediblecredibledible" # remove word
=> "increinincrediblecredibledible" # join remaining halves
=> "increin(incredible)credibledible" # find word in nest...

... repeat steps until single word remains

=> "incredible" (return True as "incredible" = word)
_____

When invalid word nests are collapsed, the starting word isn't found:
___
word = "spring"
nest = "sprspspspringringringg"

Steps:
=> "sprspspspringringringg" # starting nest
=> "sprspsp(spring)ringringg" # find word in nest
=> "sprspsp        ringringg" # remove word
=> "sprspspringringg" # join remaining halves
=> "sprsp(spring)ringg" # find word in nest...

... repeat steps until single word remains

=> "sprg" (return False as "sprig" != "spring")
_____

Given a starting word and a final word nest, return True if the word nest is valid. Return False otherwise.


[Examples]

___
valid_word_nest("deep", "deep") ➞ True

valid_word_nest("novel", "nonnonovnovnovelelelvelovelvel") ➞ True

valid_word_nest("painter", "ppaintppapaipainterinternteraintererainter") ➞ False
# Doesn't show starting word after being collapsed.

valid_word_nest("shape", "sssshapeshapehahapehpeape") ➞ False
# Word placed outside, not inside itself.
_____



[Notes]

Valid word nests can only be created by repeatedly placing the word inside itself, so at any point when collapsing the nest, there should only be one instance of the word to be found.


[conditions] [language_fundamentals] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
replace() Method
https://www.programiz.com/python-programming/methods/string/replace
Returns a copy of the string where all occurrences of a substring is replaced with another substring.
_________
_________
String count() Method
https://www.programiz.com/python-programming/methods/string/count
Returns the number of occurrences of a substring in the given string.
_________
_________
Text Sequence Type — str
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways …
_________
_________
String Methods Explained
https://www.programiz.com/python-programming/methods/string
Python has quite a few methods that string objects can call to perform frequency occurring task (related to string). For example, if you want to capitalize the first le …
_________

"""
#Your code should go here:

