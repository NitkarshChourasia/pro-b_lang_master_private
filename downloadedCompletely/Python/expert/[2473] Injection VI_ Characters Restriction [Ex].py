"""
####  Injection VI: Characters Restriction  ####

The bookstore from this collection is adamant in using eval(), but made it difficult to access the dictionary of users to prevent copying. The dictionary hacker911 holds the user_name and password for all users. The bookstore doesn't allow the string user to contain h, k, or a digit, hoping it will keep the dictionary inaccessible from the eval() procedure. The get_user(user_name) function returns entries for users which match a given username.
Create an injection string user that copies the user's dictionary to res.


[Examples]

___
hacker911 = {
  "u_DHQAIC": "pwd_AHGBLIXIO",
  "u_BEOUROGP": "pwd_GQGWVE",
  "u_RPZSQBT": "pwd_EFLT",
  "u_DABRZJRIV": "pwd_EHZUQBW",
  "u_JVGQJC": "pwd_NQFXBQ",
  "u_RVUUIB": "pwd_JNKBLTHEC"
}

def get_user(s):
    if s in hacker911:
        return {s: hacker911[s]}
    return dict()

res = eval("get_user(\"{}\")".format(user))

print(res) ➞ hacker911
_____



[Notes]

___
*) The dictionary hacker911 is randomly generated per test iteration.
*) Create a string, not a function.
___



[data_structures] [logic] [strings] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

