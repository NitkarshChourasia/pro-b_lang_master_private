"""
####  Deadly Virus  ####

Mubashir needs your help to identify the spread of a deadly virus. He can provide you with the following parameters:
___
*) A two-dimensional array persons, containing affected persons 'V' and unaffected persons 'P'.
*) Number of hours n, each infected person is spreading the virus to one person up, down, left and right each hour.
___

Your function should return the updated array containing affected and unaffected persons after n hours.


[Examples]

___
persons = [
  ["P", "P", "P", "P", "P"],
  ["V", "P", "P", "P", "P"],
  ["P", "P", "P", "P", "P"],
  ["P", "P", "P", "P", "P"],
  ["P", "P", "P", "P", "P"]
]


deadly_virus(persons, 0) ➞ [
  ["P", "P", "P", "P", "P"],
  ["V", "P", "P", "P", "P"],
  ["P", "P", "P", "P", "P"],
  ["P", "P", "P", "P", "P"],
  ["P", "P", "P", "P", "P"]
]

deadly_virus(persons, 1) ➞ [
  ["V", "P", "P", "P", "P"],
  ["V", "V", "P", "P", "P"],
  ["V", "P", "P", "P", "P"],
  ["P", "P", "P", "P", "P"],
  ["P", "P", "P", "P", "P"]
]

deadly_virus(persons, 2) ➞ [
  ["V", "V", "P", "P", "P"],
  ["V", "V", "V", "P", "P"],
  ["V", "V", "P", "P", "P"],
  ["V", "P", "P", "P", "P"],
  ["P", "P", "P", "P", "P"]
]
_____



[Notes]

N/A


[algorithms] [arrays] [language_fundamentals] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Two-Dimensional Lists (Arrays)
https://snakify.org/en/lessons/two_dimensional_lists_arrays/
The first element of a here — a[0] — is a list of numbers [1, 2, 3]. The first element of this new list is a[0][0] == 1; moreover, a[0][1] == 2, a[0][2] == 3, a[1][0] = …
_________

"""
#Your code should go here:

