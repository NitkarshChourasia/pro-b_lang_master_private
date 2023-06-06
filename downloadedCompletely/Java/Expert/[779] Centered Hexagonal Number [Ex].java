/*
####  Centered Hexagonal Number  ####

As stated on the On-Line Encyclopedia of Integer Sequences:

A centered hexagonal number is a centered figurate number that represents a hexagon with a dot in the center and all other dots surrounding the center dot in a hexagonal lattice.
At the end of that web page the following illustration is shown:
___
Illustration of initial terms:
.
.                                 o o o o
.                   o o o        o o o o o
.         o o      o o o o      o o o o o o
.   o    o o o    o o o o o    o o o o o o o
.         o o      o o o o      o o o o o o
.                   o o o        o o o o o
.                                 o o o o
.
.   1      7          19             37
.
_____

Write a function that takes an integer n and returns "Invalid" if n is not a centered hexagonal number or its illustration as a multiline rectangular string otherwise.


[Examples]

___
hexLattice(1) ➞ " o "
// o

hexLattice(7) ➞ "  o o  \n o o o \n  o o  "
//  o o
// o o o
//  o o

hexLattice(19) ➞ "   o o o   \n  o o o o  \n o o o o o \n  o o o o  \n   o o o   "
//   o o o
//  o o o o
// o o o o o
//  o o o o
//   o o o

hexLattice(21) ➞ "Invalid"
_____



[Notes]

N/A


[formatting] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Centered Hexagonal Number
https://en.wikipedia.org/wiki/Centered_hexagonal_number#:~:text=The%20first%20few%20centered%20hexagonal,%2C%20721%2C%20817%2C%20919.
Is a centered figurate number that represents a hexagon with a dot in the center and all other dots surrounding the center dot in a hexagonal lattice. Centered hexagona …
_________
_________
Centered Hexagonal Numbers
https://oeis.org/A003215
Hex (or centered hexagonal) numbers: 3*n*(n+1)+1 (crystal ball sequence for hexagonal lattice).
_________

*/
//Your code should go here:

