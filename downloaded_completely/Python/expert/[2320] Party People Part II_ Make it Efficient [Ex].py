"""
####  Party People Part II: Make it Efficient  ####

Ava, Mark, Sheila, and Pete are at a party. However, Ava and Sheila are only staying if there are at least 4 people, Pete is only staying if there's 1 person, and Mark is only staying if there are at least 5 people. Therefore, Mark leaves, which makes Ava and Sheila leave, and Pete is left alone.
Given a list with the preferences of every person at a party for the minimum number of people present, determine how many people will stay.
This challenge can be solved recursively, but recursion in Python can become quite resource-intensive. This challenge will include long lists, so you need to make your function efficient.


[Examples]

___
party_people([4, 5, 4, 1]) ➞ 1
# Ava's minimum number is 4, Mark's is 5, Sheila's is 4, and Pete's is 1. 
# Only 1 person (Pete) stays.

party_people([10, 12, 15, 15, 5]) ➞ 0

party_people([2, 1, 2, 0]) ➞ 4
_____



[Notes]

___
*) All attendees are included in the list.
*) Any person's count includes themself.
*) Expect valid input only.
*) For the recursive version of this challenge, check out Part I.
___



[algorithms] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How can I use enumerate to count backwards?
https://stackoverflow.com/questions/50382040/how-can-i-use-enumerate-to-count-backwards
letters = ['a', 'b', 'c'] Assume this is my list. Where for i, letter in enumerate(letters) would be: 0, a 1, b 2, c How can I instead make it enumerate backwards, as: …
_________

"""
#Your code should go here:

