"""
####  Is Edabit in the String?  ####

A string contains the word "edabit" if a subsequence of its characters spell "edabit".
Write a function that accepts a string and returns “YES” if the string contains a subsequence of the word edabit or "NO" if it does not.


[Examples]

___
edabit_in_string(“eddaaabt”) ➞ “NO”

edabit_in_string(“edwardisabletodoit”) ➞ “YES”

edabit_in_string(“abecdfghijklmnopqrstuvwxyz”) ➞ “NO”
_____



[Notes]

Check the Resources tab for more details on subsequence.


[strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Subsequence
https://en.wikipedia.org/wiki/Subsequence
A sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. For example, the sequence A, …
_________
_________
Finding subsequence (nonconsecutive)
https://stackoverflow.com/questions/29954748/finding-subsequence-nonconsecutive
Using an iterator trick: it = iter(haystack) all(x in it for x in needle) This is only a concise version of the same idea presented in another answer.
_________

"""
#Your code should go here:

