/*
####  Spoonerisms  ####

A spoonerism is when the first letters / sounds of two words are transposed onto one another. Create a function that takes a two-word string and performs a spoonerism on the phrase.


[Examples]

___
spoonerise("history lecture") ➞ "listory hecture"

spoonerise("loud noises") ➞ "noud loises"

spoonerise("chow mein") ➞ "mow chein"

spoonerise("edabit rules!") ➞ "redabit ules!"
_____



[Notes]

___
*) Only two words will be parsed into the function. Don't worry about handling more than two.
*) You won't always just have to swap the first letters, take care to notice which letters have been switched in the examples (notice the difference between vowel-starting and consonant-starting words).
___



[conditions] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::find, std::find_if, std::find_if_not
https://en.cppreference.com/w/cpp/algorithm/find
Returns the first element in the range [first, last) that satisfies specific criteria.
_________
_________
std::basic_string<CharT,Traits,Allocator>::find
https://en.cppreference.com/w/cpp/string/basic_string/find
Finds the first substring equal to the given character sequence. Search begins at pos, i.e. the found substring must not begin in a position preceding pos.
_________

*/
//Your code should go here:

