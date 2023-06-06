"""
####  FSA: Individual Instructions  ####

Create a function that, when given a list of individual finite-state automaton instructions, generates an FSA in the form described in this challenge. Each instruction will be a list of three elements: The first element will be the current state, the second element will be the input to which the instruction pertains, and the third element will be the new state.
For example, the instruction ["S0", 1, "S1"] indicates that, if the current state is "S0", upon receiving a 1 as input, the new state will be "S1". A deconstruction of the FSA from this challenge can be seen below:


[Examples]

___
divisible = [
  ["S0", 0, "S0"], ["S0", 1, "S1"],
  ["S1", 0, "S2"], ["S1", 1, "S0"],
  ["S2", 0, "S1"], ["S2", 1, "S2"]
]

combine(divisible) ➞ {
  "S0": ["S0", "S1"],
  "S1": ["S2", "S0"],
  "S2": ["S1", "S2"]
}
_____



[Notes]

___
*) Every FSA will use a binary alphabet.
*) All states will be of the form Sn, where n is an integer, e.g. S2.
___



[arrays] [data_structures] [functional_programming] 



-------------------------------------------------------------------
[Resources]
_________
Finite-State Machine
https://en.wikipedia.org/wiki/Finite-state_machine
A mathematical model of computation. It is an abstract machine that can be in exactly one of a finite number of states at any given time. The FSM can change from one st …
_________
_________
Ways to Create a Dictionary of Lists
https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/
We have seen the ways to creating dictionary in multiple ways and different operations on the key and values in dictionary. Now, let’s see different ways of creating a …
_________

"""
#Your code should go here:

