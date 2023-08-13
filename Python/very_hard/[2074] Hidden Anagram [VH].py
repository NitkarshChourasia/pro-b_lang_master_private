"""
####  Hidden Anagram  ####

Create a function that takes two strings. The first string contains a sentence containing the letters of the second string in a consecutive sequence but in a different order. The hidden anagram must contain all the letters, including duplicates, from the second string in any order and must not contain any other alphabetic characters.
Write a function to find the anagram of the second string embedded somewhere in the first string. You should ignore character case, any spaces, and punctuation marks and return the anagram as a lower case string with no spaces or punctuation marks.


[Examples]

___
hidden_anagram("An old west action hero actor", "Clint Eastwood") ➞ "noldwestactio"
# The sequence "n old west actio" is a perfect anagram of "Clint Eastwood".

hidden_anagram("Mr. Mojo Rising could be a song title", "Jim Morrison") ➞ "mrmojorisin"
# The sequence "Mr. Mojo Risin" ignoring the full stop, is a perfect
# anagram of "Jim Morrison".

hidden_anagram("Banana? margaritas", "ANAGRAM") ➞ "anamarg"
# The sequence "ana? marg" ignoring "?" is a perfect anagram of "Anagram".

hidden_anagram("D  e b90it->?$ (c)a r...d,,#~", "bad credit") ➞ "debitcard"
# When all spaces, numbers and puntuation marks are removed
# from the whole phrase, the remaining characters form the sequence
# "Debitcard" which is a perfect anagram of "bad credit".

hidden_anagram("Bright is the moon", "Bongo mirth") ➞ "noutfond"
# The words "Bright moon" are an anagram of "bongo mirth" but they are
# not a continuous alphabetical sequence because the words "is the" are in
# between. Hence the negative result, "noutfond" is returned.
_____



[Notes]

___
*) A perfect anagram contains all the letters of the original, in any order, no more, no less.
*) If there is no hidden anagram in the sentence, return "noutfond".
*) As in the above examples, the hidden anagram may start or finish part way through a word and/or span multiple words and may contain punctuation marks and other non-alpha characters.
*) Ignore character case and any embedded non-alpha characters.
*) If there is more than 1 result in a sentence, return the nearest to the beginning.
___



[arrays] [formatting] [loops] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
filter() Method
https://www.programiz.com/python-programming/methods/built-in/filter
Constructs an iterator from elements of an iterable for which a function returns true.
_________
_________
sorted() Function
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
Indexing and Slicing for Lists and other Sequential Types
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
Python, one of the most in-demand machine learning languages, supports slice notation for any sequential data type like lists, strings, and others. Discover more about …
_________

"""
#Your code should go here:

