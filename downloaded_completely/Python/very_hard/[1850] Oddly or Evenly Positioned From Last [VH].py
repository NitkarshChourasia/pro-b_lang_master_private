"""
####  Oddly or Evenly Positioned From Last  ####

Create a function that extracts the characters from a list (or a string) on odd or even positions, depending on the specifier. The string "odd" for items on odd positions (... 5, 3, 1) and "even" for even positions (... 6, 4, 2) from the last item of that list or string.


[Examples]

___
char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 4th & 2nd positions from right.

char_at_pos("EDABIT", "odd") ➞ "DBT"
# "D", "B" and "T" occupy the 5th, 3rd and 1st positions from right.

char_at_pos([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "odd") ➞ ["(", "&", "%", "#", "!"]
_____



[Notes]

___
*) Lists are zero-indexed, so, index+1 = position or position-1 = index.
*) Optional: Solve this challenge in a single-line lambda function.
*) A recursive version of this challenge can be found via this link.
___



[algorithms] [arrays] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Indexing and Slicing
https://realpython.com/lessons/indexing-and-slicing/
The elements of a list can be accessed by an index. To do that, you name the list, and then inside of a pair of square brackets you use an index number, like what I’m s …
_________
_________
String Comparison
https://www.thecoderpedia.com/blog/python-string-comparison/
Strings are the set of characters. In Python, String Comparison can be easily performed with the help of Comparison Operator. Like - ==, !=, , = Operator.
_________
_________
Python Lists
https://developers.google.com/edu/python/lists
Python has a great built-in list type named "list". List literals are written within square brackets [ ]. Lists work similarly to strings -- use the len() function and …
_________

"""
#Your code should go here:

