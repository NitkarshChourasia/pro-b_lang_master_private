"""
####  Current Streak  ####

Create a function that takes the current day (e.g. "2019-09-30"), a list of date dictionaries and returns the "current streak" (i.e. number of consecutive days in a row).


[Examples]

___
current_streak("2019-09-23", [
  {
    "date": "2019-09-18"
  },
  {
    "date": "2019-09-19"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]) ➞ 3

current_streak("2019-09-25", [
  {
    "date": "2019-09-16"
  },
  {
    "date": "2019-09-17"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]) ➞ 0
_____

___
*) The list of dates is sorted chronologically.
*) The today parameter will always be greater than or equal to the last date in the list.
*) An empty list should return 0.
___



[dates] [games] [loops] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Date Formatting
https://mkaz.blog/code/python-dates/
A set of examples working with Python date and time functions, including formatting dates, date calculations, and other common date tasks. See my string format example …
_________
_________
Python Datetime
https://www.w3schools.com/python/python_datetime.asp
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
_________

"""
#Your code should go here:

