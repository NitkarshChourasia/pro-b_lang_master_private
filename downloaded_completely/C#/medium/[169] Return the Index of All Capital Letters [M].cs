/*
####  Return the Index of All Capital Letters  ####

Create a function that takes a single string as argument and returns an ordered array containing the indices of all capital letters in the string.


[Examples]

___
IndexOfCapitals("eDaBiT") ➞ [1, 3, 5]

IndexOfCapitals("eQuINoX") ➞ [1, 3, 4, 6]

IndexOfCapitals("determine") ➞ []

IndexOfCapitals("STRIKE") ➞ [0, 1, 2, 3, 4, 5]

IndexOfCapitals("sUn") ➞ [1]
_____



[Notes]

___
*) Return an empty array if no uppercase letters are found in the string.
*) Special characters ($#@%) and numbers will be included in some test cases.
*) Assume all words do not have duplicate letters.
___



[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
ToCharArray Method
https://www.dotnetperls.com/tochararray
This method converts strings to character arrays. It is called on a string and returns a new char array. The original string is left unchanged.
_________
_________
Char.IsUpper Method (System)
https://docs.microsoft.com/en-us/dotnet/api/system.char.isupper?redirectedfrom=MSDN&view=netframework-4.7.2
Indicates whether a Unicode character is categorized as an uppercase letter.
_________
_________
List Class (System.Collections.Generic)
https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=netframework-4.8
Represents a strongly typed list of objects that can be accessed by index. Provides methods to search, sort, and manipulate lists.
_________
_________
List.ToArray Method (System.Collections.Generic)
https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1.toarray?view=netframework-4.8
Copies the elements of the to a new array.
_________
_________
String.IndexOf Method (System)
https://docs.microsoft.com/en-us/dotnet/api/system.string.indexof?view=netframework-4.8
Reports the zero-based index of the first occurrence of a specified Unicode character or string within this instance. The method returns -1 if the character or string i …
_________
_________
String.IndexOf Method (System)
https://docs.microsoft.com/en-us/dotnet/api/system.string.indexof?redirectedfrom=MSDN&view=netframework-4.7.2#System_String_IndexOf_System_String_
Reports the zero-based index of the first occurrence of a specified Unicode character or string within this instance. The method returns -1 if the character or string i …
_________
_________
Find Index of the First Uppercase Character
https://stackoverflow.com/questions/10257711/find-index-of-the-first-uppercase-character
As a C# Novice, currently to find out the index of the first uppercase character in a string I have figured out a way. Functionally the code works fine except that I wa …
_________

*/
//Your code should go here:

