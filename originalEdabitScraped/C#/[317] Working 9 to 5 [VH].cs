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
OverTime([9, 17, 30, 1.5]) ➞ "$240.00"

OverTime([16, 18, 30, 1.8]) ➞ "$84.00"

OverTime([13.25, 15, 30, 1.5]) ➞ "$52.50"
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
String.Format Method (System)
https://docs.microsoft.com/en-us/dotnet/api/system.string.format?view=net-5.0
Converts the value of objects to strings based on the formats specified and inserts them into another string. If you are new to the String.Format method, see the Get st …
_________

*/
//Your code should go here:

