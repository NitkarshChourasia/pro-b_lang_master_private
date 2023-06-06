/*
####  Throwing <N> Amount of Darts Find All Possible Combinations to Reach a Target Score  ####

You're given a dartboard divided into sections, each section has a unique score. That means there won't be two sections with the same score.

Throwing a certain amount of valid darts, find how many solutions there are to reach the target score. Your function will be passed three parameters...
___
*) Sections: A list of values for the sections (e.g. { 3, 6, 8, 11, 15, 19, 22 }, the list is already sorted).
*) Darts: The amount of darts to throw.
*) Target: The target score.
___

Return an empty list if no solution is found, otherwise a list of non-duplicate strings for each solution (e.g. { "3-11-18", "7-7-18", "7-11-14" }).


[Examples]

If there are duplicate values, keep only the one sorted from smallest to biggest.
___
"8-19-8"

"8-8-19" <-- This is the one you would keep.

"19-8-8"
_____

Multiple solutions should be sorted before returning them.
___
{ "3-11-18", "7-7-18", "7-11-14" } is ok.

{ "7-11-14", "7-7-18", "3-11-18" } is not ok.
_____



[Notes]

___
*) Multiple darts can land in the same section.
*) A dart must land in a valid section (it can't miss).
___



[arrays] [loops] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Language Integrated Query
https://www.tutorialsteacher.com/linq/linq-tutorials
Language-Integrated Query (LINQ) is a powerful query language introduced with .Net 3.5 & Visual Studio 2008. LINQ can be used with C# or Visual Basic to query different …
_________
_________
LINQ Extension Methods
https://dotnettutorials.net/lesson/linq-extension-methods/
The LINQ’s standard query operators such as select, where, etc. are implemented in Enumerable class. These methods are implemented as extension methods of the type IEnu …
_________
_________
C# Generic Methods
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/generic-methods
Is a method that is declared with type parameters.
_________
_________
C# Iterator Methods
https://docs.microsoft.com/en-us/dotnet/csharp/iterators
Another great feature of the C# language enables you to build methods that create a source for an enumeration. These are referred to as iterator methods. An iterator me …
_________

*/
//Your code should go here:

