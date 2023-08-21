/*
####  Calculate Elapsed Time  ####

Create a function that takes a timestamp for the start time sa and stop time st in HH:MM:SS format and returns the measured amount of elapsed time between start and stop times.


[Examples]

___
elapsedTime("11:00:00", "12:00:00") ➞ "01:00:00"

elapsedTime("13:01:43", "21:41:57") ➞ "08:40:14"

elapsedTime("17:34:43", "17:34:42") ➞ "23:59:59"
_____



[Notes]

___
*) All times will be provided in 24 Hrs format.
*) Consider Elapsed time will always be less than 24 Hrs.
___



[numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::stoi, std::stol, std::stoll
https://en.cppreference.com/w/cpp/string/basic_string/stol
Interprets a signed integer value in the string str. Discards any whitespace characters (as identified by calling isspace()) until the first non-whitespace character is …
_________
_________
std::basic_string<CharT,Traits,Allocator>::substr
https://en.cppreference.com/w/cpp/string/basic_string/substr
Returns a substring [pos, pos+count). If the requested substring extends past the end of the string, or if count == npos, the returned substring is [pos, size()).
_________
_________
Stopwatch
https://en.wikipedia.org/wiki/Stopwatch
Is a handheld timepiece designed to measure the amount of time that elapses between its activation and deactivation.
_________

*/
//Your code should go here:

