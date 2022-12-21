/*
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
syllabification("tesh") ➞ "tesh"

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
*) You can also solve this challenge using RegEx (easily if you are familiar with).
___



[Hint]

Since each syllable has only one vowel, it's not necessary to know the consonants. Just knowing that there is only one consonant before the vowel and 0 to 2 consonants after the vowel is enough to solve the challenge.


[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
The isVowel Method Which Determines if a Letter Is a Vowel
https://stackoverflow.com/questions/9154027/java-writing-a-syllable-counter-based-on-specifications
Each group of adjacent vowels (a, e, i, o, u, y) counts as one syllable (for example, the "ea" in "real" contributes one syllable, but the "e...a" in "regal" counts as …
_________
_________
How to Count Syllables in Word
https://www.reddit.com/r/Hyperskill/comments/gdwg0u/how_to_count_syllables_in_word_using_java_any/
To count the number of syllables you should use letters a, e, i, o, u, y as vowels.
_________

*/
//Your code should go here:

