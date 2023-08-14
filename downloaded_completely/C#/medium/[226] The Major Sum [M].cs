/*
####  The Major Sum  ####

Create a function that takes an integer array and return the biggest between positive sum, negative sum, or 0s count. The major is understood as the greatest absolute.
arr = {1,2,3,4,0,0,-3,-2}, the function has to return 10, because:
___
*) Positive sum = 1+2+3+4 = 10
*) Negative sum = (-3)+(-2) = -5
*) 0s count = 2 (there are two zeros in array)
___



[Examples]

___
MajorSum(1, 2, 3, 4, 0, 0, -3, -2) ➞ 10

MajorSum(-4, -8, -12, -3, 4, 7, 1, 3, 0, 0, 0, 0) ➞ -27

MajorSum(0, 0, 0, 0, 0, 1, 2, -3) ➞ 5
// Because -3 < 1+2 < 0sCount = 5
_____



[Notes]

___
*) All numbers are integers.
*) There aren't empty arrays.
*) All tests are made to return only one value.
___



[arrays] [conditions] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Introduction to LINQ Queries (C#)
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/introduction-to-linq-queries
Is an expression that retrieves data from a data source. Queries are usually expressed in a specialized query language. Different languages have been developed over tim …
_________
_________
Math.Abs Method
https://docs.microsoft.com/en-us/dotnet/api/system.math.abs?view=netcore-3.1
Returns the absolute value of a specified number.
_________
_________
C# operators - C# reference | Microsoft Docs
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/
C# provides a number of operators supported by the built-in types. For example, arithmetic operators perform arithmetic operations with numeric operands and Boolean log …
_________

*/
//Your code should go here:

