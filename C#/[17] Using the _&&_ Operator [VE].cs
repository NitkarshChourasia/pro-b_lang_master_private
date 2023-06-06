/*
####  Using the "&&" Operator  ####

C# has a logical operator &&. The && operator takes two boolean values, and returns true if both values are true.
Consider a && b:
___
*) a is checked if it is true or false.
*) If a is false, false is returned.
*) b is checked if it is true or false.
*) If b is false, false is returned.
*) Otherwise, true is returned (as both a and b are therefore true ).
*) Rembember that the default value for bool is false. (eg. var c = new bool(); c is false.)
___

The && operator will only return true for true && true.
Make a function using the && operator.


[Examples]

___
And(true, false) ➞ false

And(true, true) ➞ true

And(false, true) ➞ false

And(false, false) ➞ false
_____



[Notes]

N/A


[language_fundamentals] [logic] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Boolean Logical Operations
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/boolean-logical-operators
The following operators perform logical operations with bool operands: Unary ! (logical negation) operator. Binary & (logical AND), | (logical OR), and ^ (logical excl …
_________
_________
Lambda Expressions
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions
Use the lambda declaration operator => to separate the lambda's parameter list from its body. To create a lambda expression, you specify input parameters (if any) on th …
_________

*/
//Your code should go here:

