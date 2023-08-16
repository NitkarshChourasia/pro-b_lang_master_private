"""
####  Find an Anagram of a String in Another String  ####

Create a function that takes two strings and determines if an anagram of the first string is in the second string. Anagrams of "bag" are "bag", "bga", "abg", "agb", "gab", "gba". Since none of those anagrams are in "grab", the answer is false. A "g", "a", and "b" are in the string "grab", but they're split up by the "r".


[Examples]

___
ana_str_str("car", "race") ➞ True

ana_str_str("nod", "done") ➞ True

ana_str_str("bag", "grab") ➞ False
_____



[Notes]

___
*) Inputs will be valid strings in all lowercase letters.
*) There exists a linear time algorithm for this.
___



[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Anagram Substring Search (search for all permutations)
https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] and its permutations (or anagra …
_________
_________
Anagram
https://en.wikipedia.org/wiki/Anagram
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.[1] For example, t …
_________

"""
#Your code should go here:

