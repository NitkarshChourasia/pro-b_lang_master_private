"""
####  FSA: Creating Machines  ####

Create a finite-state automaton that determines whether a binary number is divisible by five. The finite-state automaton from this challenge can be constructed as follows:


[Example FSA]

___
divisible = {
  "S0": ["S0", "S1"],
  "S1": ["S2", "S0"],
  "S2": ["S1", "S2"]
}
_____

Each key is a state, and each value denotes instructions for each type of input. For "S0", the array ["S0", "S1"] indicates that if a 0 is received, the new state is "S0". If 1 is received, the new state is "S1".


[Notes]

___
*) Remember to create a dictionary, not a function.
*) In this case, "accept" would mean that the number is divisible by five, whereas "reject" means that it isn't.
*) The starting and accepting states should both be "S0".
*) The automaton should read the digits of a binary number from left to right. For example, the first digit for 26 (0b11010) would be 1, since we ignore the 0b.
___



[data_structures] [functional_programming] [math] 



-------------------------------------------------------------------
[Resources]
_________
7 Deterministic Finite Automata (DFA) of Binary Number divisible by 5
https://www.youtube.com/watch?v=UWrhRBfF6vM&ab_channel=saurabhschool
Design a DFA where when binary string when represented as binary number ...
_________
_________
Finite-State Machine
https://en.wikipedia.org/wiki/Finite-state_machine
A mathematical model of computation. It is an abstract machine that can be in exactly one of a finite number of states at any given time. The FSM can change from one st …
_________

"""
#Your code should go here:

