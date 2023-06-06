/*
####  Wurst Is Better  ####

Wurst is the best. Create a function that takes a string and replaces every mention of any type of sausage with the German word "Wurst," unless—of course—the sausage is already a type of German "Wurst" (i.e. "Bratwurst", see below), then leave the sausage name unchanged.



[Rules]

___
*) Replace sausages from the "Convert to Wurst" column with "Wurst".
*) Do not replace any German sausage with the word "Wurst".
*) The word "Wurst" must be title case.
___



[Examples]

___
WurstIsBetter("I like chorizos, but not sausages") ➞ "I like Wursts, but not Wursts"

WurstIsBetter("sich die Wurst vom Brot nehmen lassen") ➞ "sich die Wurst vom Brot nehmen lassen"

WurstIsBetter("Bratwurst and Rostbratwurst are sausages") ➞ "Bratwurst and Rostbratwurst are Wursts"
_____



[Notes]

All German sausage names contain the word "wurst".


[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Replace Sections of a String Using Regular Expressions
https://msdn.microsoft.com/en-us/library/taz3ak2f(v=vs.110).aspx
Using the static method Regex.Replace(string, string, string, RegexOptions) we can find and replace patterns in a string while ignoring the case of the input string. Do …
_________
_________
string.replace() Method
https://docs.microsoft.com/en-us/dotnet/api/system.string.replace?view=net-6.0#system-string-replace(system-string-system-string)
Returns a new string in which all occurrences of a specified Unicode character or String in the current string are replaced with another specified Unicode character or …
_________
_________
regex.replace() Method
https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex.replace?view=net-6.0
In a specified input string, replaces strings that match a regular expression pattern with a specified replacement string.
_________
_________
RegexOptions Enumeration
https://msdn.microsoft.com/en-us/library/system.text.regularexpressions.regexoptions(v=vs.110).aspx
We can specify a variety of options for pattern matching. RegexOptions.IgnoreCase is particularly useful.
_________

*/
//Your code should go here:

