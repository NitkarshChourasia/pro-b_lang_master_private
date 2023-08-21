/*
####  Working 9 to 5  ####

Write a function that calculates overtime and pay associated with overtime.
___
*) Working 9 to 5: regular hours
*) After 5pm is overtime
___

Your function gets an array with 4 values:
___
*) Start of working day, in decimal format, (24-hour day notation)
*) End of working day. (Same format)
*) Hourly rate
*) Overtime multiplier
___

Your function should spit out:
___
*) $ + earned that day (rounded to the nearest hundreth)
___



[Examples]

___
overTime([9, 17, 30, 1.5]) ➞ "$240.00"

overTime([16, 18, 30, 1.8]) ➞ "$84.00"

overTime([13.25, 15, 30, 1.5]) ➞ "$52.50"
_____

2nd example explained:
___
*) From 16 to 17 is regular, so 1 * 30 = 30
*) From 17 to 18 is overtime, so 1 * 30 * 1.8 = 54
*) 30 + 54 = $84.00
___



[algebra] [arrays] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
std::setprecision
http://www.cplusplus.com/reference/iomanip/setprecision/
Sets the decimal precision to be used to format floating-point values on output operations. Behaves as if member precision were called with n as argument on the stream …
_________

*/
//Your code should go here:

