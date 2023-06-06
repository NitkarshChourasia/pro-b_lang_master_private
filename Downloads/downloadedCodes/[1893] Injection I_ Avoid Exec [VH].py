"""
####  Injection I: Avoid Exec  ####

In order to improve your Python skills, you decide to go to an online bookstore that exclusively sells beginner Python books. You can search through the site by setting the param variable to a string containing your keyword(s); however, you notice that an error is thrown whenever your search contains a double quote.
You look through the site's Python code and notice that it uses exec() to set the result of your search to a variable named res. Create a query that copies the users dictionary (containing everyone's username and password) to res.


[Examples]

___
param = "your text here"

users = {
  "user1": "password",
  "user2": "password"
}

exec("res = search('%s')" % param)

print(res) ➞ users
_____



[Notes]

___
*) Create a string, not a function.
*) The rest of the Injection challenges can be found here.
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
exec() Method
https://www.programiz.com/python-programming/methods/built-in/exec
Executes the dynamically created program, which is either a string or a code object.
_________
_________
% v.s. format()
https://stackoverflow.com/questions/5082452/string-formatting-vs-format
Python 2.6 introduced the str.format() method with a slightly different syntax from the existing % operator. Which is better and for what situations? The following use …
_________

"""
#Your code should go here:

