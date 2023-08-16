"""
####  Seven Segment Display  ####


The table below shows which of the segments a through g are illuminated on the seven segment display for the digits 0 through 9. When the number on the display changes, some of the segments may stay on, some may stay off, and others change state (on to off, or off to on).
Create a function that accepts a string of digits, and for each transition of one digit to the next, returns a list of the segments that change state. Designate the segments that turn on as uppercase and those that turn off as lowercase. Sort the lists in alphabetical order.
For example:
___
seven_segment("805") ➞ [["g"], ["b", "e", "G"]]
_____

In the transition from 8 to 0, the g segment turns off. Others are unchanged. In the transition from 0 to 5, b and e turn off and G turns on. Others are unchanged.



[Examples]

___
seven_segment("02") ➞ [["c", "f", "G"]]

seven_segment("08555") ➞ [["G"], ["b", "e"], [], []]
# Empty lists designate no change.

seven_segment("321") ➞ [["c", "E"], ["a", "C", "d", "e", "g"]]

seven_segment("123") ➞ [["A", "c", "D", "E", "G"], ["C", "e"]]

seven_segment("3") ➞ []

seven_segment("33") ➞ [[]]
_____



[Notes]

N/A


[logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
upper() Method
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/#:~:text=In%20Python%2C%20upper()%20is,it%20returns%20the%20original%20string.
Is a built-in method used for string handling. The upper() methods returns the uppercased string from the given string. It converts all lowercase characters to uppercas …
_________

"""
#Your code should go here:

