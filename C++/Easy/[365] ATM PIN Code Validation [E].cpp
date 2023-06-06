/*
####  ATM PIN Code Validation  ####

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. Your task is to create a function that takes a string and returns true if the PIN is valid and false if it's not.


[Examples]

___
validatePIN("1234") ➞ true

validatePIN("12345") ➞ false

validatePIN("a234") ➞ false

validatePIN("") ➞ false
_____



[Notes]

___
*) Some test cases contain special characters.
*) Empty strings must return false.
___



[regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::regex_match
http://www.cplusplus.com/reference/regex/regex_match/
Returns whether the target sequence matches the regular expression rgx. The target sequence is either s or the character sequence between first and last, depending on t …
_________
_________
std::count()
https://www.geeksforgeeks.org/std-count-cpp-stl/
Returns number of occurrences of an element in a given range. Returns the number of elements in the range [first,last) that compare equal to val.
_________
_________
isalpha() and isdigit()
https://www.geeksforgeeks.org/isalpha-isdigit-functions-c-example/
Can be used to check if the passed character is an alphabet or not. It returns a non-zero value if it’s an alphabet else it returns 0. For example, it returns non-zero …
_________

*/
//Your code should go here:

