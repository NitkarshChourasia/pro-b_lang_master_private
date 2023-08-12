"""
####  Prime Numbers at Prime Indices  ####

The function is given an integer n. Make a list lst = [1, 2, 3, ..., n]. Consider all possible permutations of lst. Find out how many permutations are such that all prime numbers from the list are located at prime-index positions, imagining that the list indices are 1-based. The number of such permutations can be large, thus return n_permutations % (10**9 + 7).


[Examples]

___
num_prime_arrangements(3) ➞ 2
# [1, 2, 3], [1, 3, 2] -> 2 permutations
# [2, 1, 3] cannot be counted because prime number 2 is at position not prime 1

num_prime_arrangements(4) ➞ 4
# [1, 2, 3, 4], [4, 2, 3, 1], [1, 3, 2, 4], [4, 3, 2, 1] -> 4 permutations
# prime numbers 2, 3 at prime positions 2, 3

num_prime_arrangements(5) ➞ 12
# [1, 2, 3, 4, 5], [4, 2, 3, 1, 5], etc -> 12 permutations
_____



[Notes]

The given input is 2 < n < 101.


[algorithms] [arrays] [logic] [math] 



-------------------------------------------------------------------
[Resources]
_________
Prime Number
https://en.wikipedia.org/wiki/Prime_number
Is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. …
_________

"""
#Your code should go here:

