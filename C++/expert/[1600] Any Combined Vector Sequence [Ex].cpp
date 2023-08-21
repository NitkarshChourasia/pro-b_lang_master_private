/*
####  Any Combined Vector Sequence  ####

The goal is to test if a consecutive sequence can be formed. A consecutive sequence is defined as a sequence of incrementing numbers (e.g. 1, 2, 3 or 5, 6, 7, 8). The twist is that you have to consider the combination of vectors as shown. You can combine any two elements from different vectors.
___
{-5 1 3 5} => {3 5 1 -5} => {3+4  5+3  1+8  15-5} = {7 8 9 10} => true
{4 3 8  15} => {4 3 8  15}
_____

Also important is that the vectors can be of different sizes, allowing for partially unpaired numbers in some cases.
___
{2 2 2  } => {2 2 2 0} => {2+5  2+6  2+7  10+0} = {7 8 9 10} => true
{10 5 6 7} => {5 7 6 10}
_____



[Notes]

___
*) Each array has at least 2 elements.
*) Try the easier version.
___



[arrays] [logic] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Vectors are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means …
_________

*/
//Your code should go here:

