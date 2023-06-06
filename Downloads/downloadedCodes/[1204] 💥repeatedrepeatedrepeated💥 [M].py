"""
####  💥repeatedrepeatedrepeated💥  ####

This challenge concerns strings such as:
___
"repeatedrepeatedrepeated"
_____

... that are obtained by repeating a smaller string, which in this case is the string "repeated".
On a related note, since the string above is made of 3 repetitions, one way to produce this string is via the code 3 * "repeated".
Write a function that, given a string, either:
___
*) Returns False if the string isn't made by repeating a smaller string or ...
*) Returns the number of repetitions if the string repeats a smaller string.
___



[Examples]

___
is_repeated("repeatedrepeatedrepeated") ➞ 3

is_repeated("overintellectualizations") ➞ False

is_repeated("nononononononononononono") ➞ 12

is_repeated("moremoremoremoremoremore") ➞ 6

is_repeated(",,,,,,,,,,,,,,,,,,,,,,,,") ➞ 24
_____



[Notes]

To keep things a little simpler, all strings in the tests will have length exactly 24, just as in all the examples above. In particular, the answers will always be divisors of 24.


[language_fundamentals] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How can I tell if a string repeats itself in Python?
https://stackoverflow.com/questions/29481088/how-can-i-tell-if-a-string-repeats-itself-in-python/29482936#29482936
Here are some benchmarks for the various answers to this question. There were some surprising results, including wildly different performance depending on the string be …
_________
_________
How to check if a string repeats?
https://www.geeksforgeeks.org/python-check-if-string-repeats-itself/
While working with strings, many times, we can come across a use case in which we need to find if a string has in it the repeating substring, which repeats all over the …
_________

"""
#Your code should go here:

