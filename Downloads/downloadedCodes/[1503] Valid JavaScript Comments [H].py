"""
####  Valid JavaScript Comments  ####

In JavaScript, there are two types of comments:

The input will be a sequence of //, /* and */. Every /* must have a */ that immediately follows it. To add, there can be no single-line comments in between multi-line comments in between the /* and */.
Create a function that returns True if comments are properly formatted, and False otherwise.


[Examples]

___
comments_correct("//////") ➞ True
# 3 single-line comments: ["//", "//", "//"]

comments_correct("/**//**////**/") ➞ True
# 3 multi-line comments + 1 single-line comment:
# ["/*", "*/", "/*", "*/", "//", "/*", "*/"]

comments_correct("///*/**/") ➞ False
# The first /* is missing a */

comments_correct("/////") ➞ False
# The 5th / is single, not a double //
_____



[Notes]

N/A


[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Break A List Into N-Sized Chunks
https://chrisalbon.com/python/data_wrangling/break_list_into_chunks_of_equal_size/
In this snippet we take a list and break it up into n-size chunks. This is a very common practice when dealing with APIs that have a maximum request size.
_________

"""
#Your code should go here:

