"""
####  Farthest Hamming Anagrams  ####

An anagram is a word, x, formed by rearranging the letters that make up another word, y, and using up all the letters in y at the same frequency. For example, "dear" is an anagram of "read" and "plead" is an anagram of "paled".
The Hamming distance between two strings is the number of positions at which they differ. Hamming distances can only be calculated for strings of equal length.
___
s1 = "eleven"

s2 = "twelve"
_____

They only have the third position (index 2) in common, giving them a Hamming distance of 5.
As anagrams are of identical length, the Hamming distance between them can be calculated.
___
s1 = "read"

s2 = "dear"
_____

These strings differ at the first and last positions, giving them a Hamming distance of 2. "Plead" and "paled" have a Hamming distance of 3.
Create a function that takes two strings, and returns:
___
*) True if they are anagrams of each other and their Hamming distance is equal to their length (i.e. no letters in the same positions).
*) False if they aren't anagrams, or
*) Their Hamming distance if they are anagrams with >=1 letter at the same index.
___



[Examples]

___
max_ham("dear", "read") ➞ 2

max_ham("dare", "read") ➞ True

max_ham("solemn", "molest") ➞ False
_____



[Notes]

N/A


[conditions] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
Learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables in parallel and create dictionaries wit …
_________
_________
Check Whether Two Strings Are Anagram of Each Other
https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
Write a function to check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, only the o …
_________
_________
Hamming Distance
https://www.geeksforgeeks.org/hamming-distance-two-strings/
Article on how to calculate the hamming distance between two strings.
_________

"""
#Your code should go here:

