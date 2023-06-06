/*
####  Strip URL Query Parameters  ####

Create a function that takes a URL (string), removes duplicate query parameters and parameters specified within the 2nd argument (which will be an optional array).


[Examples]

___
stripUrlParams("https://edabit.com?a=1&b=2&a=2") ➞ "https://edabit.com?a=2&b=2"

stripUrlParams("https://edabit.com?a=1&b=2&a=2", ["b"]) ➞ "https://edabit.com?a=2"

stripUrlParams("https://edabit.com", ["b"]) ➞ "https://edabit.com"
_____



[Notes]

___
*) The 2nd argument paramsToStrip is optional.
*) paramsToStrip can contain multiple params.
*) If there are duplicate query parameters with different values, use the value of the last occurring parameter (see examples #1 and #2 above).
___



[algorithms] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Regular Expressions
https://www.w3schools.com/java/java_regex.asp
Is a sequence of characters that forms a search pattern. When you search for data in a text, you can use this search pattern to describe what you are searching for.
_________
_________
Query String
https://en.wikipedia.org/wiki/Query_string
Is a part of a uniform resource locator (URL) that assigns values to specified parameters. A query string commonly includes fields added to a base URL by a Web browser …
_________

*/
//Your code should go here:

