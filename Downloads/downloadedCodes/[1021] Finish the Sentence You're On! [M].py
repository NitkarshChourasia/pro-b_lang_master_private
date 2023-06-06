"""
####  Finish the Sentence You're On!  ####

POV: You are in an exam and time has just run out. While the teacher's back is turned, you hastily take the opportunity to finish scribbling down the last few words of the conclusion.
For this challenge, it takes 0.5 seconds to write a character (not including spaces). Given the full sentence and the unfinished sentence as inputs, return the time it takes to finish writing in seconds.


[Worked Example]

___
time_to_finish(
  "And so brings my conclusion to its conclusion.",
  "And so brings my conclusion to"
) ➞ 7

# "its" has 3 characters
# "conclusion." has 11 characters, including punctuation.
# 11 + 3 = 14
# 14 x 0.5 = 7
# Remember not to include spaces.
_____



[Examples]

___
time_to_finish(
  "And so brings my conclusion to its conclusion.",
  "And so brings my conclusion to its conclus"
) ➞ 2

time_to_finish(
  "As a result, my point is still valid.",
  "As a result, my"
) ➞ 9

time_to_finish(
  "Thank you for reading my essay.",
  "T"
) ➞ 12.5
_____



[Notes]

The unfinished sentence is always found at the start of a complete sentence.


[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
rfind() Method
https://www.w3schools.com/python/ref_string_rfind.asp
Finds the last occurrence of the specified value. The rfind() method returns -1 if the value is not found. The rfind() method is almost the same as the rindex() method.
_________
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string. A string must be specified as the separator.
_________
_________
split() Method
https://www.w3schools.com/python/ref_string_split.asp
Splits a string into a list. You can specify the separator, default separator is any whitespace.
_________

"""
#Your code should go here:

