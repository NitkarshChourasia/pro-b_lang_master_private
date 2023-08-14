"""
####  Find the Maximum Length of a Chain Consisting from the Given Pairs  ####

The function is given a list of tuples. Each tuple has two numbers tpl[0] < tpl[1]. A chain can be made from these tuples that satisfies the condition: (n1, n2) -> (n3, n4) -> ... for each pair of consecutive tuples n2 < n3. Find the maximum length of such chain made from the given list.


[Examples]

___
len_longest_chain([(2, 3), (3, 4), (3, 5)]) ➞ 1
# Any of the given tuple make a chain of length 1

len_longest_chain([(2, 3), (3, 4), (1, 2)]) ➞ 2
# (1, 2) -> (3, 4) => len_chain = 2

len_longest_chain([(-15, -11), (17, 22), (8, 12), (-11, -10), (-4, -1)]) ➞ 4
# (-15, -11) -> (-4, -1) -> (8, 12) -> (17, 22) => len_chain = 4

len_longest_chain([(-5, 0), (-4, 0), (4, 5), (3, 4), (-1, 1), (-6, -2)]) ➞ 3
# (-6, -2) -> (-1, 1) -> (3, 4) => len_chain = 3
_____



[Notes]

N/A


[algorithms] [arrays] [conditions] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Dynamic programming
https://en.wikipedia.org/wiki/Dynamic_programming
Dynamic programming is both a mathematical optimization method and a computer programming method. The method was developed by Richard Bellman in the 1950s and has found …
_________

"""
#Your code should go here:

