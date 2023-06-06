/*
####  Lexicographically First and Last  ####

Write a function that returns the lexicographically first and lexicographically last rearrangements of a lowercase string. Output the results in the following manner:
___
firstAndLast(string) ➞ [first, last]
_____



[Examples]

___
firstAndLast("marmite") ➞ ["aeimmrt", "trmmiea"]

firstAndLast("bench") ➞ ["bcehn", "nhecb"]

firstAndLast("scoop") ➞ ["coops", "spooc"]
_____



[Notes]

___
*) Lexicographically first: the permutation of the string that would appear first in the English dictionary (if the word existed).
*) Lexicographically last: the permutation of the string that would appear last in the English dictionary (if the word existed).
___



[arrays] [sorting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::sort
http://www.cplusplus.com/reference/algorithm/sort/
Sorts the elements in the range [first,last) into ascending order.
_________
_________
std::sort()
https://www.geeksforgeeks.org/sort-c-stl/
We have discussed qsort() in C. C++ STL provides a similar function sort that sorts a vector or array (items with random access) It generally takes two parameters, the …
_________
_________
std::lexicographical_compare
http://www.cplusplus.com/reference/algorithm/lexicographical_compare/
Returns true if the range [first1, last1) compares lexicographically less than the range [first2, last2).
_________

*/
//Your code should go here:

