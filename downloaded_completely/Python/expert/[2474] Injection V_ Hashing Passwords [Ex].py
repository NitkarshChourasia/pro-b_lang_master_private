"""
####  Injection V: Hashing Passwords  ####

The bookstore from this collection, in an attempt to avoid further attacks, has consulted an expert who advised them to start hashing their passwords. Misunderstanding what the expert meant, the bookstore has thus hashed their admin password and required it for access to the users dictionary.
The function hashp() takes a random hashing function (sha224, sha256, sha384, or sha512) and hashes the given string. The function database() will only return users if database() is called with a str matching the hashed version of the admin password. Through social engineering, you know that the admin password is of the form password??, where the last two characters are digits (i.e. it's a number between 10 and 99).
Create a query that copies users to res.


[Examples]

___
from hashlib import *

param = "your text here"

def hashp(passw):
  return sha???(bytes(passw, "utf-8")).hexdigest()

def database(passw):
  users = {
    "alice": "password",
    "bob": "password"
  }
  admin = hashp("password??")
  return users if passw == admin else {"Error": "Access Denied"}

res = eval("search("%s")" % param)

print(res) ➞ users
_____



[Notes]

___
*) Create a string, not a function.
*) Anything present in the Tests tab which doesn't appear here is test related and irrelevant.
*) For readability, try to break your string into smaller substrings.
*) As an anti-cheat measure, naming a variable x_x is prohibited.
___



[algorithms] [data_structures] [games] [logic] 



-------------------------------------------------------------------
[Resources]
_________
hashlib
https://docs.python.org/3/library/hashlib.html
This module implements a common interface to many different secure hash and message digest algorithms. Included are the FIPS secure hash algorithms SHA1, SHA224, SHA25 …
_________

"""
#Your code should go here:

