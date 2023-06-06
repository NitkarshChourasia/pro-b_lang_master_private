/*
####  Power Ranger  ####

Create a function that takes in n, a, b and returns the number of positive values raised to the nth power that lie in the range [a, b], inclusive.


[Examples]

___
PowerRanger(2, 49, 65) ➞ 2
// 2 squares (n^2) lie between 48 and 65, 49 (7^2) and 64 (8^2)

PowerRanger(3, 1, 27) ➞ 3
// 3 cubes (n^3) lie between 1 and 27, 1 (1^3), 8 (2^3) and 27 (3^3)

PowerRanger(10, 1, 5) ➞ 1
// 1 value raised to the 10th power lies between 1 and 5, 1 (1^10)

PowerRanger(5, 31, 33) ➞ 1

PowerRanger(4, 250, 1300) ➞ 3
_____



[Notes]

___
*) Remember that the range is inclusive.
*) a < b will always be true.
___



[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Math.Pow(Double, Double) Method
https://docs.microsoft.com/en-us/dotnet/api/system.math.pow?view=netframework-4.8
Syntax for Math.Pow Method for power to calculations in C#.
_________
_________
Find Nth Root
https://stackoverflow.com/questions/18657508/c-sharp-find-nth-root/18657674
I use below method to calculate Nth Root of double value, but it takes a lot of time for calculating the 240th root. I found out about Newton method, but was not able t …
_________
_________
Math.Floor() Method
https://www.geeksforgeeks.org/c-sharp-math-floor-method/
Is a Math class method. This method is used to find the largest integer, which is less than or equal to the passed argument. The floor method operates both functionalit …
_________

*/
//Your code should go here:

