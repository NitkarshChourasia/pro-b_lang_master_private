/*
####  Palindrome Sequence  ####

A palindrome is a number that is the same when reversed, 2770772 for example. A palindrome can often be formed by adding a number to it's reverse: 641 + 146 = 787 (a palindrome). Using 78 as the seed, it takes 4 steps to produce a palindrome:
___
78 + 87 = 165
165 + 561 = 726
726 + 627 = 1353
1353 + 3531 = 4884 (a palindrome)
_____

About 97% of integers less than 10,000 produce palindromes in less than 25 steps. A few, like 196 and 879, may never form palindromes.
Make a function that takes a palindrome as it's an argument and returns the smallest seed integer that will produce that palindrome, along with the number of steps required:
___
PalSeq(palindrome) = (seed, steps)
_____

___
PalSeq(4884) ➞ (69, 4)

PalSeq(1) ➞ (1, 0)

PalSeq(11) ➞ (10, 1)
# 10 + 01 = 11

PalSeq(3113) ➞ (199, 3)

PalSeq(8836886388) ➞ (177, 15)
_____



[Notes]

The sequence always terminates when the first palindrome is produced. If the seed is a palindrome, the sequence has 0 steps.


[loops] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Palindrome Program
https://dotnettutorials.net/lesson/palindrome-program-in-csharp/
In this article, the author is going to discuss the Palindrome Program in C# (Palindrome Number and Palindrome String) with Examples.
_________

*/
//Your code should go here:

