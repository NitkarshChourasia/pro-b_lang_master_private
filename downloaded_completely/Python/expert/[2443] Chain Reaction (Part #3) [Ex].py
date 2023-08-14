"""
####  Chain Reaction (Part #3)  ####

This is a direct sequel to Chain Reaction (Part #2), which was an easier particular case of this challenge (my suggestion is to try that one first).
As in the previous part, you will be given a rectangular array representing a "map" with three types of spaces:
___
*) "+" bombs: when activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
*) "x" bombs: when activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
*) Empty spaces "0".
___

The goal is simple: given a map, return the minimum number of bombs that need to be set off for all bombs to be destroyed by the chain reaction.
Let's look at some examples:
___
[["+", "x"]]
_____

For the map above, the answer is 1: to explode both bombs one can pick the '+' bomb. However, note that picking the 'x' bomb does not work.
___
[
  ["+", "0", "x"],
  ["x", "x", "x"]
]
_____

For the map above, the answer is 2: one can either pick the two 'x' bombs on the right column or the center and right 'x' bombs in the bottom row. No other choice will work.
___
[
  ["x", "x", "x"],
  ["x", "+", "x"],
  ["x", "x", "x"]
]
_____

For the map above, the answer is 4: pick the four 'x' bombs in the corners. No other choice works.
___
[
  ["x", "x", "+"],
  ["+", "0", "+"],
  ["+", "x", "x"]
]
_____

For the map above, the answer is 1: any bomb other than the "x" bombs in the top left and bottom right will work.


[Examples]

___
min_bombs_needed([
  ["+", "x"]
]) ➞ 1

min_bombs_needed([
  ["+", "0", "x"],
  ["x", "x", "x"]
]) ➞ 2

min_bombs_needed([
  ["x", "x", "x"],
  ["x", "+", "x"],
  ["x", "x", "x"]
]) ➞ 4

min_bombs_needed([
  ["x", "x", "+"],
  ["+", "0", "+"],
  ["+", "x", "x"]
]) ➞ 1
_____



[Notes]

___
*) Note that both "+" and "x" bombs have an "explosion range" of 1.
*) Many strategies that worked for part #2 will fail in this one. See the Comments for some hints on how to approach this.
___



[arrays] [games] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

