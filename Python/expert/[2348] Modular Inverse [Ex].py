"""
####  Modular Inverse  ####

A positive integer multiplied times its inverse is always equal to 1: 17*(1/17)==1. Modular arithmetic has a similar inverse function, although, for modulus m, we are confined to integers from 0 to m-1. The modular multiplicative inverse of 3 modulus 5 is equal to 2 because (3*2)%5==1. Another example: the modular inverse of 17 modulus 1000007 is equal to 58824 because (17*58824)%1000007==1. The modular inverse, if it exists, must always be in the range 0 to m-1.
Create a function that has arguments integer n and modulus m. The function will return the modular inverse of n mod m. If the modular inverse does not exist, return False.


[Examples]

___
mod_inv(2, 3) ➞ 2

mod_inv(12, 47) ➞ 4

mod_inv(11, 33) ➞ False

mod_inv(55, 678) ➞ 37

mod_inv(81, 3455) ➞ 2346
_____



[Notes]

___
*) Some of the test cases have rather large integers, so if you attempt to do a brute force search of the entire modular field, you may not be successful due to the 12 second time limit imposed by the server. See Resources for a more efficient approach.
*) The modular inverse of a number n modulus m exists only if n and m are coprime (i.e. they have no common factors other than 1).
*) One practical use of modular inverse is in public-key cryptography like RSA where it can be used to determine the value of the private key.
___



[cryptography] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How to find Multiplicative Inverse of a number modulo M?
https://www.rookieslab.com/posts/how-to-find-multiplicative-inverse-of-a-number-modulo-m-in-python-cpp
What is Multiplicative Inverse? What is Modular Multiplicative Inverse? How to find Modular Multiplicative Inverse? How to find Multiplicative Inverse of a number modul …
_________

"""
#Your code should go here:

