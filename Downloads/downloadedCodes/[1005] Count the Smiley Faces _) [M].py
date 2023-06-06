"""
####  Count the Smiley Faces :)  ####

Create a function that takes a list of strings and return the number of smiley faces contained within it. These are the components that make up a valid smiley:
___
*) A smiley has eyes. Eyes can be : or ;.
*) A smiley has a nose but it doesn't have to. A nose can be - or ~.
*) A smiley has a mouth which can be ) or D.
___

No other characters are allowed except for those mentioned above.


[Examples]

___
count_smileys([":)", ";(", ";}", ":-D"]) ➞ 2

count_smileys([";D", ":-(", ":-)", ";~)"]) ➞ 3

count_smileys([";]", ":[", ";*", ":$", ";-D"]) ➞ 1
_____



[Notes]

___
*) You will always be given a list as input.
*) An empty list should return 0.
*) The order of each facial element will always be the same.
*) Noses are optional (e.g. :) and :-) are both valid).
___



[loops] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Data Structures
https://docs.python.org/3/tutorial/datastructures.html
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.in …
_________
_________
For Loops in Python
https://wiki.python.org/moin/ForLoop
For loops are traditionally used when you have a block of code which you want to repeat a fixed number of times. The Python for statement iterates over the members of a …
_________

"""
#Your code should go here:

