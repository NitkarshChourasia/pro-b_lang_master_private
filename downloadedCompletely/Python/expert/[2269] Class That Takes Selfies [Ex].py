"""
####  Class That Takes Selfies  ####

Implement a class Selfie that can store the current state of the object in the form of binary string. It can take multiple pictures and then recover to a state it was before. During testing an object will be provided with new attributes and their values. It will store its state. Then the values will be changed. Then it will be given new attributes. It will store its state again. It will be repeated few times.
Later the states of the object will be recovered given an index. The return value should be a new Selfie with the requested historic state and the state history of the new object should be updated with a copy of current object's state history.
The object also knows how many states it has stored. If the index is not within the range of stored states, the object stays as is. If the argument is invalid, n < 0 or n >= self.n_states(), the current object (or a copy thereof) should be returned.


[Examples]

___
p = Selfie()
p.x = 2
p.save_state()
p.x = 5
p = p.recover_state(0)
p.x ➞ 2
_____



[Notes]

___
*) Use of global variables outside the class is not allowed.
*) When an object is restored to a previous state it keeps all saved states.
___



[classes] [objects] 



-------------------------------------------------------------------
[Resources]
_________
The Pickle Module
https://docs.python.org/3/library/pickle.html
Implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into …
_________

"""
#Your code should go here:

