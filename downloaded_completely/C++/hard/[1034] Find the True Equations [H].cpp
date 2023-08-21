/*
####  Find the True Equations  ####

In this challenge you will be given an array containing equations, with each equation written as a string. Here's an example:
___
["1+1=2", "2+2=3", "5*5=10", "3/3=1"]
_____

If you do the math, you'll see that the equations "1+1=2" and "3/3=1" are actually true while "2+2=3" and "5*5=10" are false nonsense.
Write a function which, given an array of equations as above, returns only the true equations. For instance, for the example above the output should be:
___
["1+1=2", "3/3=1"]
_____



[Examples]

___
trueEquations(["2*2=4"]) ➞ ["2*2=4"]

trueEquations(["1+1=3", "3-1=1"]) ➞ []

trueEquations(["1+1=2", "2+2=3", "5*5=10", "3/3=1"]) ➞ ["1+1=2", "3/3=1"]
_____



[Notes]

___
*) If all equations are false, return the empty array [], as in the second example.
*) The equations will only involve the elementary operations: +, -, *, /
___



[algebra] [language_fundamentals] [math] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
std::string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments. When pos is specified, the search only includes characters at or after positio …
_________

*/
//Your code should go here:

