/
##Profitable Gamble

Create a function that takes three arguments prob, prize, pay and returns true if prob * prize > pay; otherwise return false.
To illustrate:
___
profitableGamble(0.2, 50, 9)
_____

... should yield true, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.


[Examples]

___
profitableGamble(0.2, 50, 9) ➞ true

profitableGamble(0.9, 1, 2) ➞ false

profitableGamble(0.9, 3, 2) ➞ true
_____



[Notes]

A profitable gamble is a game that yields a positive net profit, where net profit is calculated in the following manner: net_outcome = probability_of_winning * prize - cost_of_playing.


[conditions] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Java Ternary Operator
https://www.javainterviewpoint.com/java-ternary-operator/
The value of a variable often depends on whether a particular Boolean expression is or is not true. Java ternary operator let’s you assign a value to a variable based o …
_________
_________
Java Ternary Operator
http://tutorials.jenkov.com/java/ternary-operator.html
The Java ternary operator functions like a simplified Java if statement. The ternary operator consists of a condition that evaluates to either true or false, plus a val …
_________
/ 
// Your code should go here:

