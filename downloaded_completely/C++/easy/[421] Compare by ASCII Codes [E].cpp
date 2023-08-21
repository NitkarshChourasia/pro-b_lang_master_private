/*
####  Compare by ASCII Codes  ####

Create a function that compares two words based on the sum of their ASCII codes and returns the word with the smaller ASCII sum.


[Examples]

___
asciiSort(["hey", "man"]) ➞ "man"
# ["h", "e", "y"] ➞ sum([104, 101, 121]) ➞ 326
# ["m", "a", "n"] ➞ sum([109, 97, 110]) ➞ 316

asciiSort(["majorly", "then"]) ➞ "then"

asciiSort(["victory", "careless"]) ➞ "victory"
_____



[Notes]

Both words will have strictly different ASCII sums.


[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::accumulate
https://en.cppreference.com/w/cpp/algorithm/accumulate
Computes the sum of the given value init and the elements in the range [first, last).
_________
_________
Vectors
https://www.geeksforgeeks.org/vector-in-cpp-stl/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________
_________
ASCII Codes of Characters
http://www.asciitable.com/
Is a character encoding standard for electronic communication. ASCII codes represent text in computers, telecommunications equipment, and other devices. Most modern cha …
_________

*/
//Your code should go here:

