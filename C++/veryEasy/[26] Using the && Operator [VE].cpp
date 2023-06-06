/*
####  Using the && Operator  ####

C++ has a logical operator &&, which can also be written as "and" (for users without & on their keyboard). The && operator is very useful, it takes in two values. For example, a&&b works like:
___
*) a is checked if it is true or false.
*) Same with b if a is true. If a is false, return false
*) Return true if a and b are true and false otherwise.
___

The && operator is equivalent to this function (it doesn't use any shortcuts so it is easier to understand for beginners):
___
bool AND(bool a, bool b){
  if (a == false) {
    return false; // stops function and returns false
  }
  else if (b == true){ // "a" must be true because it would return otherwise
    return true;
  } else {
    return false;
  }
}
_____

So, && will only return true for true&&true.
Make a function using &&.


[Examples]

___
andAnd(true, false) ➞ false

andAnd(true, true) ➞ true

andAnd(false, true) ➞ false

andAnd(false, false) ➞ false
_____



[Notes]

N/A


[language_fundamentals] [logic] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Logical Operators
https://en.cppreference.com/w/cpp/language/operator_logical
Returns the result of a boolean operation.
_________
_________
Logical AND Operator: &&
https://docs.microsoft.com/en-us/cpp/cpp/logical-and-operator-amp-amp?view=vs-2019
Returns the boolean value TRUE if both operands are TRUE and returns FALSE otherwise. The operands are implicitly converted to type bool prior to evaluation, and the re …
_________
_________
Bitwise AND Operator: &
https://docs.microsoft.com/en-us/cpp/cpp/bitwise-and-operator-amp?view=vs-2019
Compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corr …
_________

*/
//Your code should go here:

