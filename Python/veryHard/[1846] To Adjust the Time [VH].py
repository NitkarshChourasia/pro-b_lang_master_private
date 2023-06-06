"""
####  To Adjust the Time  ####

In this challenge, you have to add a variable amount of hours, minutes and seconds to a given time, obtaining, in turn, a new adjusted time.
Given a string now being a timestamp in the format hh:mm:ss, and three integers hrs, mins and sec being the hours, minutes and seconds to add, implement a function that returns a string being the newly adjusted timestamp (maintaining the same format).


[Examples]

___
time_adjust("01:00:00", 1, 30, 10) ➞ "02:30:10"

time_adjust("18:22:30", 4, 60, 30) ➞ "23:23:00"

time_adjust("00:00:00", 72, 120, 120) ➞ "02:02:00"
_____



[Notes]

___
*) The amounts of hrs, mins and sec can be any positive integer, and you have to correctly add them to the corresponding unit if they exceed their scale. See example #2: sixty minutes is one hour, and sixty seconds (30 + 30) is one minute.
*) If the amount of time to add exceeds the 24 hours, then the time will start again from "00:00:00". See example #3: 72 hours are 3 exact days so that after three cycles of 24 hours, the hour will be again "00" (and becomes "02" because we are adding also 120 minutes or 2 hours).
___



[dates] [formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
What is Python timedelta?
https://www.jquery-az.com/python-timedelta/
Is the class in datetime module that represents duration. The delta means average of difference and so the duration expresses the difference between two date, datetime …
_________
_________
Program to Find Difference Between Current Time and Given Time
https://www.geeksforgeeks.org/python-program-to-find-difference-between-current-time-and-given-time/
Given two times h1:m1 and h2:m2 denoting hours and minutes in 24 hours clock format. The current clock time is given by h1:m1. The task is to calculate the difference b …
_________

"""
#Your code should go here:

