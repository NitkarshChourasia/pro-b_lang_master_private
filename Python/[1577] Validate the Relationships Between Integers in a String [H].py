"""
####  Validate the Relationships Between Integers in a String  ####

You will be given a string consisting of a list of integers and their relationships to their neighboring integers. For instance:
___
"-15<-10<=0=0<5"
_____

Test to see that all the relationships between the integers in the string are true. If they are, return True. If they are not, return False.


[Examples]

___
validate_relationships("5>-1<0=0<-5>5=5") ➞ False
# This is False because 0 is not less than -5.

validate_relationships("-15<-10<=0=0<5") ➞ True

validate_relationships("0=807<1000<=1000>9990<-3605<=20") ➞ False
# This is False because 0 is not equal to 807.
_____



[Notes]

___
*) This is a modifcation of Helen Yu's "Correct Signs" challenge.
*) As the examples above show, there could be negative numbers in the string.
*) The numbers will only be separated by: =, <, >, >=, <=
*) Tests will not contain any spaces.
___



[conditions] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
re.sub
https://lzone.de/examples/Python%20re.sub
Note: Take care to always prefix patterns containing \ escapes with raw strings (by adding an r in front of the string). Otherwise the \ is used as an escape sequence a …
_________
_________
Replace strings
https://note.nkmk.me/en/python-str-replace-translate-re-sub/
Here's how to replace strings in Python.Replace substrings: replace()Specify the maximum count of replacements: countReplace multiple different substringsReplace newlin …
_________
_________
eval() Method
https://www.w3schools.com/python/ref_func_eval.asp
Evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
_________

"""
#Your code should go here:

