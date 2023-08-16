/*
####  Ordering People in a Line  ####

Create a function that takes in the size of the line and the number of people waiting and places people in an S-shape ordering, returning the result as string. The demonstration below will make it clear:
___
# Ordering numbers 1-15 in a 5 x 3 space.

OrderPeople(5, 3, 15) ➞ 
1, 2, 3
6, 5, 4
7, 8, 9
12, 11, 10
13, 14, 15
_____

If there is extra room, leave those spots blank with a 0 filler.
___
# Ordering numbers 1-5 in a 4 x 3 space.

OrderPeople(4, 3, 5) ➞
1, 2, 3
0, 5, 4,
0, 0, 0,
0, 0, 0
_____

If there are too many people for the given dimensions, return "overcrowded".
___
OrderPeople(4, 3, 20) ➞ "overcrowded"
_____



[Examples]

___
OrderPeople(3, 3, 8) ➞
1, 2, 3
6, 5, 4
7, 8, 0

OrderPeople(2, 4, 5) ➞
1, 2, 3, 4
0, 0, 0, 5

OrderPeople(2, 4, 10) ➞ "overcrowded"
_____



[Notes]

___
*) Always start the ordering on the upper-left corner.
*) Return the the result as a string e.g. "1, 2, 3\n6, 5, 4\n7, 8, 9\n12, 11, 10\n13, 14, 15". Note the spacing of the numbers and the new line character \n between each row.
*) If the S-shape concept doesn't make sense, try writing down some of these examples on a piece of paper and tracing a pencil through the numbers in order.
___



[arrays] [loops] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

