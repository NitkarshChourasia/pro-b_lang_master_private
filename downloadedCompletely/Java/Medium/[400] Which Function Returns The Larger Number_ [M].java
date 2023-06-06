/*
####  Which Function Returns The Larger Number?  ####

Write a function that will be passed with two integer values, j and k and two functions, f and g, that don't take any parameters. Your function has to call them (and use the two integer values, accordingly), and returns a string that indicates which function has returned the larger number.
___
*) If f returns the larger number, return the string f.
*) If g returns the larger number, return the string g.
*) If both functions return the same number, return the string neither.
___



[Examples]

___
whichIsLarger(5, 10, f -> f, g -> g) ➞ "g"

whichIsLarger(25, 25, f -> f, g -> g) ➞ "neither"

whichIsLarger(505050, 5050, f -> f, g -> g) ➞ "f"
_____



[Notes]

___
*) This exercise is designed as an introduction to higher order functions (functions which use other functions to do their work).
*) Function f takes variable j as its parameter and g takes k as these functions are invoked inside your function.
*) Check out the Resources tab for more details about higher order functions.
___



[higher_order_functions] [language_fundamentals] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How to pass function as a parameter in a method?
https://techndeck.com/how-to-pass-function-as-a-parameter-in-a-method-in-java-8/
Here, we are going to see the magic that Java 8 brought to all of us in the form of ‘higher order functions’ or first-class functions. Higher order functions are the fu …
_________

*/
//Your code should go here:

