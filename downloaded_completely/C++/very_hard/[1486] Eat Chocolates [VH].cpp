/*
####  Eat Chocolates  ####

Arun recently started eating chocolates. The shopkeeper tells Arun that for every three chocolates Arun eats, he will give him one chocolate in exchange for three chocolate wrappers. Now, Arun is confused about how many chocolates he can eat.
Given the total money Arun has and the cost of one chocolate, help him figure out how many chocolates he can eat.


[Examples]

___
countChocolates("4$", "1$") ➞ 5
// Arun eats three chocolates and purchases one more
// chocolate from Bitu in those three wrappers. Now he
// eats those two chocolates and hence 3 + 2 = 5.

countChocolates("55   $", "5$") ➞ 16

countChocolates("I have 68$", "2$")  ➞ 50

countChocolates("I got -68$ from my mom ", "2$")  ➞ 0
// Because -68 is a negative number and money can't be negative.
_____



[Notes]

Figure out the invalid inputs and take care of them.


[algorithms] [logic] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

