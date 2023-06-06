/*
####  Palindrome Timestamps  ####

Create a function that takes two times of day (hours, minutes, seconds) and returns the number of occurences of palindrome timestamps within that range, inclusive.
A palindrome timestamp should be read the same hours : minutes : seconds as seconds : minutes : hours, keeping in mind the seconds and hours digits will reverse. For example, 02 : 11 : 20 is a palindrome timestamp.


[Examples]

___
PalendromeTimestamps(2, 12, 22, 4, 35, 10) ➞ 14

PalendromeTimestamps(12, 12, 12, 13, 13, 13) ➞ 6

PalendromeTimestamps(6, 33, 15, 9, 55, 10) ➞ 0
_____



[Notes]

___
*) Expect military time.
*) Include the given time parameters if they happen to be palendromes.
*) The parameter timestamps are chronological.
___



[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
TimeSpan Struct
https://docs.microsoft.com/en-us/dotnet/api/system.timespan?view=netcore-3.1#:~:text=The%20value%20of%20a%20TimeSpan,MaxValue.
Represents a time interval.
_________
_________
TimeSpan in C#
https://www.c-sharpcorner.com/blogs/timespan-in-c-sharp
Represents a time interval that is difference between two times measured in number of days, hours, minutes, and seconds. C# TimeSpan is used to compare two C# DateTime …
_________

*/
//Your code should go here:

