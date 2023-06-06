"""
####  Sort the Dates  ####

In this challenge, sort a list containing a series of dates given as strings. Each date is given in the format DD-MM-YYYY_HH:MM:
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

Given a list lst and a string mode, implement a function that returns:
___
*) if mode is equal to "ASC", the list lst sorted in ascending order.
*) if mode is equal to "DSC", the list lst sorted in descending order.
___



[Examples]

___
sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC") ➞ ["10-02-2016_12:30", "10-02-2018_12:15", "10-02-2018_12:30"]

sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC") ➞ ["10-02-2018_12:30", "10-02-2018_12:15", "10-02-2016_12:30"]

sort_dates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC") ➞ ["01-01-1999_00:55", "09-02-2000_10:03", "10-02-2000_18:29"]
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
How to sort list of date strings?
https://stackoverflow.com/questions/17627531/sort-list-of-date-strings
I have an arbitrary list of date strings (mm-yyyy). I need this list to be sorted first by the level of years (ascending), then on the level of months (ascending)..so t …
_________
_________
datetime — Basic date and time types
https://docs.python.org/2/library/datetime.html
The datetime module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the im …
_________
_________
Python string to datetime - strptime()
https://www.journaldev.com/23365/python-string-to-datetime-strptime
We can convert a string to datetime using strptime() function. This function is available in datetime and time modules to parse a string to datetime and time objects re …
_________
_________
strptime() Method
https://www.programiz.com/python-programming/datetime/strptime
In this article, you will learn to create a datetime object from a string (with the help of examples). For that, we use Python's strptime() method. Any string represent …
_________

"""
#Your code should go here:

