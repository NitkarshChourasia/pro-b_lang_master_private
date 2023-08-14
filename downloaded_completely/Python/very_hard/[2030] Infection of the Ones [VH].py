"""
####  Infection of the Ones  ####

Write a function that replaces every row and column that contains at least one 1 into a row/column that is filled entirely with 1s.
Solve this without returning a copy of the input list.


[Examples]

___
ones_infection([
  [0, 0, 1],
  [0, 0, 0],
  [0, 0, 0]
]) ➞ [
  [1, 1, 1],
  [0, 0, 1],
  [0, 0, 1]
]

ones_infection([
  [1, 0, 1, 0],
  [0, 1, 0, 0],
  [0, 0, 0, 0]
]) ➞ [
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 0]
]

ones_infection([
  [0, 1, 0, 1],
  [0, 0, 0, 0],
  [0, 1, 0, 0]
]) ➞ [
  [1, 1, 1, 1],
  [0, 1, 0, 1],
  [1, 1, 1, 1]
]
_____



[Notes]

___
*) You must mutate the original matrix.
*) Input matrices will have at least row and one column.
*) Bonus: Solve this without using any higher-order functions.
___



[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
pandas.DataFrame.shift — pandas
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shift.html
When freq is not passed, shift the index without realigning the data. If freq is passed (in this case, the index must be date or datetime, or it will raise a NotImpleme …
_________

"""
#Your code should go here:

