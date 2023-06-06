/*
####  Track the Robot (Part 1)  ####

A robot has been given a list of movement instructions. Each instruction is either left, right, up or down, followed by a distance to move. The robot starts at [0, 0]. You want to calculate where the robot will end up and return its final position as an array.
To illustrate, if the robot is given the following instructions:
___
new string[] { "right 10", "up 50", "left 30", "down 10" }
_____

It will end up 20 left and 40 up from where it started, so we return int[] { -20, 40 }.


[Examples]

___
TrackRobot(new string[] { "right 10", "up 50", "left 30", "down 10" }) ➞ int[] { -20, 40 }

TrackRobot(new string[] { }) ➞ int[] { 0, 0 }
// If there are no instructions, the robot doesn't move.

TrackRobot(new string[] { "right 100", "right 100", "up 500", "up 10000" }) ➞ new int[] { 200, 10500 }
_____



[Notes]

___
*) The only instructions given will be left, right, up or down.
*) The distance after the instruction is always a positive whole number.
___



[arrays] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
string.split Method
https://docs.microsoft.com/en-us/dotnet/api/system.string.split?view=net-6.0#system-string-split(system-char())
Returns a string array that contains the substrings in this instance that are delimited by elements of a specified string or Unicode character array.
_________
_________
Finding Length of a Given Array
https://www.geeksforgeeks.org/how-to-find-the-length-of-an-array-in-c-sharp/
Array.Length Property is used to get the total number of elements in all the dimensions of the Array. Basically, the length of an array is the total number of the eleme …
_________
_________
Declaring Array of a Specific Size
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/#:~:text=You%20declare%20an%20array%20by,directly%20or%20indirectly%20from%20Object.
You declare an array by specifying the type of its elements. If you want the array to store elements of any type, you can specify object as its type. In the unified typ …
_________
_________
Converting a String to Int32
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/types/how-to-convert-a-string-to-a-number
You convert a string to a number by calling the Parse or TryParse method found on numeric types (int, long, double, and so on), or by using methods in the System.Conver …
_________

*/
//Your code should go here:

