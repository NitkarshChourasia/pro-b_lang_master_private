"""
####  Most Common Last Vowel  ####

Create a function that takes in a sentence as input and returns the most common last vowel in the sentence as a single character string.


[Examples]

___
common_last_vowel("Hello World!") ➞ "o"

common_last_vowel("Watch the characters dance!") ➞ "e"

common_last_vowel("OOI UUI EEI AAI") ➞ "i"
_____



[Notes]

___
*) There will only be one common last vowel in each sentence.
*) If the word has one vowel, treat the vowel as the last one even if it is at the start of the word.
*) The question asks you to compile all of the last vowels of each word and returns the vowel in the list which appears most often.
*) y won't count as a vowel.
*) Return outputs in lowercase.
___



[algorithms] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Find the Last Vowel in a String
https://stackoverflow.com/questions/46406958/find-the-last-vowel-in-a-string
You can reverse your string, and use itertools.takewhile to take everything until the "last" (now the first after reversal) vowel.
_________
_________
Counting Elements in a List
https://www.geeksforgeeks.org/enumerate-in-python/
Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. This enumerated object can then be used directly for loops or converted …
_________

"""
#Your code should go here:

