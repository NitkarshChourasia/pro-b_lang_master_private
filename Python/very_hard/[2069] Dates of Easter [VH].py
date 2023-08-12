"""
####  Dates of Easter  ####

The Christian holiday of Easter Sunday is a movable feast. It can occur on any date from March 22 to April 25. The date depends on the timing between the Paschal Full Moon and the spring equinox. It wasn't until the late 19th century that a formula was developed to accurately predict Easter's date for a given year.
Your task is to use this formula, also known as Butcher's Algorithm, to write a function that will return the date of Easter for any year after 1600. See the Resources tab for a detailed description of the algorithm.


[Examples]

___
easter_date(1600) ➞ "April 2"

easter_date(2020) ➞ "April 12"

easter_date(1853) ➞ "March 27"

easter_date(3535) ➞ "April 14"
_____



[Notes]

Before 1600 the Julian calendar was used in most countries. The algorithm we're using is based on the Gregorian calendar, which is still in use today.


[algorithms] [math] 



-------------------------------------------------------------------
[Resources]
_________
Calculating the Date of Easter
http://www.oremus.org/liturgy/etc/ktf/app/easter.html
We refer to the year number as y, and use it to calculate the Golden number, g: g = y mod 19 + 1 Next we calculate the date of the Paschal full moon, that is, the fu …
_________
_________
Calculate Easter (Western) Given a Year
http://code.activestate.com/recipes/576517-calculate-easter-western-given-a-year/
An implementation of Butcher's Algorithm for determining the date of Easter for the Western church. Works for any date in the Gregorian calendar (1583 and onward). Retu …
_________
_________
Computus
https://en.wikipedia.org/wiki/Computus#Algorithms
The computus (Latin for "computation") is a calculation that determines the calendar date of Easter. Because the date is based on an ecclesiastical or paschal "equinox" …
_________
_________
Meeus/Jones/Butcher Algorithm
https://en.wikipedia.org/wiki/Computus#Anonymous_Gregorian_algorithm
The computus (Latin for 'computation') is a calculation that determines the calendar date of Easter. Because the date is based on an ecclesiastical or paschal "equinox" …
_________

"""
#Your code should go here:

