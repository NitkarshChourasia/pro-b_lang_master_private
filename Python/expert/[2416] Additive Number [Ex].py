"""
####  Additive Number  ####

Write a function that checks if a given sequence of digits is an additive sequence, i.e. if the sequence can be split into a sequence of numbers where each number is the sum of the previous two numbers.
For example:
___
"12988110101891"
_____

... is an additive sequence since it can be split into the sequence:
___
129, 881, 1010, 1891
_____

... and 129 + 881 = 1010, 881 + 1010 = 1891.
Note: A valid additive sequence should contain at least three numbers.


[Examples]

___
is_additive("112358") ➞ True
# The digits can be split into an additive sequence: 1, 1, 2, 3, 5, 8.
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

is_additive("129881000") ➞ True
# Each number can contain 1 or more digits: 12, 988, 1000.
# 12 + 988 = 1000

is_additive("12988110101891") ➞ True
# 129 + 881 = 1010, 881 + 1010 = 1891

is_additive("123456789") ➞ False

is_additive("300045007500") ➞ True
_____



[Notes]

___
*) The string will contain only digits 0, 1, 2, ... 9.
*) Numbers in the additive sequence cannot have leading zeros, so the sequences 1, 2, 03 and 1, 02, 3 are invalid.
___



[algebra] [algorithms] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

