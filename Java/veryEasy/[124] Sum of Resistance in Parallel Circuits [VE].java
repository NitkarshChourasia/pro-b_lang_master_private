/*
####  Sum of Resistance in Parallel Circuits  ####

If two or more resistors are connected in parallel, the overall resistance of the circuit reduces. It is possible to calculate the total resistance of a parallel circuit by using this formula:

Create a function that takes an array of parallel resistance values, and calculates the total resistance of the circuit.


[Worked Example]

___
parallelResistance([6, 3, 6]) ➞ 1.5

// 1/RTotal = 1/6 + 1/3 + 1/6
// 1/RTotal = 2/3
// RTotal = 3/2 = 1.5
_____



[Examples]

___
parallelResistance([6, 3]) ➞ 2

parallelResistance([10, 20, 10]) ➞ 4

parallelResistance([500, 500, 500]) ➞ 166.6
// Round to the nearest decimal place
_____



[Notes]

___
*) Return the RTotal, not the reciprocal.
*) Round to the nearest decimal place.
*) All inputs will be valid.
___



[arrays] [loops] [math] [physics] 



-------------------------------------------------------------------
[Resources]
_________
Explanation of the Parallel Circuit
https://www.electronics-tutorials.ws/resistor/res_4.html
Unlike the previous series resistor circuit, in a parallel resistor network the circuit current can take more than one path as there are multiple paths for the current. …
_________

*/
//Your code should go here:

