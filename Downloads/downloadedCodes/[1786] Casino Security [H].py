"""
####  Casino Security  ####

You're head of security at a casino that has money being stolen from it. You get the data in the form of strings and you have to set off an alarm if a thief is detected.
___
*) If there is no guard between thief and money, return "ALARM!"
*) If the money is protected, return "Safe"
___



[String Components]

___
*) x - Empty Space
*) T - Thief
*) G - Guard
*) $ - Money
___



[Examples]

___
security("xxxxTTxGxx$xxTxxx") ➞ "ALARM!"

security("xxTxxG$xxxx$xxxx") ➞ "Safe"

security("TTxxxx$xxGxx$Gxxx") ➞ "ALARM!"
_____



[Notes]

Money at the extremes are safe.


[games] [logic] [regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Find string between two substrings [duplicate]
https://stackoverflow.com/questions/3368969/find-string-between-two-substrings
Find a string between two substrings
_________

"""
#Your code should go here:

