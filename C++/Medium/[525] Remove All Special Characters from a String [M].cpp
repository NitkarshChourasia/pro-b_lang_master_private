/*
####  Remove All Special Characters from a String  ####

Create a function that takes a string, removes all "special" characters (e.g. ., !, @, #, $, %, ^, &, \, *, (, )) and returns the new string. The only non-alphanumeric characters allowed are dashes -, underscores _ and spaces.


[Examples]

___
removeSpecialCharacters("The quick brown fox!") ➞ "The quick brown fox"

removeSpecialCharacters("%fd76$fd(-)6GvKlO.") ➞ "fd76fd-6GvKlO"

removeSpecialCharacters("D0n$c sed 0di0 du1") ➞ "D0nc sed 0di0 du1"
_____



[Notes]

N/A


[arrays] [formatting] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Erase–remove idiom
https://en.wikipedia.org/wiki/Erase%E2%80%93remove_idiom
The erase–remove idiom is a common C++ technique to eliminate elements that fulfill a certain criterion from a C++ Standard Library container.
_________
_________
std::remove, std::remove_if
https://en.cppreference.com/w/cpp/algorithm/remove
Removes all elements satisfying specific criteria from the range [first, last) and returns a past-the-end iterator for the new end of the range.
_________
_________
std::isalnum
https://en.cppreference.com/w/cpp/string/byte/isalnum
Checks if the given character is an alphanumeric character as classified by the current C locale. In the default locale, the following characters are alphanumeric.
_________

*/
//Your code should go here:

