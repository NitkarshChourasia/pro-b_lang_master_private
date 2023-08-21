/*
####  Next Largest Number  ####

Write a function that returns the next number that can be created from the same digits as the input.


[Examples]

___
nextNumber(19) ➞ 91

nextNumber(3542) ➞ 4235

nextNumber(5432) ➞ 5432

nextNumber(58943) ➞ 59348
_____



[Notes]

___
*) If no larger number can be formed, return the number itself.
*) Bonus: See if you can do this without generating all digit permutations.
___



[numbers] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
std::next_permutation
https://en.cppreference.com/w/cpp/algorithm/next_permutation
Permutes the range [first, last) into the next permutation, where the set of all permutations is ordered lexicographically with respect to operator< or comp.
_________
_________
std::to_string
https://en.cppreference.com/w/cpp/string/basic_string/to_string
Converts a numeric value to std::string.
_________
_________
std::stoi, std::stol, std::stoll
https://en.cppreference.com/w/cpp/string/basic_string/stol
Interprets a signed integer value in the string str.
_________
_________
Next Lexicographical Permutation Algorithm
https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
Suppose we have a finite sequence of numbers like (0, 3, 3, 5, 8), and want to generate all its permutations. What is the best way to do so? The naive way would be to t …
_________

*/
//Your code should go here:

