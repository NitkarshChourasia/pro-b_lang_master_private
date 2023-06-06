/*
####  The Complete Bracelet  ####

A complete bracelet is an array with at least one subsequence (pattern) repeating at least two times, and completely - the subsequence cannot be cut-off at any point. The subsequence must have length two or greater.
Complete bracelets:
___
{ 1, 2, 3, 3, 1, 2, 3, 3 }  // Pattern: { 1, 2, 3, 3 }

{ 1, 2, 1, 2, 1, 2, 1, 2 }  // Pattern: { 1, 2 } or { 1, 2, 1, 2 }

{ 1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7 }  // Pattern: { 1, 1, 6, 1, 1, 7 }

{ 4, 4, 3, 4, 4, 4, 4, 3, 4, 4 }  // Pattern: { 4, 4, 3, 4, 4 }
_____

Incomplete bracelets:
___
{ 1, 2, 2, 2, 1, 2, 2, 2, 1 }  # Incomplete (chopped off)

{ 1, 1, 6, 1, 1, 7 }  # Incomplete (subsequence repeats only once)
_____

Create a function that returns true if a bracelet is complete, and false otherwise.


[Examples]

___
CompleteBracelet({ 1, 2, 2, 1, 2, 2 }) ➞ true

CompleteBracelet({ 5, 1, 2, 2 }) ➞ false

CompleteBracelet({ 5, 5, 5 }) ➞ false
// potential pattern { 5, 5 } cut-off (patterns >= 2)
_____



[Notes]

___
*) Patterns must be at least two integers in length.
*) Use Comments for a hint if you are stuck.
___



[arrays] [loops] [scope] [validation] 



-------------------------------------------------------------------
[Resources]
_________
For Loop
https://www.w3schools.com/cs/cs_for_loop.php
When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop.
_________

*/
//Your code should go here:

