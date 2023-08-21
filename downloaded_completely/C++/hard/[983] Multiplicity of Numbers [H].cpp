/*
####  Multiplicity of Numbers  ####

Write a function that returns an array of elements [number, multiplicity]. The multiplicity of a number refers to the number of times it occurs in the array.
To illustrate:
___
[5, 5, 1, 1, 5, 5, 3]
[[5, 4], [1, 2], [3, 1]]

// Since 5 appears 4 times, 1 appears twice, and 3 appears once.
_____

The final array should only include unique elements, and the elements should be ordered by when they first appeared in the original array.


[Examples]

___
multiplicity([1, 1, 1, 2, 2, 3]) ➞ [[1, 3], [2, 2], [3, 1]]

multiplicity([1, 1, 1, 1, 1]) ➞ [[1, 5]]

multiplicity([1, 5, 4, 3, 2]) ➞ [[1, 1], [5, 1], [4, 1], [3, 1], [2, 1]]
_____



[Notes]

N/A


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
What's the most efficient way to erase duplicates and sort a vector?
https://stackoverflow.com/questions/1041620/whats-the-most-efficient-way-to-erase-duplicates-and-sort-a-vector
I need to take a C++ vector with potentially a lot of elements, erase duplicates, and sort it. I currently have the below code, but it doesn't work. How can I correctly …
_________
_________
std::unique
http://www.cplusplus.com/reference/algorithm/unique/
Removes all but the first element of every consecutive group of equivalent elements.
_________

*/
//Your code should go here:

