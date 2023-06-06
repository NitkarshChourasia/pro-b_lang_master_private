/*
####  Strange Pair  ####

A pair of strings form a strange pair if both of the following are true:
___
*) The 1st string's first letter = 2nd string's last letter.
*) The 1st string's last letter = 2nd string's first letter.
___

Create a function that returns true if a pair of strings constitutes a strange pair, and false otherwise.


[Examples]

___
IsStrangePair("ratio", "orator") ➞ true
// "ratio" ends with "o" and "orator" starts with "o".
// "ratio" starts with "r" and "orator" ends with "r".

IsStrangePair("sparkling", "groups") ➞ true

IsStrangePair("bush", "hubris") ➞ false

IsStrangePair("", "") ➞ true
_____



[Notes]

It should work on a pair of empty strings (they trivially share nothing).


[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String.StartsWith Method
https://docs.microsoft.com/en-us/dotnet/api/system.string.startswith?view=netframework-4.8
Determines whether the beginning of this string instance matches a specified string.
_________
_________
String.EndsWith Method
https://docs.microsoft.com/en-us/dotnet/api/system.string.endswith?view=netframework-4.8
Determines whether the end of this string instance matches a specified string.
_________
_________
String.IsNullOrEmpty(String) Method
https://docs.microsoft.com/en-us/dotnet/api/system.string.isnullorempty?view=netframework-4.8
Indicates whether the specified string is null or an empty string ("").
_________
_________
First and Last
https://stackoverflow.com/questions/6675561/are-first-and-last-on-ienumerable-really-the-first-and-last
How to not use string indexing. But use First() and Last() methods.
_________

*/
//Your code should go here:

