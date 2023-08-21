/*
####  Is This a Haiku?  ####

Haikus are poems formed by three lines of 5, 7, and 5 syllables. Your task is to write a function that determines if a given poem scans as a Haiku.
How to count syllables:
___
*) Every syllable must contain at least one vowel.
*) If two or more vowels appear back to back, they should be counted as a single vowel (e.g. "fair").
*) If an "e" appears at the end of a word, it shouldn't be counted, as those aren't usually pronounced. That extends to words ending in es or e's.
*) An exception to the previous point is a word whose only vowel appears at the end (e.g. "the" or "She's").
*) "Y" counts as a vowel.
___



[Examples]

___
haiku("New vids ev'ry day / Never skipped a single day / I'll see you in March") ➞ true

haiku("Delightful display / Snowdrops bow their pure white heads / To the sun's glory") ➞ true

haiku("Superman's my fav / Wonder Woman is pretty dope / Don't forget Rorschach") ➞ false
_____



[Notes]

___
*) Each new line of the poem will be marked with a /.
*) You may find commas, apostrophes, and other punctuation marks.
___



[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
Syllable Counter - Count syllables for a word or sentence
https://syllablecounter.net/count
Syllable Counter is a free online tool that helps you count the total number of syllables for any word or sentences, per line for haiku poems.
_________

*/
//Your code should go here:

