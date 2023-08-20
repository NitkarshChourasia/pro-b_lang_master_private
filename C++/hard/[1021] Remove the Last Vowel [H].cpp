/*
####  Remove the Last Vowel  ####

Write a function that removes the last vowel in each word in a sentence.


[Examples]

___
removeLastVowel("Those who dare to fail miserably can achieve greatly.")
➞ "Thos wh dar t fal miserbly cn achiev gretly."

removeLastVowel("Love is a serious mental disease.")
➞ "Lov s  serios mentl diseas"

removeLastVowel("Get busy living or get busy dying.")
➞ "Gt bsy livng r gt bsy dyng"
_____



[Notes]

Vowels are: a, e, i, o, u (both upper and lowercase).


[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::tolower
https://en.cppreference.com/w/cpp/string/byte/tolower
Converts the given character to lowercase according to the character conversion rules defined by the currently installed C locale.
_________
_________
std::basic_string<CharT,Traits,Allocator>::erase
https://en.cppreference.com/w/cpp/string/basic_string/erase
Removes specified characters from the string.
_________
_________
std::remove, std::remove_if
https://en.cppreference.com/w/cpp/algorithm/remove
Removes all elements satisfying specific criteria from the range [first, last) and returns a past-the-end iterator for the new end of the range.
_________

*/
//Your code should go here:

