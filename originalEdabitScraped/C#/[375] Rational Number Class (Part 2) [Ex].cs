/*
####  Rational Number Class (Part 2)  ####

C# has several numeric types including natural, real and irrational numbers. One numeric type that's missing is a Rational number. A rational number, as the name suggests, is a ratio between two natural numbers and is usually represented as a fraction in the form 1/2, 5/4, -79/13, etc.
In part 1 of this challenge, you were asked to create a C# struct with a constructor that takes two integer parameters, either or both of which may be positive or negative. The struct should include two read-only properties, Numerator and Denominator, which return the numerator and denominator of the fraction respectively of type int. These properties should be reduced to there lowest common form. The ToString() method should be overridden to give a string representation of the rational number as described in the preceding paragraph.
Before completing this part, make sure your class meets the conditions described in part 1. The best way to do this is to complete that challenge first and use the code to start this challenge.
Your task now is to add arithmetical operations to your class so that rational numbers can be added, subtracted, multiplied, and divided. To do this you will need to understand how to overload the operators +, -, *, and /. You should also implement the unary '-` operator. If you're not sure how to do this, check out the Resources tab.
Since Math.Sign() does not know about the Rational class, implement a read-only property Sign that returns an int value of -1, 0 or '1' depending on the sign of the fraction.


[Examples]

___
var r1 = new Rational(1, 2); 
var r2 = new Rational(10, 8); 
var r3 = new Rational(2, -1); 

// The following operations are valid:
var r4 = r1 + r2; r4.ToString() ➞ "7/4"
(r1 * r3).ToString() ➞ "-1"
(r2 - new Rational(-1, 4)).ToString() ➞ "3/2" 
var r5 = (r1 + r2) / r3; r5.ToString() ➞ "-7/8"

// Unary operator '-' changes the sign
(-r1).ToString() ➞ "-1/2"
(-r3).ToString() ➞ "2" 
(r1 - -r2).ToString() ➞ "7/4" (1/2 + 5/4)

r3.Sign ➞ -1
_____



[Notes]

___
*) You need to cope with negative, positive, or zero rational numbers.
*) If an attempt is made to divide by a zero rational number (e.g. new Rational(0, 1)), a DivideByZeroException should be raised.
___



[Part 3]

In part 3 of this series, the task will be to complete the Rational numeric struct by implementing comparison operators ==, !=, <, <=, >, and >=. This will enable the Rational number type to be used in comparison statements and expressions. You will also be asked to implement implicit and explicit type conversions between Rational and decimal types.


[language_fundamentals] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Operator Overloading
https://www.geeksforgeeks.org/c-sharp-operator-overloading/
The concept of overloading a function can also be applied to operators. Operator overloading gives the ability to use the same operator to do various operations. It pro …
_________

*/
//Your code should go here:

