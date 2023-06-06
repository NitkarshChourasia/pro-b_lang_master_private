"""
####  Tidy Title and Author Strings  ####

You have a list of strings, each consisting of a book title and an author's name.
To illustrate:
___
[
  ["   Death of a Salesman - Arthur Miller    "],
  ["   Macbeth - William Shakespeare    "],
  ["    A Separate Peace - John Knowles     "],
  [" Lord of the Flies - William Golding"],
  ["A Tale of Two Cities - Charles Dickens"]
]
_____

Create a function that takes a list like the one above and transforms it into the same format as the one below:
___
[
  ["Death of a Salesman", "Arthur Miller"],
  ["Macbeth", "William Shakespeare"],
  ["A Separate Peace", "John Knowles"],
  ["Lord of the Flies", "William Golding"],
  ["A Tale of Two Cities", "Charles Dickens"]
]
_____



[Examples]

___
tidy_books([
  ["     The Catcher in the Rye - J. D. Salinger    "],
  ["    Brave New World - Aldous Huxley   "],
  ["    Of Mice and Men - John Steinbeck    "]
]) ➞ [
  ["The Catcher in the Rye", "J. D. Salinger"],
  ["Brave New World", "Aldous Huley"],
  ["Of Mice and Men", "John Steinbeck"]
]
_____



[Notes]

Some of these entries have excess white space. Remove this white space in your final output.


[arrays] [formatting] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Remove Spaces from String
https://www.journaldev.com/23763/python-remove-spaces-from-string
There are various ways to remove spaces from a string in Python. This tutorial is aimed to provide a short example of various functions we can use to remove whitespaces …
_________

"""
#Your code should go here:

