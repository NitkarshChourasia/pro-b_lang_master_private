"""
####  Word Chain 2.0  ####

Let's update our previous word-chain definition. In this 2.0 version, a word-chain is an array of words, where the next word is formed by either:

Note: You can only do one (not both) for each word change.


[Examples]

___
isWordChain(["row", "crow", "crown", "brown", "brawn"]) ➞ True
# add "c" to "row" to get "crow", "n" to get "crown", etc. 

isWordChain(["flew", "flaw", "flan", "flat", "fat", "rat", "rot", "tot"]) ➞ True

isWordChain(["meek", "meet", "meat", "teal"]) ➞ False
# "meat" => "teal" changes 2 letters (can only change 1)

isWordChain(["run", "runny", "bunny"]) ➞ False
# "run" => "runny" adds 2 letters (can only add 1)
_____



[Notes]

___
*) All words will be in lower-case.
___



[arrays] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Levenshtein Distance
https://en.wikipedia.org/wiki/Levenshtein_distance
A string metric for measuring the difference between two sequences.
_________

"""
#Your code should go here:

