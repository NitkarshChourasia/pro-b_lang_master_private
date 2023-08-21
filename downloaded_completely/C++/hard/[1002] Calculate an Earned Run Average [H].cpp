/*
####  Calculate an Earned Run Average  ####

Create a function that returns an Earned Run Average (ERA). An ERA is calculated by multiplying 9 by the quotient of Earned Runs Allowed er divided by ip Innings Pitched.
In baseball statistics, innings are represented with a fractional part of .1 (1/3) or .2 (2/3) to represent the number of outs in an inning. A whole number or a number with a fractional part of .0 represents a full inning with three outs. Check the Resources tab for a deeper explanation.


[Examples]

___
era(22, 99) ➞ 2.00

era(23, 99.1) ➞ 2.08

era(24, 99.2) ➞ 2.17
_____



[Notes]

___
*) ERA is represented with a scale of 2: 2.08
*) For 1/3 and 2/3, use a scale of 2.
___



[math] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
ERA Calculator
https://captaincalculator.com/sports/baseball/era-calculator/
ERA is the number of runs a pitcher allows for every 9 innings of play (7 innings for some leagues). The lower the number, the fewer runs the pitcher allows.
_________
_________
Innings Pitched
https://en.wikipedia.org/wiki/Innings_pitched
Are the number of innings a pitcher has completed, measured by the number of batters and baserunners that are put out while the pitcher is on the pitching mound in a ga …
_________
_________
Rounding Floating Point Number to Two Decimal Places
https://www.geeksforgeeks.org/rounding-floating-point-number-two-decimal-places-c-c/
How to round off a floatig point value to two places. For example, 5.567 should become 5.57 and 5.534 should become 5.53
_________
_________
Earned Run Average
https://en.wikipedia.org/wiki/Earned_run_average
Is the average of earned runs given up by a pitcher per nine innings pitched (i.e. the traditional length of a game). It is determined by dividing the number of earned …
_________
_________
std::setprecision
http://www.cplusplus.com/reference/iomanip/setprecision/
Sets the decimal precision to be used to format floating-point values on output operations. Behaves as if member precision were called with n as argument on the stream …
_________

*/
//Your code should go here:

