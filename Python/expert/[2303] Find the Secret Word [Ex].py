"""
####  Find the Secret Word  ####

This string, "sadbpstcrdvaefikkgoenqrt" has a five letter word embedded within it.
Here's a clue on how to find it:

Given the string and length of the secret word, improvise a function that finds the secret word.


[Examples]

___
secret_word("sadbpstcrdvaefikkgoenqrt", 5) ➞ "brake"
# sa(dbp)st(crd)(vae)f(ikk)g(oen)qrt
# The values of the triplets in parentheses are 22, 25, 28, 31, 34.
# An arithmetic series with difference of 3.

secret_word("aheiayd", 3) ➞ "hey"
# (a[he)i](ayd)
# The triplets with the secret letters can overlap.
# ahe=14, hei=22, ayd=30; a series with a difference of 8.
_____



[Notes]

N/A


[algorithms] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
Depth-first search
https://en.wikipedia.org/wiki/Depth-first_search#:~:text=Depth%2Dfirst%20search%20(DFS),along%20each%20branch%20before%20backtracking.
Is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the …
_________

"""
#Your code should go here:

