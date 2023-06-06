/*
####  Mangle the String  ####

Create a function that takes a string and replaces every letter with the letter following it in the alphabet ("c" becomes "d", "z" becomes "a", "b" becomes "c", etc). Then capitalize every vowel (a, e, i, o, u) and return the new modified string.


[Examples]

___
Mangle("Fun times!") ➞ "GvO Ujnft!"

Mangle("The quick brown fox.") ➞ "UIf rvjdl cspxO gpy."

Mangle("Omega") ➞ "Pnfhb"
_____



[Notes]

___
*) If a letter is already uppercase, return it as uppercase (regardless of being a vowel).
*) "y" is not considered a vowel.
___



[formatting] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Char.IsLetter Method (System)
https://docs.microsoft.com/en-us/dotnet/api/system.char.isletter?view=netcore-3.1
Indicates whether a Unicode character is categorized as a Unicode letter.
_________
_________
Enumerable.Select Method (System.Linq)
https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.select?view=netcore-3.1
Projects each element of a sequence into a new form.
_________
_________
Regex.Replace Method (System.Text.RegularExpressions)
https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex.replace?view=netframework-4.8
In a specified input string, replaces strings that match a regular expression pattern with a specified replacement string.
_________

*/
//Your code should go here:

