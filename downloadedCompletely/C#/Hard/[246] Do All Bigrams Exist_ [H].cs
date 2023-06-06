/*
####  Do All Bigrams Exist?  ####

You are given an input array of bigrams, and an array of words.
Write a function that returns true if every single bigram from this array can be found at least once in an the list of words.


[Examples]

___
CanFind(new string[] { "at", "be", "th", au" }, new string[] { "beautiful", "the", "hat" }) ➞ true

CanFind(new string[] { "ay", "be", "ta", cu" }, new string[] { "maybe", "beta", "abet", "course" }) ➞ false
// "cu" does not exist in any of the words.

CanFind(new string[] { "th", "fo", "ma", or" }, new string[] { "the", "many", "for", "forest" }) ➞ true

CanFind(new string[] { "oo", "mi", "ki", la" }, new string[] { "milk", "chocolate", "cooks" }) ➞ false
_____



[Notes]

___
*) A bigram is string of two consecutive characters in the same word.
*) If the array of words is empty, return false.
___



[higher_order_functions] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
String.Contains() Method
https://www.geeksforgeeks.org/c-sharp-string-contains-method/
Is a string method. This method is used to check whether the substring occurs within a given string or not.
_________

*/
//Your code should go here:

