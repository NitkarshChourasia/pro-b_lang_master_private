/*
####  Valid JavaScript Comments  ####

In JavaScript, there are two types of comments:

The input will be a sequence of //, /* and */. Every /* must have a */ that immediately follows it. To add, there can be no single-line comments in between multi-line comments in between the /* and */.
Create a function that returns true if comments are properly formatted, and false otherwise.


[Examples]

___
CommentsCorrect("//////") ➞ true
// 3 single-line comments: ["//", "//", "//"]

CommentsCorrect("/**//**////**/") ➞ true
// 3 multi-line comments + 1 single-line comment:
// ["/*", "*/", "/*", "*/", "//", "/*", "*/"]

CommentsCorrect("///*/**/") ➞ false
// The first /* is missing a */

CommentsCorrect("/////") ➞ false
// The 5th / is single, not a double //
_____



[Notes]

N/A


[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Regex.IsMatch Method (System.Text.RegularExpressions)
https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex.ismatch?view=netcore-3.1
Indicates whether the regular expression finds a match in the input string.
_________

*/
//Your code should go here:

