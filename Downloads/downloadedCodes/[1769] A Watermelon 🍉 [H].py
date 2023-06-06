"""
####  A Watermelon 🍉  ####

Mubashir is eating a watermelon.
___
*) He spits out all watermelon seeds if seeds are more than five.
*) He can swallow all watermelon seeds if seeds are less than or equal to five.
*) He can eat 1/4 of a watermelon each time.
___

Given a 2D array of watermelon where 0 is representing juicy watermelon while 1 is representing seed, return total number of seeds spit-out. See below example for detailed explanation :
Given a watermelon:
___
1, 0, 0, 1, 1, 1, 0, 1
1, 0, 1, 0, 1, 1, 0, 0
1, 1, 1, 1, 0, 0, 0, 0
0, 1, 0, 1, 1, 1, 1, 0
0, 0, 0, 1, 0, 1, 0, 0
1, 1, 1, 0, 0, 0, 1, 1
1, 0, 1, 1, 0, 0, 0, 0
0, 0, 0, 0, 0, 0, 0, 0

seeds = 0
total seeds = 0
_____

Mubashir eats 1/4 piece (4x4 matrix) of watermelon :
___
x, x, x, x, 1, 1, 0, 1
x, x, x, x, 1, 1, 0, 0
x, x, x, x, 0, 0, 0, 0
x, x, x, x, 1, 1, 1, 0
0, 0, 0, 1, 0, 1, 0, 0
1, 1, 1, 0, 0, 0, 1, 1
1, 0, 1, 1, 0, 0, 0, 0
0, 0, 0, 0, 0, 0, 0, 0

seeds = 10
total seeds = 10 (All seeds were spit-out)
_____

Mubashir eats next 1/4 piece (4x4 matrix) of watermelon :
___
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
0, 0, 0, 1, 0, 1, 0, 0
1, 1, 1, 0, 0, 0, 1, 1
1, 0, 1, 1, 0, 0, 0, 0
0, 0, 0, 0, 0, 0, 0, 0

seeds = 8
total seeds = 10+8 = 18 (All seeds were spit-out)
_____

Mubashir eats next 1/4 piece (4x4 matrix) of watermelon :
___
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, 0, 1, 0, 0
x, x, x, x, 0, 0, 1, 1
x, x, x, x, 0, 0, 0, 0
x, x, x, x, 0, 0, 0, 0

seeds = 7
total seeds = 18+7 = 25 (All seeds were spit-out)
_____

Mubashir eats last 1/4 piece (4x4 matrix) of watermelon :
___
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x

seeds = 3
total seeds = 25+0 = 25
_____



[Examples]

___
total_seeds(watermelon) ➞ 25
_____



[arrays] [loops] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
For Loop
https://www.programiz.com/python-programming/for-loop
Is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
_________

"""
#Your code should go here:

