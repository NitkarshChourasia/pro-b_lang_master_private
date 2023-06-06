"""
####  Substituting the The  ####

Create a function that replaces "the" in the sentence with "an" or "a". Remember that if the next word begins with a vowel, use "an". In the case of a consonant, use "a".


[Examples]

___
replace_the("the dog and the envelope") ➞ "a dog and an envelope"

replace_the("the boy ran at the wall") ➞ "a boy ran at a wall"

replace_the("the egg, the spoon and the espionage") ➞ "an egg, a spoon and an espionage"
_____



[Notes]

___
*) Sentences will always be in lowercase.
*) The last word of the sentence will never be "the".
*) This won't cover edge cases such as "an hour" or "a unique thing" (since they sound differently to the rule).
___



[formatting] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________
_________
Regular Expression Operations
https://docs.python.org/3/library/re.html
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________
_________
re.sub() Function
https://www.kite.com/python/answers/how-to-use-re.sub()-in-python
Is used to replace substrings in strings.
_________

"""
#Your code should go here:

