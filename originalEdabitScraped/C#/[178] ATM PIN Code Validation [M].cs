/*
####  ATM PIN Code Validation  ####

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. Your task is to create a function that takes a string and returns true if the PIN is valid and false if it's not.


[Examples]

___
ValidatePIN("1234") ➞ true

ValidatePIN("12345") ➞ false

ValidatePIN("a234") ➞ false

ValidatePIN("") ➞ false
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
Int32.TryParse Method (System)
https://docs.microsoft.com/en-us/dotnet/api/system.int32.tryparse?view=netframework-4.8
Converts the string representation of a number to its 32-bit signed integer equivalent. A return value indicates whether the operation succeeded.
_________
_________
IsDigit(Char) (System)
https://docs.microsoft.com/en-gb/dotnet/api/system.char.isdigit?redirectedfrom=MSDN&view=netframework-4.8#System_Char_IsDigit_System_Char_
Indicates whether a Unicode character is categorized as a decimal digit.
_________
_________
Byte.TryParse (System)
https://docs.microsoft.com/en-ca/dotnet/api/system.byte.tryparse?view=netframework-4.7.2#System_Byte_TryParse_System_String_System_Globalization_NumberStyles_System_IFormatProvider_System_Byte__
Tries to convert the string representation of a number to its equivalent, and returns a value that indicates whether the conversion succeeded.
_________
_________
How to match exactly 7 or 9 digits with RegEx?
https://stackoverflow.com/questions/11797897/regular-expressions-match-exactly-7-or-9-digits
My reg ex skills are almost zero and I am trying to match a field to have exactly 7 or 9 numbers (not between 7 or 9 so no 8 numbers is not valid). I have tried (don't …
_________
_________
IsDigit(Char) (System)
https://msdn.microsoft.com/ru-ru/library/7f0ddtxh(v=vs.110).aspx
Indicates whether the specified Unicode character is categorized as a decimal digit.
_________

*/
//Your code should go here:

