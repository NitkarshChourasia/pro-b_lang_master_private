"""
####  Minimum Number of Genetic Mutations  ####

A gene is represented by an 8-character long string containing: "A", "C", "G", "T". Gene mutation is defined as when a single character is changed in the gene string.
For example, "AACCGGTT" -> "AACCGGTA" is a mutation because only the last character is different.
Also, there is a list of genes, bank, which contains all the valid / allowed gene mutations.
The function is given start, end, and bank. Determine the minimum number of mutations needed to mutate from start to end. If there is no mutation chain found return -1.


[Examples]

___
min_mutations("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) ➞ 1

min_mutations("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]) ➞ 2

min_mutations("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]) ➞ 3

min_mutations("AAAAACCC", "AACTCCCC", ["AAAACCCC", "AAACCCCC", "AACTCCCC"]) ➞ -1
_____



[Notes]

___
*) The starting point is valid, so it might not be included in the bank. The endpoint is included.
*) All mutations in the searched sequence must be found in the bank.
___



[algorithms] [logic] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Breadth-first search
https://en.wikipedia.org/wiki/Breadth-first_search
Breadth-first search (BFS) is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all n …
_________

"""
#Your code should go here:

