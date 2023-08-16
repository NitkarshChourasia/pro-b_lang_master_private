"""
####  Switch on the Gravity  ####

Given a 2D array of some suspended blocks (represented as hastags), return another 2D array which shows the end result once gravity is switched on.


[Examples]

___
switch_gravity_on([
  ["-", "#", "#", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"]
]) ➞ [
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "#", "#", "-"]
]

switch_gravity_on([
  ["-", "#", "#", "-"],
  ["-", "-", "#", "-"],
  ["-", "-", "-", "-"],
]) ➞ [
  ["-", "-", "-", "-"],
  ["-", "-", "#", "-"],
  ["-", "#", "#", "-"]
]

switch_gravity_on([
  ["-", "#", "#", "#", "#", "-"],
  ["#", "-", "-", "#", "#", "-"],
  ["-", "#", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-"]
]) ➞ [
  ["-", "-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-"],
  ["-", "#", "-", "#", "#", "-"],
  ["#", "#", "#", "#", "#", "-"]
]
_____



[Notes]

Each block falls individually, meaning there are no rigid objects. Think about it like falling sand in Minecraft as opposed to the rigid blocks in Tetris.


[arrays] [logic] [loops] [physics] 



-------------------------------------------------------------------
[Resources]
_________
Two Dimensional Lists / Arrays
https://snakify.org/en/lessons/two_dimensional_lists_arrays/
In real-world Often tasks have to store rectangular data table. [say more on this!] Such tables are called matrices or two-dimensional arrays. In Python any table can b …
_________

"""
#Your code should go here:

