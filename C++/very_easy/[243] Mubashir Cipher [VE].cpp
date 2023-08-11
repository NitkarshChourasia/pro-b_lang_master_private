/*
####  Mubashir Cipher  ####

In Mubashir Cipher, encoding is done by simply replacing paired letters from the provided key.
Create a function that takes a string containing the message to be encoded with a fixed given 2D array of letters key.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
key = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'],
    ['s', 'v'], ['h', 'x'], ['i', 'z'], ['r', 'y'],
    ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]

message = "edabit is amazing !"

mubashirCipher(message) ➞ "uqkgzf zv kckizlb !"
_____

Step 1: Search letter in the given key and replace it with paired letter:
___
e = u
d = q
a = k
b = g
.
.
.
g = b
_____

Step 2: Keep all characters (including spaces) other than letters in their original positions:
___
"uqkgzf zv kckizlb !"
_____

See the below examples for a better understanding:


[Examples]

___
mubashirCipher("mubashir is not amazing") ➞ "cegkvxzy zv ljf kckizlb"

mubashirCipher("%$ &%") ➞ "%$ &%"

mubashirCipher("evgeny sh is amazing") ➞ "usbulr vx zv kckizlb"
_____



[Notes]

N/A


[algorithms] [cryptography] [logic] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Conditions and If Statements
https://www.w3schools.com/cpp/cpp_conditions.asp
C++ supports the usual logical conditions from mathematics. You can use these conditions to perform different actions for different decisions. C++ has the following co …
_________
_________
For Loops
https://www.w3schools.com/cpp/cpp_for_loop.asp
When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop.
_________
_________
Vector of Vectors
https://www.geeksforgeeks.org/vector-of-vectors-in-c-stl-with-examples/
Vectors are known as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automatical …
_________

*/
//Your code should go here:

