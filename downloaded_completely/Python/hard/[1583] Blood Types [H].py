"""
####  Blood Types  ####

When a person receives a blood transfusion, it is essential to make sure that the donor's blood type is compatible with the receiver's blood type. Receiving a blood type that is not compatible with your own can be life-threating, so blood banks always make sure to note the type of blood they receive from donors so that they can ensure a safe transfusion.
Blood types are named according to three factors: presence of antigen A, presence of antigen B, and presence of Rh factor. If antigen A is found, the blood type includes the letter "A". If antigen B is found, the blood type includes the letter "B". And if the Rh factor is present, the blood type ends with "+"; otherwise, it ends with "-". If neither antigen A nor antigen B are found, the blood type includes the letter "O".
For example, a person with only antigen A would have the blood type "A-". A person with both antigens A and B and the Rh factor would have blood type "AB+", and a person wih only the Rh factor would have blood type "O+".
The rules for giving and receiving blood are as follows:
___
*) A person with antigen A may only give blood to another person with antigen A.
*) A person with antigen B may only give blood to another person with antigen B.
*) A person with the Rh factor may only give blood to another person with the Rh factor.
*) A person with none of the above factors (O-) can give blood to anyone.
___

Write a function that takes in a donor's and receiver's blood types as strings and returns whether or not the donor can safely give blood to the receiver, according to the rules above.


[Examples]

___
can_give_blood("O+", "A+") ➞ True

can_give_blood("A-", "B-") ➞ False

can_give_blood("A-", "AB+") ➞ True
_____



[Notes]

___
*) All letters are capital.
*) Each blood type will be one of the following strings: "O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-".
___



[conditions] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Any & All
https://www.tutorialspoint.com/any-and-all-in-python
The any() function returns True if any item in an iterable are true, otherwise it returns False. However, if the iterable object is empty, the any () function will retu …
_________
_________
strip() Method
https://www.programiz.com/python-programming/methods/string/strip
Returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed).
_________
_________
How would I check a string for a certain letter in Python?
https://stackoverflow.com/questions/4877844/how-would-i-check-a-string-for-a-certain-letter-in-python
How would I tell Python to check the below for the letter x and then print "Yes"?
_________

"""
#Your code should go here:

