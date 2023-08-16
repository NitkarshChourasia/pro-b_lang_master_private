/*
####  Fix the Error: Vowel Edition  ####

Your friend is trying to write a function that removes all vowels from a string. They write:
___
std::string removeVowels(std::string text) {
  std::regex vowels("[aiou]");
  std::stringstream result;
  std::regex_replace(std::ostream_iterator<char>(result), text.begin(), text.end(), vowels, "");
  return result.str();
}
_____

However, it seems that it doesn't work? Fix your friend's code so that it actually does remove all vowels.


[Examples]

___
removeVowels("candy") ➞ "cndy"

removeVowels("hello") ➞ "hell"
// The "o" is removed, but the "e" is still there!

removeVowels("apple") ➞ "pple"
_____



[Notes]

All letters will be lowercase.


[bugs] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::regex_replace
http://www.enseignement.polytechnique.fr/informatique/INF478/docs/Cpp/en/cpp/regex/regex_replace.html
Uses a regular expression to perform substitution on a sequence of characters: 1) Copies characters in the range [first,last) to out, replacing any sequences that matc …
_________

*/
//Your code should go here:

