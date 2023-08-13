"""
####  Partitions of a Natural Number  ####

Create a function that determines the number of partitions of a natural number.
A partition of a number n is an unordered sum of one or more numbers which totals n. For example, the partitions of the number 4 are:
___
1 + 1 + 1 + 1 = 4
1 + 1 + 2 = 4
1 + 3 = 4
2 + 2 = 4
4 = 4
_____

Since partitions are unordered, the sums 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 4 are considered the same partition.


[Examples]

___
partitions(4) ➞ 5

partitions(10) ➞ 42

partitions(0) ➞ 1

partitions(1) ➞ 1

partitions(2) ➞ 2
_____



[Notes]

Remember the trivial partition n = n. Also, we say there is one way to partition zero; namely, 0 = 0.


[algorithms] [logic] [math] 



-------------------------------------------------------------------
[Resources]
_________
Integer Sequence A000041
https://oeis.org/A000041
A000041: a(n) is the number of partitions of n (the partition numbers). …
_________
_________
Generating Integer Partitions
http://jeromekelleher.net/generating-integer-partitions.html
The purpose of this page is to give an informal presentation of the algorithms I developed for my PhD thesis and subsequently turned into a research article. The basic …
_________
_________
Partition Function P
https://mathworld.wolfram.com/PartitionFunctionP.html
Gives the number of ways of writing the integer as a sum of positive integers, where the order of addends is not considered significant. By convention, partitions are …
_________
_________
Partition (number theory)
https://en.wikipedia.org/wiki/Partition_(number_theory)
In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums …
_________

"""
#Your code should go here:

