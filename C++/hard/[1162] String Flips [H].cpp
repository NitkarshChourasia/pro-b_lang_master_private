/*
####  String Flips  ####

Create a function that takes a string as the first argument, and a (string) specification as a second argument. If the specification is "word", return a string with each word reversed while maintaining their original order. If the specification is "sentence", reverse the order of the words in the string, while keeping the words intact.


[Examples]

___
str = "There's never enough time to do all the nothing you want"


flip("Hello", "word") ➞ "olleH"

flip("Hello", "sentence") ➞ "Hello"

flip(str, "word") ➞ "s'erehT reven hguone emit ot od lla eht gnihton uoy tnaw"

flip(str, "sentence") ➞ "want you nothing the all do to time enough never There's"
_____



[Notes]

N/A


[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::reverse_copy
https://en.cppreference.com/w/cpp/algorithm/reverse_copy
Copies the elements from the range [first, last) to another range beginning at d_first in such a way that the elements in the new range are in reverse order.
_________
_________
std::rotate
https://en.cppreference.com/w/cpp/algorithm/rotate
Performs a left rotation on a range of elements. Specifically, std::rotate swaps the elements in the range [first, last) in such a way that the element n_first becomes …
_________
_________
std::basic_stringstream
https://en.cppreference.com/w/cpp/io/basic_stringstream
Implements input and output operations on string based streams. It effectively stores an instance of std::basic_string and performs the input and output operations on it.
_________

*/
//Your code should go here:

