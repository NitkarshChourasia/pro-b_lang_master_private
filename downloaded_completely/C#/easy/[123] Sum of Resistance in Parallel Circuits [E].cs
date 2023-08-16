/*
####  Sum of Resistance in Parallel Circuits  ####

If two or more resistors are connected in parallel, the overall resistance of the circuit reduces. It is possible to calculate the total resistance of a parallel circuit by using this formula:

Create a function that takes an array of parallel resistance values, and calculates the total resistance of the circuit.


[Worked Example]

___
ParallelResistance({6, 3, 6}) ➞ 1.5

// 1/RTotal = 1/6 + 1/3 + 1/6
// 1/RTotal = 2/3
// RTotal = 3/2 = 1.5
_____



[Examples]

___
ParallelResistance({6, 3}) ➞ 2

ParallelResistance({10, 20, 10}) ➞ 4

ParallelResistance({500, 500, 500}) ➞ 166.6
// Round to the nearest decimal place
_____



[Notes]

___
*) Note that you should rearrange to return the Resistance Total, not 1 / Resistance Total.
*) Round to the nearest decimal place.
*) All inputs will be valid.
___



[arrays] [loops] [math] [physics] 



-------------------------------------------------------------------
[Resources]
_________
Math.Round Method (System)
https://docs.microsoft.com/en-us/dotnet/api/system.math.round?view=net-5.0#Round2_Example
Rounds a value to the nearest integer or to the specified number of fractional digits.
_________
_________
Linq Select Method
https://www.tutorialspoint.com/chash-linq-select-method
Use the Select method to modify the elements in an array.The following is our string array.string[] stationery = { diary, board, pencil, whiteboard };Th ...
_________
_________
Sum Method: Add Up All Numbers
https://www.dotnetperls.com/sum
Use the Sum extension method and the selector overload. Include the System.Linq namespace.
_________

*/
//Your code should go here:

