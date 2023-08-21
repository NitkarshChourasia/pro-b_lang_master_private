/*
####  Single Letter Swaps  ####

Given an array of strings and an original string, write a function to output an array of zeroes and ones - 1 if the word can be formed from the original word by swapping two letters only once and 0 otherwise.


[Examples]

___
validateSwaps(["BACDE", "EBCDA", "BCDEA", "ACBED"], "ABCDE")
➞ [1, 1, 0, 0]

// Swap "A" and "B" from "ABCDE" to get "BACDE".
// Swap "A" and "E" from "ABCDE" to get "EBCDA".
// Both "BCDEA" and "ACBED" cannot be formed from "ABCDE" using only a single swap.

validateSwaps(["32145", "12354", "15342", "12543"], "12345")
➞ [1, 1, 1, 1]

validateSwaps(["9786", "9788", "97865", "7689"], "9768")
➞ [1, 0, 0, 0]
_____



[Notes]

Original string will consist of unique characters.


[arrays] [loops] [validation] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

