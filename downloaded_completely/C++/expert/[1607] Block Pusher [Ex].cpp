/*
####  Block Pusher  ####

Create a function which returns the state of a board after n moves. There are different types of blocks on the board, which are represented as strings.
___
*) > is a pusher which moves right every turn, and pushes a block to the right if it occupies the same space as it.
*) '#' is a block which can be pushed by the pusher. If a block is pushed onto another block, then the other block also joins the push chain!
*) '-' is an empty space, which a block can be pushed into.
___

Note that the pusher can push any number of blocks at a time, but is always stopped if the push chain hits the end of the list.


[Examples]

___
blockPushing(['-', '>', '#', '-', '#', '-', '-', '-'], 1) ➞ ['-', '-', '>', '#', '#', '-', '-', '-']

blockPushing(['>', '#', '-', '#', '-', '-', '#'], 10) ➞ ['-', '-', '-', '>', '#', '#', '#']

blockPushing(['>', '-', '>', '#', '-', '-', '#', '-'], 2) ➞ ['-', '-', '>', '-', '>', '#', '#', '-']

blockPushing(['>', '>', '>', '-'], 3) ➞ ['-', '>', '>', '>']
_____



[Notes]

___
*) There may be more than one pusher at a time on the board.
*) Pushers are solid blocks, so a push chain of pushers should also stop when hitting the end of the list.
___



[arrays] [games] [loops] 



-------------------------------------------------------------------
[Resources]
_________
find_last_of in C++ with Examples
https://www.geeksforgeeks.org/stdstringfind_last_of-in-c-with-examples/
The std::string::find_last_of is a string class member function which is used to find the index of last occurrence of any characters in a string. If the character is pr …
_________

*/
//Your code should go here:

