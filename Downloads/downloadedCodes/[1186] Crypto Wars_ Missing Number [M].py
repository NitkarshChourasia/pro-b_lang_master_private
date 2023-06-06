"""
####  Crypto Wars: Missing Number  ####

Our fleet managed to get one of the enemy's top-secret codes from the remains of its fallen ship. The codes were immediately sent over to our code-breaking base over at Bleckley Park ;) for analysis. The team found that each code contains 25 numbers with one missing. The missing number corresponds to a letter in the English alphabet. Your job is to find a more efficient Method of decrypting the messages by digitizing the process.
Write a function that takes a list, detects the missing number (in the list), and returns its corresponding letter.


[Examples]

___
decrypt([19, 12, 14, 21, 22, 3, 11, 20, 9, 16, 24, 17, 2, 10, 13, 18, 7, 8, 4, 5, 1, 6, 25, 23, 26]) ➞ "O"
# The missing number is 15.

decrypt(24, 12, 2, ..., 25) ➞ "N"
# The missing number is 14.

decrypt(24, 12, 2, ..., 25) ➞ "P"
# The missing number is 16.
_____



[Notes]

___
*) The list will only contain positive integers from 1 to 26 with one missing.
*) There will be no duplicate numbers.
*) Return the capital letter.
___



[arrays] [cryptography] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Set pop()
https://www.geeksforgeeks.org/python-set-pop/
This in-built function of Python helps to pop out elements from a set just like the principal used in the concept while implementing Stack. This method removes a random …
_________
_________
Python Arrays
https://www.w3schools.com/python/python_arrays.asp
Is a special variable, which can hold more than one value at a time.
_________
_________
Python A1Z26 Cipher
https://talkgeekto.me/2017/12/13/python-cipher-series-a1z26-cipher/
The first cipher is the most basic, the A1Z26 cipher. All you have to do is convert each letter into it’s numeric value, meaning A=1, B=2, C=3, … Z=26. There are seve …
_________
_________
chr() in Python
https://www.geeksforgeeks.org/chr-in-python/#:~:text=Itertools.Product()-,chr()%20in%20Python,code%20point%20is%20an%20integer.&text=The%20chr()%20method%20takes,(0x10FFFF%20in%20base%2016).
Returns a string representing a character whose Unicode code point is an integer.
_________

"""
#Your code should go here:

