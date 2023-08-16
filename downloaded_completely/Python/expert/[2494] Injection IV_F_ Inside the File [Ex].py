"""
####  Injection IV.F: Inside the File  ####

The bookstore from this collection is adamant in using eval(), but has moved the user’s records into a file to prevent copying. For security, the bookstore also creates several files with fake user records to obscure the intruder. The check_user(user_name) function returns entries for users which match a given username.
Create a query that copies all user records to res as list of strings.


[Examples]

___
# User’s records are stored in a file line by line (name password):
# u_etfylfe p_mmc
# u_vlrw p_davcx
# u_uau p_svlb
# u_yup p_htdgr
# u_tvhfjccd p_dlohtcjoz

res = eval("check_user(\"{}\")".format(user_name),
           {'check_user': check_user})

print(res) ➞ real_users
_____



[Notes]

Create a string, not a function.


[data_structures] [games] [logic] [strings] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

