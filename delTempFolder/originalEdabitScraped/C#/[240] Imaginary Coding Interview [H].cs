/*
####  Imaginary Coding Interview  ####

Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.
The criteria for a candidate to be qualified in the coding interview is:

If all the above conditions are satisfied, return "qualified", else return "disqualified".
You will be given an array of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.
Given an array, in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].
The maximum time to complete the interview includes a buffer time of 20 minutes.


[Examples]

___
Interview(new int [] { 5, 5, 10, 10, 15, 15, 20, 20 }, 120) ➞ "qualified"

Interview(new int [] { 2, 3, 8, 6, 5, 12, 10, 18 }, 64) ➞  "qualified"

Interview(new int [] { 5, 5, 10, 10, 25, 15, 20, 20 }, 120) ➞ "disqualified"
// Exceeded the time limit for a medium question.

Interview(new int [] { 5, 5, 10, 10, 15, 15, 20 }, 120) ➞ "disqualified"
// Did not complete all the questions.

Interview(new int [] { 5, 5, 10, 10, 15, 15, 20, 20 }, 130) ➞ "disqualified"
// Solved all the questions in their respected time limits but exceeded the total time limit of the interview.
_____



[Notes]

Try to solve the problem using only array methods.


[arrays] [conditions] [interview] 



-------------------------------------------------------------------
[Resources]
_________
enumerable.zip Method
https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.zip?view=net-5.0
Applies a specified function to the corresponding elements of two sequences, producing a sequence of the results.
_________

*/
//Your code should go here:

