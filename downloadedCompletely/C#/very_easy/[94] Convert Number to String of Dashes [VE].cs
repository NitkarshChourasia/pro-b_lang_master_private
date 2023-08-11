/*
####  Convert Number to String of Dashes  ####

Create a function that takes a number (from 1 - 60) and returns a corresponding string of hyphens.


[Examples]

___
Go(1) ➞ "-"

Go(5) ➞ "-----"

Go(3) ➞ "---"
_____



[Notes]

___
*) You will be provided integers ranging from 1 to 60.
*) Don't forget to return your result as a string.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[loops] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
StringBuilder.Append(Char, Int32)
https://docs.microsoft.com/en-us/dotnet/api/system.text.stringbuilder.append?view=netframework-4.7.2#System_Text_StringBuilder_Append_System_Char_System_Int32_
Appends a specified number of copies of the string representation of a Unicode character to this instance.
_________
_________
String(Char, Int32)
https://docs.microsoft.com/en-us/dotnet/api/system.string.-ctor?view=netframework-4.7.2#System_String__ctor_System_Char_System_Int32_
Initializes a new instance of the String class to the value indicated by a specified Unicode character repeated a specified number of times.
_________
_________
String.Join Method (System)
https://docs.microsoft.com/en-us/dotnet/api/system.string.join?view=netframework-4.7.2
Concatenates the elements of a specified array or the members of a collection, using the specified separator between each element or member.
_________
_________
StringBuilder Class (System.Text)
https://docs.microsoft.com/en-us/dotnet/api/system.text.stringbuilder?view=netframework-4.7.2
Represents a mutable string of characters. This class cannot be inherited.
_________
_________
StringBuilder() Method!
https://www.tutorialsteacher.com/csharp/csharp-stringbuilder
If you're building a string, it's better to use this than just type String.
_________
_________
String.PadRight Method (System)
https://docs.microsoft.com/en-us/dotnet/api/system.string.padright?view=netframework-4.8
Returns a new string of a specified length in which the end of the current string is padded with spaces or with a specified Unicode character.
_________
_________
Immutability and the StringBuilder Class
https://docs.microsoft.com/en-us/dotnet/api/system.string?view=netframework-4.7.2#immutability-and-the-stringbuilder-class
A String object is called immutable (read-only), because its value cannot be modified after it has been created. Methods that appear to modify a String object actually …
_________
_________
Enumerable.Repeat<TResult>(TResult, Int32) Method
https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.repeat?view=netframework-4.8
Generates a sequence that contains one repeated value.
_________
_________
String vs StringBuilder
https://www.geeksforgeeks.org/c-sharp-string-vs-stringbuilder/
StringBuilder is used to represent a mutable string of characters. Mutable means the string which can be changed. So String objects are immutable but StringBuilder is t …
_________
_________
Expression Body Definitions
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/methods#expression-body-definitions
It is common to have method definitions that simply return immediately with the result of an expression, or that have a single statement as the body of the method. Ther …
_________

*/
//Your code should go here:

