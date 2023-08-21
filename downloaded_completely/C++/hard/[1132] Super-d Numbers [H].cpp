/*
####  Super-d Numbers  ####

A number n becomes a super-d number when, for any digit d from 2 up to 9, the result of d * nᵈ contains d consecutive digits equal to d.
Given a positive integer n, implement a function that returns:
___
*) "Super-d Number" if n is a super-d number, replacing the letterd with the digit (any from 2 up to 9) that makes it super;
*) "Normal Number" if n is not a super-d number.
___



[Examples]

___
isSuperD(19) ➞ "Super-2 Number"
// when d = 2
// 2 * 19² = 722
// There are two (d) consecutives digits equal to 2 (d)

isSuperD(753) ➞ "Super-3 Number"
// when d = 3
// 3 * 753³ = 1280873331
// There are three (d) consecutives digits equal to 3 (d)

isSuperD(1168) ➞ "Super-4 Number"
// when d = 4
// 4 * 1168⁴ = 7444428488704
// There are four (d) consecutives digits equal to 4 (d)

isSuperD(24) ➞ "Normal Number"
// No cases where d * 24ᵈ (with d being any digit from 2 up to 9)...
// ...leads to a result containing d consecutive digits equal to d
_____



[Notes]

___
*) Any given n will be a positive integer greater or equal to 0.
___



[algorithms] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Returns a string with the representation of val. The format used is the same that printf would print for the corresponding type.
_________

*/
//Your code should go here:

