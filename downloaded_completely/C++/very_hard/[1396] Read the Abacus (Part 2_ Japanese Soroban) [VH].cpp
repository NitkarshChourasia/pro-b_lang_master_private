/*
####  Read the Abacus (Part 2: Japanese Soroban)  ####

The Japanese soroban is type of abacus (counting tool) that is used by sliding threaded beads up and down wires. The soroban is divided into an upper deck (where each bead is worth 5 units) and a lower deck (where beads are worth 1 unit). Working from the right and moving to the left, units increase by a factor of 10. If we use "O" for a bead and "|" to show the wire, we can represent the soroban as follows:
___
OOOOOOO
|||||||  Upper deck
-------  Dividing line
|||||||  Lower deck
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
_____

To read the number, we count the value of the number of beads that have been moved towards the dividing line. The values for the upper and lower deck are added together. In the example below, the number is 30651:
___
OOOO||O
||||OO|
-------
||O|O|O
OOOO|O|
OOOOOOO
OO|OOOO
OOOOOOO

0000550  Upper deck
0030101  Lower deck
  30651  Total
_____

Given an array of strings representing the soroban, return the number being displayed.


[Examples]

___
soroban([
  "OOOO||O",
  "||||OO|",
  "-------",
  "|||O|OO",
  "OOOOOOO",
  "OOO|OOO",
  "OOOOO|O",
  "OOOOOO|"
]) ➞ 2584

soroban([
  "||OO||O",
  "OO||OO|",
  "-------",
  "OO|OO||",
  "OOO|OOO",
  "OOOO|OO",
  "|OOOOOO",
  "O|OOOOO"
]) ➞ 8901750
_____



[Notes]

For more info on how to use a soroban, please check the Resources tab.


[arrays] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Abacus
https://en.wikipedia.org/wiki/Abacus
The abacus (plural abaci or abacuses), also called a counting frame, is a calculating tool that was in use in the ancient Near East, Europe, China, and Russia, centurie …
_________
_________
Soroban
https://en.wikipedia.org/wiki/Soroban
Is an abacus developed in Japan. It is derived from the ancient Chinese suanpan, imported to Japan in the 14th century. Like the suanpan, the soroban is still used toda …
_________
_________
2D Vector In C++ With User Defined Size
https://www.geeksforgeeks.org/2d-vector-in-cpp-with-user-defined-size/
A 2D vector is a vector of vector. Like 2D arrays, we can declare and assign values to a 2D vector! Assuming you are familiar with a normal vector in C++, with the hel …
_________
_________
std::stoi
http://www.cplusplus.com/reference/string/stoi/
Parses str interpreting its content as an integral number of the specified base, which is returned as an int value. If idx is not a null pointer, the function also set …
_________
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Returns a string with the representation of val. The format used is the same that printf would print for the corresponding type.
_________

*/
//Your code should go here:

