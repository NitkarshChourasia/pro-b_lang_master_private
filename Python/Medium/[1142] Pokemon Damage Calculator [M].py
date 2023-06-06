"""
####  Pokemon Damage Calculator  ####

It's a Pokemon battle! Your task is to calculate the damage that a particular move would do using the following formula (not the actual one from the game):
___
damage = 50 * (attack / defense) * effectiveness
_____

___
*) attack = your attack power
*) defense = the opponent's defense
*) effectiveness = the effectiveness of the attack based on the matchup (see explanation below)
___

Effectiveness:
Attacks can be super effective, neutral, or not very effective depending on the matchup. For example, water would be super effective against fire, but not very effective against grass.
___
*) Super effective: 2x damage
*) Neutral: 1x damage
*) Not very effective: 0.5x damage
___

To prevent this challenge from being tedious, you'll only be dealing with four types: fire, water, grass, and electric. Here is the effectiveness of each matchup:
___
*) fire > grass
*) fire < water
*) fire = electric
*) water < grass
*) water < electric
*) grass = electric
___

The function you must implement takes in:
___
*) your type
*) the opponent's type
*) your attack power
*) the opponent's defense
___



[Examples]

___
calculate_damage("fire", "water", 100, 100) ➞ 25

calculate_damage("grass", "fire", 35, 5) ➞ 175

calculate_damage("electric", "fire", 100, 100) ➞ 50
_____



[Notes]

Any type against itself is not very effective. Also, assume that the relationships between different types are symmetric (if A is super effective against B, then B is not very effective against A).


[conditions] [games] [logic] [math] 



-------------------------------------------------------------------
[Resources]
_________
Conditions and if Statements
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics: Equals: a == b, Not Equals: a != b, Less than: a < b, Less than or equal to: a <= b, Greater than: a …
_________

"""
#Your code should go here:

