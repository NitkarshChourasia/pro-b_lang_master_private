"""
####  Syllabification  ####

The syllabic structure of the Persian language is CV(C)(C). C stands for Consonants and V stands for Vowels. The CV(C)(C) means that there are three types of syllables in Persian:
___
*) CV
*) CVC
*) CVCC
___

Write a function that takes the phonetic transcription of a Persian word as an argument and returns the syllabified word based on the syllabic structure. In other words, put a period between syllables.


[Examples]

___
syllabification("kAr") ➞ "kAr"

syllabification("bArAn") ➞ "bA.rAn"

syllabification("tA") ➞ "tA"

syllabification("deraxt") ➞ "de.raxt"

syllabification("pust") ➞ "pust"

syllabification("lAjevard") ➞ "lA.je.vard"
_____



[Notes]

___
*) Mono-syllabic words don't need syllabification.
*) Persian has six vowels: a, A, e, i, o, u
*) Persian has 23 consonants: p, b, t, d, k, g, G, ?, f, v, s, z, S, Z, x, h, c, j, m, n, r, l, y
*) Try to solve the problem by using RegEx.
___



[Hint]

Since each syllable has only one vowel, it's not necessary to know the consonants. Just knowing that there is only one consonant before the vowel and 0 to 2 consonants after the vowel is enough to solve the challenge.


[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Tutorial: Python Regex (Regular Expressions) for Data Scientists
https://www.dataquest.io/blog/regular-expressions-data-scientists/
Diving headlong into data sets is a part of the mission for anyone working in data science. Often, this means number-crunching, but what do we do when our data set is p …
_________
_________
Capturing Groups and Backreferences
https://www.regular-expressions.info/refcapture.html
Backreferences match the same text as previously matched by a capturing group.
_________
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

