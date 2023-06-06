/*
####  The Day Rob Was Born in Dutch  ####

I was born on the 21st of September in the year of 1970. That was a Monday. Where I was born that weekday is called måndag.
___
*) Write a method that when passed a date as year/month/ day and returns the date's weekday name in the Dutch culture. The culture identifier to use is "nl-NL". Not "nl-BE".
*) You can assume the specified date is valid.
*) Looking at the tests and doing a switch statement or similar is considered cheating.
*) System.Globalization.CultureInfo should be used.
*) The method may be used to get the name of the Dutch weekday of other memorable days too, like in the examples below:
___



[Examples]

___
WeekdayRobWasBornInDutch(1970, 9, 21)) ➞ "maandag"

WeekdayRobWasBornInDutch(1945, 9, 2)) ➞ "zondag"

WeekdayRobWasBornInDutch(2001, 9, 11)) ➞ "dinsdag"
_____



[Notes]

Check the Resources tab for help.


[arrays] [dates] 



-------------------------------------------------------------------
[Resources]
_________
DateTime.DayOfWeek Property
https://docs.microsoft.com/en-us/dotnet/api/system.datetime.dayofweek?view=netframework-4.8
Gets the day of the week represented by this instance.
_________
_________
Language Culture Names, Codes, and ISO Values
http://docwiki.embarcadero.com/RADStudio/Rio/en/Language_Culture_Names,_Codes,_and_ISO_Values
RAD Studio includes a suite of Translation Tools to facilitate localization and development of Win32 applications for different locales. When you add a new language to …
_________
_________
DateTimeFormatInfo.DayNames Property
https://docs.microsoft.com/en-us/dotnet/api/system.globalization.datetimeformatinfo.daynames?view=netframework-4.8
Gets or sets a one-dimensional string array that contains the culture-specific full names of the days of the week.
_________
_________
Gobalization example with DateTime.DayOfWeek
https://stackoverflow.com/questions/5716762/datetime-now-dayofweek-tostring-with-cultureinfo
Example of how to make a culture and get the information from DateTime.
_________
_________
CultureInfo.GetCultureInfo Method
https://docs.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo.getcultureinfo?view=netframework-4.8
Retrieves a cached, read-only instance of a culture.
_________

*/
//Your code should go here:

