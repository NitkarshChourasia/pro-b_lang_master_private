"""
####  Check Password Hash  ####

Write a function that takes a username and password and checks the list user_pass_db for a match. The list stores the passwords as a hash using the SHA1 algorithm. Return True for a match and False otherwise.


[Examples]

___
user_pass_db = [{"username" : "myUsername", "pass_hash" : "5413ee24723bba2c5a6ba2d0196c78b3ee4628d1"}]

check_pass("myUsername", "myPassword") ➞ True

check_pass("myUsername", "wrongPassword") ➞ False
_____



[Notes]

N/A


[arrays] [conditions] [cryptography] [validation] 



-------------------------------------------------------------------
[Resources]
_________
hashlib — Secure hashes and message digests
https://docs.python.org/3/library/hashlib.html
This module implements a common interface to many different secure hash and message digest algorithms. Included are the FIPS secure hash algorithms SHA1, SHA224, SHA256 …
_________
_________
Best way to convert string to bytes in Python 3?
https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
There appear to be two different ways to convert a string to bytes, as seen in the answers to TypeError: 'str' does not support the buffer interface. Which of these me …
_________

"""
#Your code should go here:

