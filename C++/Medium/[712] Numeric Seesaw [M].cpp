/*
####  Numeric Seesaw  ####

A number is left-heavy if the digits on the left side are larger than the digits on the right. It is right-heavy if the digits on the right side are larger than the digits on the left. Else, it is balanced.
Create a function that takes in an integer and classifies it into one of the three mutually exclusive categories: left, right or balanced. For inputs with an odd number of integers, ignore the fulcrum (the middle number).


[Examples]

___
seesaw(3449) ➞ "right"
// since 34 < 49

seesaw(1143113) ➞ "left"
// since 114 > 113 (3 is the fulcrum)

seesaw(585585) ➞ "balanced"
// since 585 == 585
_____



[Notes]

N/A


[arrays] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Helpful for taking the substring of a string: substr(index, length).
_________

*/
//Your code should go here:

