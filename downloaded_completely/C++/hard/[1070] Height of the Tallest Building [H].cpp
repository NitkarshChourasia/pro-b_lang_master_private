/*
####  Height of the Tallest Building  ####

Given an array of strings (depicting a skyline of several buildings), return in meters the height of the tallest building. Each line in the list represents 20m.


[Examples]

___
tallestBuildingHeight([
  "            ##",
  "            ##",
  "            ##",
  "###   ###   ##",
  "###   ###   ###",
  "###   ###   ###",
  "###   ###   ###"
]) ➞ "140m"

// Tallest building is 7 rows
// 7 x 20m = 140m

tallestBuildingHeight([
  "               ",
  "               ",
  "               ",
  "       #    ###",
  "      # #   ###",
  "###   ###   ###",
  "###   ###   ###"
]) ➞ "80m"

// tallest building is 4 rows
// 4 x 20m = 80m

tallestBuildingHeight([
  "                              ",
  "                         ###  ",
  "                         ###  ",
  "###                    #####  ",
  "###      #             #####  ",
  "###     ###            #####  ",
  "######  ###            #######",
  "######  ######  ###    #######",
  "###################    #######",
  "###############################",
  "###############################"
]) ➞ "200m"

// Tallest building is 10 rows
// 10 x 20m = 200m
_____



[Notes]

___
*) There may be some open sky above buildings (can't just find the length of the array).
*) There may be multiple tallest buildings (see example #2).
___



[arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________
_________
std::find
http://www.cplusplus.com/reference/algorithm/find/
Returns an iterator to the first element in the range [first, last) that compares equal to val. If no such element is found, the function returns last.
_________

*/
//Your code should go here:

