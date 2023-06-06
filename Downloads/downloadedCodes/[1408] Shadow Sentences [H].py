"""
####  Shadow Sentences  ####

Given two sentences, return whether they are shadows of each other. This means that all of the word lengths are the same, but the corresponding words don't share any common letters.


[Examples]

___
shadow_sentence("they are round", "fold two times") ➞ True

shadow_sentence("own a boat", "buy my wine") ➞ False
# No words share common letters, but "a" and "my" have different lengths.

shadow_sentence("his friends", "our company") ➞ False
# Word lengths are the same but "friends" and "company" share the letter "n".

shadow_sentence("salmonella supper", "birthright") ➞ False
# Setences with different numbers of words.
_____



[Notes]

___
*) All sentences will be given in lowercase, and will have no punctuation.
*) Return False if the sentences have different numbers of words.
___



[loops] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Test if Any Two Lists Have Any Elements in Common
https://stackoverflow.com/questions/3170055/test-if-lists-share-any-items-in-python
I want to check if any of the items in one list are present in another list. I can do it simply with the code below, but I suspect there might be a library function to …
_________
_________
String split() Method
https://www.w3schools.com/python/ref_string_split.asp
Splits a string into a list.
_________

"""
#Your code should go here:

