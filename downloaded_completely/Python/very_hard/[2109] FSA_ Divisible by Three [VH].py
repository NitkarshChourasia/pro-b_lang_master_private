"""
####  FSA: Divisible by Three  ####

Create a function which checks if a binary number is divisible by three by implementing the following finite-state automaton:

The function should implement the following commands:
___
*) 0, 1 ➞ The next digit in the number.
*) "state" ➞ The automaton's current state: "S0", "S1", or "S2".
*) "stop" ➞ Whether the automaton accepts or rejects the number that's been given. The function should either return "accept" or "reject".
___



[Examples]

___
divisible(1)(1)(0)(1)(0)("stop") ➞ "reject"
# 26 is not divisible by 3, and 26 == 0b11010

divisible("state") ➞ "S0"
# The automaton should start at S0

divisible(1)(0)(1)("state") ➞ "S2"
_____



[Notes]

___
*) The function should be capable of handling arbitrarily long binary numbers.
*) The function will only be fed valid inputs.
*) The function should terminate after a "state" or "stop" command.
*) In this case, acceptance occurs if the state at termination is "S0", whereas rejection occurs if the state at termination is "S1" or "S2".
*) The int function is disabled to prevent conversion from binary to decimal.
___



[closures] [functional_programming] [higher_order_functions] 



-------------------------------------------------------------------
[Resources]
_________
Python Functions with Multiple Parameter Brackets
https://stackoverflow.com/questions/42874825/python-functions-with-multiple-parameter-brackets
Python Functions with Multiple Parameter Brackets.
_________
_________
Finite-State Machine
https://en.wikipedia.org/wiki/Finite-state_machine
A mathematical model of computation. It is an abstract machine that can be in exactly one of a finite number of states at any given time. The FSM can change from one st …
_________

"""
#Your code should go here:

