/*
####  Tidy Title and Author Strings  ####

You have an array of strings, each consisting of a book title and an author's name.
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

Create a function that takes an array like the one above and transforms it into the same format as the one below:
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
tidyBooks([
  "     The Catcher in the Rye - J. D. Salinger    ",
  "    Brave New World - Aldous Huxley   ",
  "    Of Mice and Men - John Steinbeck    "
]) ➞ [
  "The Catcher in the Rye", "J. D. Salinger",
  "Brave New World", "Aldous Huley",
  "Of Mice and Men", "John Steinbeck"
]
_____



[Notes]

Some of these entries have excess white space. Remove this white space in your final output.


[arrays] [formatting] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

