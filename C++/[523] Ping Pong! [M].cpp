/*
####  Ping Pong!  ####

A game of table tennis almost always sounds like Ping! followed by Pong! Therefore, you know that Player 2 has won if you hear Pong! as the last sound (since Player 1 didn't return the ball back).
Given an array of Ping!, create a function that inserts Pong! in between each element. Also:
___
*) If win equals true, end the list with Pong!.
*) If win equals false, end with Ping! instead.
___



[Examples]

___
pingPong(["Ping!"], true) ➞ ["Ping!", "Pong!"]

pingPong(["Ping!", "Ping!"], false) ➞ ["Ping!", "Pong!", "Ping!"]

pingPong(["Ping!", "Ping!", "Ping!"], true) ➞ ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"]
_____



[Notes]

___
*) You will always return the ball (i.e. the Pongs are yours).
*) Player 1 serves the ball and makes Ping!.
*) Return an array of strings.
___



[algorithms] [arrays] [games] 



-------------------------------------------------------------------
[Resources]
_________
vector::insert
http://www.cplusplus.com/reference/vector/vector/insert/
The vector is extended by inserting new elements before the element at the specified position, effectively increasing the container size by the number of elements inserted.
_________
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________

*/
//Your code should go here:

