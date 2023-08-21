/*
####  Coin Trouble  ####

Given an array of coins, father needs to distribute them amongst his three children. Write a function to determine if the coins can be distributed equally or not. Return true if each son receives the same amount of money, otherwise return false.
___
[1, 2, 3, 2, 2, 2, 3] ➞ true
_____

___
*) Amount to be distributed to each child = (1+2+3+2+4+3)/3 => 15/3 => 5
*) Possible set of coin to be distributed to children = [(1,2,2),(2,3),(2,3)]
___

___
[5, 3, 10, 1, 2] ➞ false
_____

___
*) Amount to be distributed to each child = (5+3+10+1+2)/3 => 21/3 => 7
*) But there are no combination such that each child get equal value which is 7.
___



[Examples]

___
coinsDiv([1, 2, 3, 2, 2, 2, 3]) ➞ true

coinsDiv([5, 3, 10, 1, 2]) ➞ false

coinsDiv([2, 4, 3, 2, 4, 9, 7, 8, 6, 9]) ➞ true
_____



[Notes]

___
*) Inputs will be an array of positive integers only.
*) Coin can be any positive value.
___



[arrays] [logic] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Partition of a Set Into K Subsets With Equal Sum
https://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/
Given an integer array of N elements, the task is to divide this array into K non-empty subsets such that the sum of elements in every subset is same. All elements of t …
_________

*/
//Your code should go here:

