"""
####  Let the Dominoes Fall Down  ####

The function is given a string consisting of a mix of three characters representing which direction a domino is tilted:
___
*) "R" tilted to the right
*) "L" tilted to the left
*) "I" standing up, not tilted
___

The string represents the initial state of the assembly. After a time click the overall state can change. The tilted dominoes tend to tilt their standing-up neighbors. The propagation speed is the same for left and right. The following rules are applied:
___
*) "RI" will change to "RR" unless "I" is being pushed from two opposite directions at the same time.
*) "IL" will change to "LL" unless "I" is being pushed from two opposite directions at the same time.
*) "RIL" will stay unchanged because "I" is being pushed from two opposite directions at the same time.
*) "RIIL" will change to "RRLL" after one click.
*) "RR", "LL" "RL" will stay unchanged.
*) Some "I"s at the ends of the string may stay unaffected if no push came to them.
___

Determine the final state of the assembly after all propagations have been exhausted and return it as a string (of the same length).


[Examples]

___
dominoes_fall("") ➞ ""
# No dominoes in the assembly.

dominoes_fall("RIIII") ➞ "RRRRR"
# Propagation starts on the left causing all others to tilt right.

dominoes_fall("IIIIL") ➞ "LLLLL"
# Propagation starts on the right causing all others to tilt left.

dominoes_fall("RIIIL") ➞ "RRILL"
# After one click second and fourth tilt and then the middle one is pushed by two opposing forces.

dominoes_fall("IRIIL") ➞ "IRRLL"
# The first one has not received any push.

dominoes_fall("IRRIL") ➞ "IRRIL"
# The assembly is already in the final stage. No propagation was launched.
_____



[Notes]

Keep in mind that the state changes time click after time click.


[algorithms] [logic] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________

"""
#Your code should go here:

