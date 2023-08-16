"""
####  Get the Months Between Two Dates  ####

Create a function that, given 2 dates, returns the names of the months that are present between them (inclusive).


[Examples]

Input
___
 january = datetime.date(2017, 1, 1)
 march = datetime.date(2017, 3, 1)

monthsInterval(january, march)
_____

Output
___
['January', 'February', 'March']
_____

Input
___
 december = datetime.date(2017, 12, 1)
 january = datetime.date(2018, 1, 1)

monthsInterval(december, january)
_____

Output
___
['January', 'December']
_____

Input
___
 january2017 = datetime.date(2017, 0, 1)
 january2018 = datetime.date(2018, 0, 1)

monthsInterval(january2017, january2018)
_____

Output
___
['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
_____

(Notice that January is not duplicated!)


[Notes]

___
*) The returned list should include the months of dateStart and dateEnd (inclusive)
*) The returned list must not include duplicate values
*) The month names returned by the function should be sorted (not alphabetically, but ordered by which comes first (January = 1st month, February = 2nd month, … , December = 12th month))
*) The function should produce the same output even if dateStart is greater than dateEnd
___



[arrays] [dates] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
datetime — Basic Date and Time Types
https://docs.python.org/3/library/datetime.html
The datetime module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the im …
_________
_________
calendar — General Calendar Related Functions
https://docs.python.org/3/library/calendar.html
This module allows you to output calendars like the Unix cal program, and provides additional useful functions related to the calendar. By default, these calendars have …
_________

"""
#Your code should go here:

