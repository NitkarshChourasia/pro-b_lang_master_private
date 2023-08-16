"""
####  Injection IV: Inside the Function  ####

The bookstore from this collection is adamant in using eval(), but has moved the users dictionary into a function to prevent copying. The exists() function returns entries in users which match a given username. Create a query that copies users to res.


[Examples]

___
from re import *

param = "your text here"

def exists(name):
  users = {
    "alice": "password",
    "bob": "password"
  }
  if not name.isalnum():
    return {"Error": "No users found."}
  return {
    k:users[k] for k in users
    if type(search("^%s$" % name, k)).__name__ == "SRE_Match"
  }

res = eval("search("%s")" % param)

print(res) ➞ users
_____



[Notes]

___
*) Create a string, not a function.
*) Anything present in the Tests tab exists() function which doesn't appear here is test related and irrelevant.
*) Assume you know nothing about the usernames in the database.
*) For readability, try to break your string into smaller substrings.
___



[data_structures] [games] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Incorrectly Filtered Escape Characters
https://en.wikipedia.org/wiki/SQL_injection#Incorrectly_filtered_escape_characters
This form of injection occurs when user input is not filtered for escape characters and is then passed into an SQL statement. This results in the potential manipulation …
_________

"""
#Your code should go here:

