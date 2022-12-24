/*
####  Bracket Logic  ####

Brackets and parentheses in mathematical expressions have to conform to certain logical rules. Every opening bracket must have a closing mate somewhere further down the line. Although brackets can be nested, different types cannot overlap:
___
*) ([<x+y>+3]-1) makes sense because each set of brackets contains or is contained by another set.
*) ([<x+y>+3)-1] makes no sense because the parentheses and the square brackets overlap.
___

Given a string expression that can contain four types of brackets: () <> [] {}, create a function that returns true if the bracket logic is valid and false if it is not.


[Examples]

___
bracketLogic("[<>()]") ➞ true

bracketLogic("[<(>)]") ➞ false

bracketLogic("[(a*b+<7-c>+9]") ➞ false
// Opening parenthesis has no mate.

bracketLogic("[{(h*i+3)-12]/4*x+2}") ➞ false
// Square and curly brackets overlap.

bracketLogic("[ab(c/d<e-f+(7*6)>)+2]") ➞ true
_____



[Notes]

Any characters other than the brackets can be ignored.


[logic] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Bracket Logic Java Coding Challenge
https://youtu.be/xZu9FWgOKZw
Bracket logic Java coding challenge.
_________
_________
Check for Balanced Parentheses in an Expression
https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in exp.
_________
_________
How to Check for Balanced Parentheses in an Expression
https://java2blog.com/check-for-balanced-parentheses-in-expression-java/
In this post, we will see how to check for balanced parentheses in an expression. Lets say, you have expression as a*(b+c)-(d*e) If you notice, above expression have ba …
_________

*/
//Your code should go here:

