"""
####  Correct the Spending Bill  ####

An employee receives a spending bill from the credit card company. He needs to modify the amounts for certain activities before submitting it to the employer for reimbursement. The input is a multiline string. Each line has the following form:
___
- activity_description = $amount
_____

Activities fall into four categories:
___
activity = {
  "secret": ["bribery", "spying", "settlement", "poaching"],
  "undesirable": ["gambling", "alcohol", "sex"],
  "illegal": ["drugs", "gun", "speeding"]
}

# "normal" ⁠— any other activity that does not have a word
# (case non-sensitive) from the 3 lists mentioned above.
_____

___
*) For secret activity, replace activity_description with len(description) * "x" and multiply the amount by 1.2 (and round to 2 digits) to have a secret tip for yourself. These spendings help the company to achieve objectives and not being checked too carefully.
*) For undesirable activity keep the description as is, but divide the amount by 2 (and round to 2 digits) to promote a positive outlook of the employee.
*) Illegal activities line needs to be removed completely from the bill. Nobody needs to see that.
*) Normal activities stay as is without modifications.
___

Write two regular expressions that will be passed to re.sub() in order to modify the bill.
___
pattern = ...
repl = ...
_____



[Examples]

___
8 activities: 2 from each category
s = """
- Rental car costs = $175.00
- Supplier bribery = $70000.00
- Coffee with secretary = $5.20
- Speeding ticket = $15.99
- Spying on competitors = $900.00
- Electroshock gun = $1500.00
- Online gambling = $500.00
- Alcoholic cocktail = $16.00
"""

re.sub(pattern, repl, s) ➞

6 remaining activities: 4 modified, 2 kept unchanged, 2 replaced with empty sting
"""
- Rental car costs = $175.00
- xxxxxxxxxxxxxxxx = $84000.00
- Coffee with secretary = $5.20
- xxxxxxxxxxxxxxxxxxxxx = $1080.00
- Online gambling = $250.00
- Alcoholic cocktail = $8.00
"""
_____



[Notes]

Prerequisite: Alessandro’s RegEx Exercises series.


[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Regex Tester and Debugger
https://regex101.com
With highlighting for PHP, PCRE, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

