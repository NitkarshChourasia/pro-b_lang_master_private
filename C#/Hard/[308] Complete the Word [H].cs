/*
####  Complete the Word  ####

An input string can be completed if additional letters can be added and no letters need to be taken away to match the word. Furthermore, the order of the letters in the input string must be the same as the order of letters in the final word.
Create a function that, given an input string, determines if the word can be completed.


[Examples]

___
CanComplete("butl", "beautiful") ➞ true
// We can add "ea" between "b" and "u", and "ifu" between "t" and "l".

CanComplete("butlz", "beautiful") ➞ false
// "z" does not exist in the word beautiful.

CanComplete("tulb", "beautiful") ➞ false
// Although "t", "u", "l" and "b" all exist in "beautiful", they are incorrectly ordered.

CanComplete("bbutl", "beautiful") ➞ false
// Too many "b"s, beautiful has only 1.
_____



[Notes]

Both string input and word will be lowercased.


[loops] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
System.Text.RegularExpressions Namespace
https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions?view=netframework-4.8
The System.Text.RegularExpressions namespace contains classes that provide access to the .NET Framework regular expression engine. The namespace provides regular expres …
_________
_________
RegExr: Learn, Build, & Test RegEx
https://regexr.com/
Regular expression tester with syntax highlighting, PHP / PCRE & JS Support, contextual help, cheat sheet, reference, and searchable community patterns.
_________

*/
//Your code should go here:

