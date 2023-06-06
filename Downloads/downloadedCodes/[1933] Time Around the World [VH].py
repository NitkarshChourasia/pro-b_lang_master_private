"""
####  Time Around the World  ####

In this challenge, the goal is to calculate what time it is in two different cities. You're given a string city_a and the related string timestamp (time in city_a) with the date formatted in full U.S. notation, as in this example:
___
"July 21, 1983 23:01"
_____

You have to return a new timestamp with date and corresponding time in city_b, formatted as in this example:
___
"1983-7-22 23:01"
_____

See the table below for a list of given cities and their GMT (Greenwich Mean Time) hours offsets.



[Examples]

___
time_difference("Los Angeles", "April 1, 2011 23:23", "Canberra") ➞ "2011-4-2 17:23"
# Can be a new day.

time_difference("London", "July 31, 1983 23:01", "Rome") ➞ "1983-8-1 00:01"
# Can be a new month.

time_difference("New York", "December 31, 1970 13:40", "Beijing") ➞ "1971-1-1 02:40"
# Can be a new year.
_____



[Notes]

___
*) Pay attention to hours and minutes, a leading 0 is needed in the returned timestamp when they're a single digit.
*) Pay attention to cities with half hours offsets.
___



[dates] [formatting] 



-------------------------------------------------------------------
[Resources]
_________
How to add hours to current time in Python?
https://stackoverflow.com/questions/13685201/how-to-add-hours-to-current-time-in-python/13685221
I am able to get the current time as below: from datetime import datetime str(datetime.now())[11:19] Result '19:43:20' Now, i am trying to add 9 hours to the above time …
_________
_________
strftime() Method
https://www.programiz.com/python-programming/datetime/strftime
In this article, you will learn to convert datetime object to its equivalent string in Python with the help of examples. For that, we can use strftime() method. Any obj …
_________

"""
#Your code should go here:

