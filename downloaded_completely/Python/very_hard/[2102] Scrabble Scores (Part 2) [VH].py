"""
####  Scrabble Scores (Part 2)  ####

This challenge is based on the game Scrabble. Each word you play is scored based on the point value of each tile/letter (see first table), as well as additional points conferred by any special squares your tiles land on (see second table).
Create a function that takes a list representing a row of squares in a Scrabble board, and a string representing the word to be played. The list will consist of - representing normal squares, and "DL", "TL", "DW" representing special squares. Return the index of the list where the first letter of the word should be placed to maximise the score of the word to be played. Return the lowest index, if several exist.




[Examples]

___
best_start(["-","DW","-","-","-","TL","-","-","-","TL","-","-","-","DW","-"], "quiz") ➞ 0
# Doubling the entire word maximises the score. Starting at
# indices 1,10, and 11 have the same effect, but the function
# should return the lowest index.

best_start(["-","DW","-","-","-","TL","-","-","-","TL","-","-","-","DW","-"], "quit") ➞ 5
# Tripling the first letter alone gives a higher score than
# doubling the entire word, as the other 3 letters have
# low point-values.

best_start(["-","DW","-","-","-","TL","-","-","-","TL","-","-","-","DW","-"], "quart") ➞ 9
# Tripling the first (high-scoring) letter, and doubling the word.

best_start(["-","DW","-","-","-","TL","-","-","-","TL","-","-","-","DW","-"], "quartz") ➞ 0
# Tripling the last (high-scoring) letter, and doubling the word.
# Index 9 has the same effect (tripling the first letter, doubling
# the word), but 0 is the lower index.
_____



[Notes]

N/A


[algorithms] [conditions] [games] 



-------------------------------------------------------------------
[Resources]
_________
Sorting Mini-HOW TO
https://wiki.python.org/moin/HowTo/Sorting
Python lists have a built-in sort() method that modifies the list in-place and a sorted() built-in function that builds a new sorted list from an iterable. There are ma …
_________

"""
#Your code should go here:

