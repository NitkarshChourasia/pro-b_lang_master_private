/*
####  Helping Alex with Treasure  ####

Alex and Cindy, two students who recently spent some time on treasure hunting. Apart from scrap metal, they found a number of boxes full of old coins. Boxes are of different value and now are lined up in a row. Cindy proposes an idea to divide the treasure into two parts. She thinks that a fair way is that she and Alex take turns, and each of them chooses one box from either left or right side of the line. Cindy is a very generous person and lets Alex to go first.
Alex wants to check whether this idea is actually good for him. He asks you to write a program to calculate the total value that he will get compared to how much Cindy will get if he chooses a box first. You can be sure that they both are very smart, and always select the next box in such way that it leads to the best overall individual solution for them. This means they may not always choose the highest value box of the two currently available in order to ensure they get a higher value box later.


[Examples]

___
Solve([7, 2]) ➞ 5
// Alex will choose the 7, and then Cindy gets the 2.
// So the result is 7 ‐ 2 = 5.

Solve([2, 7, 3]) ➞ ‐2
// It doesn't matter whether Alex chooses the 2 or the 3. Cindy will
// choose the 7 and Alex will get the remaining box. (2+3) ‐ 7 = ‐2.

Solve([1000, 1000, 1000, 1000, 1000]) ➞ 1000
// Since Alex chooses first, he will get 3 boxes and Cindy will get only 2.
// They all have the same value so (1000+1000+1000) ‐ (1000+1000) = 1000.

Solve([823, 912, 345, 100000, 867, 222, 991, 3, 40000]) ➞ ‐58111
_____



[Notes]

N/A


[algorithms] [arrays] [data_structures] [functional_programming] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

