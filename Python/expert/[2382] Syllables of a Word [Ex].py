"""
####  Syllables of a Word  ####

In this challenge, you are tasked to return the syllables of a word in a list. To find a syllables, if one consonant follows a vowel, divide the word between the vowel and the consonant. if two consonants follow a vowel, divide the word between the two consonants. However, when the last letter is "e", if the letter before it is a consonant, it would become a silent letter and would therefore be added to the syllable before instead of being its own syllable.


[Examples]

___
syllable("happy") ➞ ["hap" ,  py"]

syllable("motel") ➞ ["mo" , "tel"]

syllable("pancake") ➞ ["pan" , "cake"]

syllable("dogumaru") ➞ ["do" , "gu" , "ma" , "ru"]

syllable("abbufhafa") ➞ ["ab" , "buf" , "ha" , "fa"]
_____



[Notes]

___
*) Vowels are a, e, i, o, u and y.
*) There will only be a maximun of 2 consonants in a row and one vowel in a row.
___



[algorithms] [logic] [regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

