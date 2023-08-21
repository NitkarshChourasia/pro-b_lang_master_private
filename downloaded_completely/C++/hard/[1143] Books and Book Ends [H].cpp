/*
####  Books and Book Ends  ####

Suppose a pair of identical characters serve as book ends for all characters in between them. Write a function that returns the total number of unique characters (books, so to speak) between all pairs of book ends.
The function will look like:
___
countUniqueBooks("stringSequence", "bookEnd")
_____



[Examples]

___
countUniqueBooks("AZYWABBCATTTA", 'A') ➞ 4

// 1st bookend group: "AZYWA" : 3 unique books: "Z", "Y", "W"
// 2nd bookend group: "ATTTA": 1 unique book: "T"

countUniqueBooks("$AA$BBCATT$C$$B$", '$') ➞ 3

countUniqueBooks("ZZABCDEF", 'Z') ➞ 0
_____



[Notes]

___
*) No book characters will be identical to the bookend character.
*) There will always be an even number of bookends.
*) Return 0 if bookends contain zero books.
___



[higher_order_functions] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
C++ Strings
https://www.tutorialspoint.com/cplusplus/cpp_strings.htm
The C-style character string originated within the C language and continues to be supported within C++. This string is actually a one-dimensional array of characters wh …
_________

*/
//Your code should go here:

