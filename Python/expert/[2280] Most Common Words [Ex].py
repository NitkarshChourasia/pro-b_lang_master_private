"""
####  Most Common Words  ####

This challenge requires you to find the most common words. There will be two leyword arguments passed in text and n. Return the most common words in the form of a dictionary.
text would be the variable containing all the words, while n is a number that means return the top n most common words from text. In case n exceeds the total number of unique words, return the full dictionary of most common words.
text will only contain letters, spaces, and basic punctuation like fullstops, commas, exclamation marks, question marks and apostrophes, which means you would have to split the text into words as well.
In the case of an apostrophe: "where's" would be considered as two words, "where" and "s", and "I'm" would be "i" and "m".
All words in the returned dictionary should be lower case.


[Examples]

___
words = "How much wood could a woodchuck chuck If a woodchuck could chuck wood? As much wood as a woodchuck could chuck, If a woodchuck could chuck wood"

most_common_words(text=words, n=3) ➞ {
  "wood": 4,
  "could": 4,
  "a": 4
}

most_common_words(text=words, n=7) ➞ {
  "wood": 4,
  "could": 4,
  "a": 4,
  "woodchuck": 4,
  "chuck": 4,
  "much": 2,
  "if": 2
}

most_common_words(text=words, n=999) ➞ {
  "wood": 4,
  "could": 4,
  "a": 4,
  "woodchuck": 4,
  "chuck": 4,
  "much": 2,
  "if": 2,
  "as": 2,
  "how": 1
}
_____



[Notes]

In the case of duplicate values (eg. { "word1": 1, "word2": 1 }), their order of appearance should follow their position in the text.
For example:
___
most_common_words("word1, word2", 1) ➞ { "word1": 1 }
most_common_words("word2, word1", 1) ➞ { "word2": 1 }
_____



[algorithms] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Counter
https://pymotw.com/2/collections/counter.html
Is a container that keeps track of how many times equivalent values are added. It can be used to implement the same algorithms for which bag or multiset data structures …
_________
_________
OrderedDict vs dict
https://realpython.com/python-ordereddict/
In this step-by-step tutorial, you'll learn what Python's OrderedDict is and how to use it in your code. You'll also learn about the main differences between regular di …
_________
_________
Dictionaries
https://realpython.com/python-dicts/
You'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, you should have a good sense of when a …
_________
_________
Container datatypes
https://docs.python.org/3.3/library/collections.html#collections.Counter
This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.
_________

"""
#Your code should go here:

