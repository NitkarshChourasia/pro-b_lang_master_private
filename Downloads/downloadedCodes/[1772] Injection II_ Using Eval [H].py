"""
####  Injection II: Using Eval  ####

The bookstore from this collection, in a desperate attempt to avoid getting hacked, changed from exec() to eval(). Create a query that stores the users dictionary in the res variable.


[Examples]

___
param = "your text here"

users = {
  "user1": "password",
  "user2": "password"
}

res = eval('search("%s")' % param)

print(res) ➞ users
_____



[Notes]

___
*) Create a string, not a function.
*) The site dictionary and search function have been gutted/deleted for brevity.
___



[data_structures] [games] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Incorrectly Filtered Escape Characters
https://en.wikipedia.org/wiki/SQL_injection#Incorrectly_filtered_escape_characters
This form of injection occurs when user input is not filtered for escape characters and is then passed into an SQL statement. This results in the potential manipulation …
_________
_________
clear() Method
https://www.programiz.com/python-programming/methods/dictionary/clear
Removes all items from the dictionary.
_________

"""
#Your code should go here:

