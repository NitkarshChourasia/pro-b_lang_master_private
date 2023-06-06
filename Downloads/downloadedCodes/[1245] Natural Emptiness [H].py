"""
####  Natural Emptiness  ####

In abstract set theory, a construction due to von Neumann represents the natural numbers by sets, as follows:
___
*) 0 = [ ] is the empty set
*) 1 = 0 ∪ [ 0 ] = [ 0 ] = [ [ ] ]
*) 2 = 1 ∪ [ 1 ] = [ 0, 1 ] = [ [ ], [ [ ] ] ]
*) n = n−1 ∪ [ n−1 ] = ...
___

Write a function that receives an integer n and produces the representing set.


[Examples]

___
rep_set(0) ➞ []

rep_set(1) ➞ [[]]

rep_set(2) ➞ [[], [[]]]

rep_set(3) ➞ [[], [[]], [[], [[ ]]]]
_____



[Notes]

___
*) Make sure to use list brackets [,].
*) Technically we should use set brackets {,} instead, but Python doesn't approve.
*) A neat feature of this representation is that n < m precisely if the set representing n is contained in the set representing m.
___



[arrays] [math] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Von Neumann Ordinals
https://en.wikipedia.org/wiki/Natural_number#Constructions_based_on_set_theory
Further discussion on how natural numbers are abstractly defined in set theory.
_________
_________
Append a List to the Same List
https://www.sololearn.com/discuss/1856497/python-append-a-list-to-the-same-list
By appending a list to itself, you create a self-referencing list. This is denoted by the ellipsis ([...]). It's like a recursive function (without a break condition).
_________

"""
#Your code should go here:

