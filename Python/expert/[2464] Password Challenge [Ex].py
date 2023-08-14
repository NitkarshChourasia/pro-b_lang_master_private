"""
####  Password Challenge  ####

A certain security system is responsible for maintaining a code capable of generating a key for each respective lock key = code % lock .This security system has a key ( main_key) and its respective lock( main_lock) that are fixed and serve as a base to update all the others. To maintain security, after a certain lock is accessed 10 times with the wrong key they update its lock value lock = lock + main_key.
A hacker was able to steal the main_key and the main_lock but he has no idea what the code is. Write a function that returns how many attempts the hacker needs to be sure he is able to find certain lock key, if that is impossible return "system with a high level of security".
Will be provided: main_key, main_lock and lock_x (the one you have to find how many attempts to figure the key_x).


[Examples]

___
hack(1, 2, 8) ➞ 4
# With only four attempts it is possible to access the lock.

hack(1, 2, 13) ➞ 17

hack(5, 101, 111) ➞ 996

hack(10, 101, 111) ➞ "system with a high level of security"
_____



[Notes]

All the inputs will be positive integers less than 10^6.


[cryptography] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Modular Arithmetic
https://brilliant.org/wiki/modular-arithmetic/#:~:text=Properties%20of%20addition%20in%20modular%20arithmetic%3A&text=If%20a%20%E2%89%A1%20b%20(%20m,N)%20for%20any%20integer%20k%20.&text=a%2Bc%20%5Cequiv%20b%2B,(modN).
Is a system of arithmetic for integers, which considers the remainder. In modular arithmetic, numbers "wrap around" upon reaching a given fixed quantity (this given qua …
_________

"""
#Your code should go here:

