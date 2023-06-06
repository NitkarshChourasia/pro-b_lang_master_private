/*
####  Both Zero, Negative or Positive  ####

Write a function that returns true if both numbers are:
___
*) Smaller than 0, OR ...
*) Greater than 0, OR ...
*) Exactly 0
___

Otherwise, return false.


[Examples]

___
both(6, 2) ➞ true

both(0, 0) ➞ true

both(-1, 2) ➞ false

both(0, 2) ➞ false
_____



[Notes]

Inputs will always be two numbers.


[conditions] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
&& operator
https://docs.microsoft.com/en-us/cpp/cpp/logical-and-operator-amp-amp?view=msvc-170#:~:text=The%20logical%20AND%20operator%20(%20%26%26,true%20and%20returns%20false%20otherwise.&text=The%20operands%20are%20commonly%20relational,the%20logical%20AND%20expression%20continues.
Returns true if both operands are true and returns false otherwise. The operands are implicitly converted to type bool before evaluation, and the result is of type bool …
_________
_________
How to find the sign bit of an integer?
https://stackoverflow.com/questions/3001653/how-can-i-access-the-sign-bit-of-a-number-in-c
Although this can be solved while comparing with zero. But here I just thought of using the sign bit of the integer to compare if they are equal!
_________

*/
//Your code should go here:

