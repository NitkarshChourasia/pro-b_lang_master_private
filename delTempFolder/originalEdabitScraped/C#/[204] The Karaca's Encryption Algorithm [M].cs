/*
####  The Karaca's Encryption Algorithm  ####

Make a function that encrypts a given input with these steps:
Input: "apple"
Step 1: Reverse the input: "elppa"
Step 2: Replace all vowels using the following chart:
___
a => 0
e => 1
i => 2
o => 2
u => 3

// "1lpp0"
_____

Step 3: Add "aca" to the end of the word: "1lpp0aca"
Output: "1lpp0aca"


[Examples]

___
Encrypt("banana") ➞ "0n0n0baca"

Encrypt("karaca") ➞ "0c0r0kaca"

Encrypt("burak") ➞ "k0r3baca"

Encrypt("alpaca") ➞ "0c0pl0aca"
_____



[Notes]

All inputs are strings, no uppercases and all output must be strings.


[algorithms] [cryptography] [formatting] [regex] 



-------------------------------------------------------------------
[Resources]
_________
String.IndexOf Method
https://docs.microsoft.com/en-us/dotnet/api/system.string.indexof?view=netframework-4.8
Reports the zero-based index of the first occurrence of a specified Unicode character or string within this instance. The method returns -1 if the character or string i …
_________
_________
String.Contains Method
https://docs.microsoft.com/en-us/dotnet/api/system.string.contains?view=netframework-4.8
Returns a value indicating whether a specified character occurs within this string, using the specified comparison rules.
_________
_________
String.Substring Method
https://docs.microsoft.com/en-us/dotnet/api/system.string.substring?view=netframework-4.8
Retrieves a substring from this instance. This member is overloaded. For complete information about this member, including syntax, usage, and examples, click a name in …
_________
_________
foreach statement
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/foreach-in
The foreach statement executes a statement or a block of statements for each element in an instance of the type that implements the System.Collections.IEnumerable or Sy …
_________

*/
//Your code should go here:

