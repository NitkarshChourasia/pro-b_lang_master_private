/*
####  Self-Descriptive Numbers  ####

The number 10213223 is self-descriptive. Count the number of zeros, ones, twos, and threes that are contained in this number and you have 1 zero, 2 ones, 3 twos, 2 threes, but that is a replica of the number itself 10|21|32|23.
Write a function that returns true if its argument is a self-descriptive number, false if not.


[Examples]

___
selfDescriptive("22") ➞ true

selfDescriptive("3999") ➞ false

selfDescriptive("31331419") ➞ true

selfDescriptive("21321316") ➞ false

selfDescriptive("4132232416171") ➞ false

selfDescriptive("31331819") ➞ true
_____



[Notes]

___
*) Since the number's descriptors are always in pairs, any self-descriptive number must have an even number of digits.
*) The largest self-descriptive number possible is reportedly 71322723161814151019 (see Resources tab).
___



[loops] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Self-Descriptive Numbers
https://www.primepuzzles.net/puzzles/puzz_324.htm
Each digit is "described" at most one time, i.e., I have excluded cases in which there are repeated pairs quantifier-digit.
_________
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Returns a string with the representation of val.
_________
_________
Convert Char to Int
https://stackoverflow.com/questions/5029840/convert-char-to-int-in-c-and-c
a - '0' is equivalent to ((int)a) - ((int)'0'), which means the ascii values of the characters are subtracted from each other.
_________

*/
//Your code should go here:

