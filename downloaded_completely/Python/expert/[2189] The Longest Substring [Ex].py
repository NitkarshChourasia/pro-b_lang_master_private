"""
####  The Longest Substring  ####

Given a string of letters, create a function that returns a list with the separator that yields the longest possible substring, provided that:
___
*) The substring starts and ends with the separator.
*) The separator doesn't occur inside the substring other than at the ends.
___

If two or more separators yield substrings with the same length, they should appear in alphabetical order.


[Examples]

___
max_separator("supercalifragilistic") ➞ ["s"]
# The longest substring is "supercalifragilis".

max_separator("laboratory") ➞ ["a", "o", "r"]
# "abora", "orato" and "rator" are the same length.

max_separator("candle") ➞ []
# No possible substrings.
_____



[Notes]

___
*) All substrings should be at least of length 2 (i.e. no single-letter substrings).
*) Expect lowercase alphabetic characters only.
___



[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Lookahead and Lookbehind
https://www.rexegg.com/regex-lookarounds.html
Explains the fine details of Lookahead and Lookbehind, including zero-width matches, overlapping matches and atomicity.
_________
_________
Backreferences To Match The Same Text Again
https://www.regular-expressions.info/backref.html
Backreferences match the same text as previously matched by a capturing group. Suppose you want to match a pair of opening and closing HTML tags, and the text in betwee …
_________

"""
#Your code should go here:

