/*
####  Rational Number Class (Part 1)  ####

C# has several numeric types, including natural, real, and irrational numbers. One numeric type that's missing is a Rational number. A rational number, as the name suggests is a ratio between 2 natural numbers and is usually represented as a fraction in the form 1/2, 5/4, -79/13, etc.
Create a C# struct with a constructor that takes two integer parameters, either or both of which may be positive or negative. Include two read-only properties, Numerator and Denominator, that return the numerator and denominator of the fraction respectively of type int. Also, override the ToString() method to give a string representation of the rational number as described in the preceding paragraph.


[Examples]

___
var r1 = new Rational(1, 2);
r1.Numerator ➞ 1
r1.Denominator ➞ 2
r1.ToString() ➞ "1/2"

var r2 = new Rational(10, 8);
r2.Numerator ➞ 5
r2.Denominator ➞ 4
r2.ToString() ➞ "5/4"

var r3 = new Rational(2, -1);
r3.Numerator ➞ -2
r3.Denominator ➞ 1
r3.ToString() ➞ "-2"

var r4 = new Rational(-16, -64);
r4.Numerator ➞ 1
r4.Denominator ➞ 4
r4.ToString() ➞ "1/4"
_____



[Notes]

___
*) The numerator may be zero, but if the denominator is zero an ArgumentException should be raised by the constructor function.
*) The Numerator and Denominator values should be reduced to their lowest possible integer values to maintain the ratio (examples r2 and r4 above).
*) If the resulting fraction is a whole number, the Denominator should return 1 but the ToString() method should only show the integer value (example r3 above).
*) If one of the values of numerator and denominator is negative, the sign is shown on the Numerator and the Denominator is positive (example r3 above).
*) If both the numerator and denominator are negative, the fraction is positive and both Numerator and Denominator are positive (example r4 above).
*) If the numerator is zero, the denominator should be set to 1, regardless of the value passed to the constructor.
___



[Parts 2 and 3]

Parts 2 and 3 of this series will build on the Rational struct developed here to include arithmetical operations, comparison operators, and conversion to and from other numeric types. They can be found here.


[language_fundamentals] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Structure Types
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/struct
Is a value type that can encapsulate data and related functionality. You use the struct keyword to define a structure type.
_________
_________
Simplifying Fractions
https://www.mathsisfun.com/simplifying-fractions.html
Divide the top and bottom by the highest number that can divide into both numbers exactly.
_________
_________
Greatest Common Factor
https://www.mathsisfun.com/greatest-common-factor.html
The highest number that divides exactly into two or more numbers. It is the "greatest" thing for simplifying fractions!
_________

*/
//Your code should go here:

