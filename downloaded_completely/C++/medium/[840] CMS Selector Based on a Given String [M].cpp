/*
####  CMS Selector Based on a Given String  ####

Write a function that takes an array of strings and a pattern (string) and returns the strings that contain the pattern in alphabetical order. If the pattern is an empty string, return all the strings passed in the input array.


[Examples]

___
cmsSelector(["WordPress", "Joomla", "Drupal"], "w") ➞ ["WordPress"]

cmsSelector(["WordPress", "Joomla", "Drupal", "Magento"], "ru") ➞ ["Drupal"]

cmsSelector(["WordPress", "Joomla", "Drupal", "Magento"], "") ➞ ["Drupal", "Joomla", "Magento", "WordPress"]
_____



[Notes]

___
*) The given letter(s) are case sensitive and can be more than one.
*) In the case of an empty string, return the entire array.
*) A CMS is a Content Management System.
___



[arrays] [formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
string::empty
http://www.cplusplus.com/reference/string/string/empty/
Tests if string is empty.
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
std::string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments. When pos is specified, the search only includes characters at or after positio …
_________
_________
std::copy, std::copy_if
https://en.cppreference.com/w/cpp/algorithm/copy
Copies the elements in the range, defined by [first, last), to another range beginning at d_first. 1) Copies all elements in the range [first, last) starting from firs …
_________

*/
//Your code should go here:

