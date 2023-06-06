/*
####  RNA Reverse Complement  ####

Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:
___
original -> complement
"AAA" -> "UUU"
"UUU" -> "AAA"
"GGG" -> "CCC"
"CCC" -> "GGG"
"GGAACC" -> "CCUUGG"
_____

Your function should find the complement on the right AND also reverse the resulting string.


[Examples]

___
reverse_complement("GUGU") ➞ "ACAC"

reverse_complement("UCUCG") ➞ "CGAGA"

reverse_complement("CAGGU") ➞ "ACCUG"
_____



[Notes]

Assume all input seqeuences are valid.


[algorithms] [loops] 



-------------------------------------------------------------------
[Resources]
_________
std::reverse
https://en.cppreference.com/w/cpp/algorithm/reverse
Reverses the order of the elements in the range [first, last).
_________
_________
std::transform
https://en.cppreference.com/w/cpp/algorithm/transform
Applies the given function to a range and stores the result in another range, beginning at d_first.
_________
_________
std::for_each
https://en.cppreference.com/w/cpp/algorithm/for_each
Applies the given function object f to the result of dereferencing every iterator in the range [first, last), in order.
_________

*/
//Your code should go here:

