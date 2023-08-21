/*
####  Need Help With Your Packing?  ####

You arrive at the supermarket checkout and you've only got a limited number of shopping bags with you. Miser that you are, you hate buying extra bags when you've got dozens at home that you forgot to bring with you!! Can you fit all your shopping into the bags you've got with you?
Each bag can carry a maximum of 10kg and each item you've purchased weighs between 1 and 10kg.
Create a function that takes two parameters, a list of the weights of each item and the number of bags you are carrying. Return true if there are enough bags to contain all the items, otherwise false.


[Example]

___
canFit([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2], 4) ➞ true
// Bag 1 = [2, 1, 2, 5] (10kg)
// Bag 2 = [4, 3, 3] (10kg)
// Bag 3 = [6, 2, 1, 1] (10kg)
// Bag 4 = [9] (9kg)

canFit([2, 7, 1, 3, 3, 4, 7, 4, 1, 8, 2], 4) ➞ false
// Bag 1 = [2, 8] (10kg)
// Bag 2 = [3, 7] (10kg)
// Bag 3 = [2, 4, 4] (10kg)
// Bag 4 = [7, 3] (10kg)
// two 1kg items left over!
_____



[Notes]

___
*) All weights will be integers between 1 and 10kg inclusive
*) Items can be packed in any order
*) There may be more than one way to fit all the items in the available bags
___

Based on an easier challenge How Many Boxes? by @zatoichi49.


[algorithms] [logic] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to use an array element in if-statement?
https://www.daniweb.com/programming/software-development/threads/178126/how-to-use-an-array-element-in-if-statement
In one function, the user will enter a 9-character string that will be stored in an array (AcctNum[10], to allow for the terminating null-character). One of the things …
_________
_________
std::accumulate()
https://www.geeksforgeeks.org/accumulate-and-partial_sum-in-c-stl-numeric-header/
This header is part of the numeric library in C++ STL. This article explains some useful functions in the numeric header which can be used during competitive programmin …
_________
_________
std::sort()
https://www.geeksforgeeks.org/sort-c-stl/
It generally takes two parameters , the first one being the point of the array/vector from where the sorting needs to begin and the second parameter being the length up …
_________

*/
//Your code should go here:

