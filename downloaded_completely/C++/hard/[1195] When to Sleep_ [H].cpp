/*
####  When to Sleep?  ####

Given a series of arrays, with each individual array containing the time of the alarm set and the sleep duration, return what time to sleep.


[Examples]

___
bedTime(["07:50", "07:50"]) ➞ ["00:00"]
// The second argument means 7 hours, 50 minutes sleep duration.

bedTime(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"]) ➞ ["20:15", "22:00", "23:30"]
// The second argument of each sub list means 10 hours sleep duration.

bedTime(["05:45", "04:00"], ["07:10", "04:30"]) ➞ ["01:45", "02:40"]
// Sleep duration can be different among the arrays.
_____



[Notes]

___
*) Times should be given in 24-hrs (i.e. "23:25" as opposed to "11:25PM").
*) Return an array of strings.
___



[arrays] [logic] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

