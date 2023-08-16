"""
####  Injection IV.E: Inside the Class  ####

The bookstore from this collection is adamant in using eval(), but has moved the users dictionary into a class to prevent copying. The check_a_user(name) function returns entries in users which match a given username. Create a query that copies users to res.


[Examples]

___
res = eval("check_a_user({})".format(user_name),
           {'check_a_user': check_a_user})

print(res) ➞ clients.all_users(control_num)
_____



[Notes]

Create a string, not a function.


[classes] [data_structures] [games] [logic] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

