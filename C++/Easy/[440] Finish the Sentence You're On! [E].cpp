/*
####  Finish the Sentence You're On!  ####

POV: You are in an exam and time has just run out. While the teacher's back is turned, you hastily take the opportunity to finish scribbling down the last few words of the conclusion.
For this challenge, it takes 0.5 seconds to write a character (not including spaces). Given the full sentence and the unfinished sentence as inputs, return the time it takes to finish writing in seconds.


[Worked Example]

___
timeToFinish(
  "And so brings my conclusion to its conclusion.",
  "And so brings my conclusion to"
) ➞ 7

// "its" has 3 characters
// "conclusion." has 11 characters, including punctuation.
// 11 + 3 = 14
// 14 x 0.5 = 7
// Remember not to include spaces.
_____



[Examples]

___
timeToFinish(
  "And so brings my conclusion to its conclusion.",
  "And so brings my conclusion to its conclus"
) ➞ 2

timeToFinish(
  "As a result, my point is still valid.",
  "As a result, my"
) ➞ 9

timeToFinish(
  "Thank you for reading my essay.",
  "T"
) ➞ 12.5
_____



[Notes]

The unfinished sentence is always found at the start of a complete sentence.


[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
std::setprecision
http://www.cplusplus.com/reference/iomanip/setprecision/
Sets the decimal precision to be used to format floating-point values on output operations. Behaves as if member precision were called with n as argument on the stream …
_________
_________
Removing a Substring from a String
https://www.oreilly.com/library/view/c-cookbook/0596007612/ch04s12.html
You want to remove a substring from a string. Solution Use the find, erase, and length member functions of basic_string …
_________

*/
//Your code should go here:

