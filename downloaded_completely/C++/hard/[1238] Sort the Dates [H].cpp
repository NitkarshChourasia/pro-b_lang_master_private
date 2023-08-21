/*
####  Sort the Dates  ####

In this challenge, sort an array containing a series of dates given as strings. Each date is given in the format DD-MM-YYYY_HH:MM:
___
"12-02-2012_13:44"
_____

The priority of criteria used for sorting will be:
___
*) Year
*) Month
*) Day
*) Hours
*) Minutes
___

Given an array arr and a string type, implement a function that returns:
___
*) if type is equal to "ASC", the array arr sorted in ascending order.
*) if type is equal to "DSC", the array arr sorted in descending order.
___



[Examples]

___
sortDates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC") ➞ [
  "10-02-2016_12:30", "10-02-2018_12:15", "10-02-2018_12:30"
]

sortDates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC") ➞ [
  "10-02-2018_12:30", "10-02-2018_12:15", "10-02-2016_12:30"
]

sortDates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC") ➞ [
  "01-01-1999_00:55", "09-02-2000_10:03", "10-02-2000_18:29"
]
_____



[Notes]

___
*) Remember: the date is in the format DD-MM-YYYY_HH:MM.
*) You can expect only valid formatted dates, without exceptions to handle.
___



[dates] [sorting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

