"""
####  Find the Pattern  ####

___
*) Given a dictionary containing up to six phrases, return a list containing the matching phrases according to the given string (p).
*) Ignore any digit that is placed after or before the given string.
*) Whether the first letter is capitalized or not, if all letters of the word match the given string (p), it is valid.
*) If it does not match the given string (p) then None.
___



[Examples]

___
find_pattern({
  "Phrase1": "COVID-19 is no good",
  "Phrase2": "COVID-18 is no good",
  "Phrase3": "COVID-17 is no good"
}, "COVID-19")

➞ ["Phrase1 = COVID-19", "Phrase2 = None", "Phrase3 = None"]
_____

___
find_pattern({
  "Phrase1": "Edabit is great",
  "Phrase2": "Edabit is very great",
  "Phrase3": "Edabit is really great"
}, "really")

➞ ["Phrase1 = None", "Phrase2 = None", "Phrase3 = really"]
_____



[Notes]

If you are stuck, check the Resources.


[arrays] [formatting] [objects] [scope] 



-------------------------------------------------------------------
[Resources]
_________
Regex
https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285
Are extremely useful in extracting information from any text by searching for one or more matches of a specific search pattern (i.e. a specific sequence of ASCII or uni …
_________
_________
sorted() Function
https://www.w3schools.com/python/ref_func_sorted.asp#:~:text=The%20sorted()%20function%20returns,string%20values%20AND%20numeric%20values.
Returns a sorted list of the specified iterable object.
_________

"""
#Your code should go here:

