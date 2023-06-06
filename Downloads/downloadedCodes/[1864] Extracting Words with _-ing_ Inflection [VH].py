"""
####  Extracting Words with "-ing" Inflection  ####

Write a function that takes a string as an argument and returns a list of all the words inflected by "-ing". Your function should also exclude all the mono-syllabic words ending in "-ing" (e.g. bing, sing, sling, ...). Although these words end in "-ing", the "-ing" is not an inflection affix.


[Examples]

___
ing_extractor("coming bringing Letting sing") ➞ ["coming", "bringing", "Letting"]

ing_extractor("going Ping, king sHrink dOing") ➞ ["going", "dOing"]

ing_extractor("zing went ring, ding wing SINk") ➞ []
_____



[Notes]

___
*) Mono-syllabic means a word containing just one syllable.
*) It's probably best to use RegEx for this challenge.
___



[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
RegEx
https://www.programiz.com/python-programming/regex
In this tutorial, you will learn about regular expressions (RegEx), and use Python's re module to work with RegEx (with the help of examples).
_________
_________
Regexes
https://realpython.com/regex-python/
In previous tutorials in this series, you've seen several different ways to compare string values with direct character-by-character comparison. In this tutorial, you'l …
_________
_________
Regex Tester and Debugger
https://regex101.com
With highlighting for PHP, PCRE, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

