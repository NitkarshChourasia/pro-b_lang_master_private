/*
####  Stand in Line [Queueing]  ####

Write a function that takes a vector and an integer as arguments. Add the number to the end of the vector, then remove the first element of the vector. The function should then return the updated vector.


[Examples]

___
nextInLine({5, 6, 7, 8, 9}, 1) ➞ {6, 7, 8, 9, 1}

nextInLine({7, 6, 3, 23, 17}, 10) ➞ {6, 3, 23, 17, 10}

nextInLine({1, 10, 20, 42 }, 6) ➞ {10, 20, 42, 6}

nextInLine({}, 6) ➞ {}
_____



[Notes]

___
*) For an empty vector input, return an empty vector.
*) This challenge also is an introduction to the concept of queueing.
___



[arrays] [conditions] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/?kw=vector
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________
_________
vector::push_back
http://www.cplusplus.com/reference/vector/vector/push_back/
How to add to a vector.
_________
_________
vector::erase
http://www.cplusplus.com/reference/vector/vector/erase/
How to remove items from a vector.
_________
_________
Namespaces
https://www.cplusplus.com/doc/oldtutorial/namespaces/
Allow to group entities like classes, objects and functions under a name. This way the global scope can be divided in "sub-scopes", each one with its own name.
_________
_________
My Personal Vector Header
https://github.com/chessset5/cpp-vector-header-example/blob/main/Pro6Vector.h
THIS IS NOT THE OFFICIAL VECTOR FILE. This is just my personal vector file I created for school, I am posting it here if you want to check it out.
_________

*/
//Your code should go here:

