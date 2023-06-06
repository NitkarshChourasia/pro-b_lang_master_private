/*
####  Positive Count / Negative Sum  ####

Create a function that takes an array of positive and negative numbers. Return an array where the first element is the count of positive numbers and the second element is the sum of negative numbers.


[Examples]

___
CountPosSumNeg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) ➞ [10, -65]
// There are a total of 10 positive numbers.
// The sum of all negative numbers equals -65.

CountPosSumNeg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]) ➞ [7, -252]

CountPosSumNeg([91, -4, 80, -73, -28]) ➞ [2, -105]

CountPosSumNeg([]) ➞ []
_____



[Notes]

___
*) If given an empty array, return an empty array: []
*) Cast sum to int, don't mind the remaining decimal places.
*) 0 is not positive.
___



[arrays] [conditions] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Converting a double to an int in C#?
https://stackoverflow.com/questions/10754251/converting-a-double-to-an-int-in-c-sharp
In our code we have a double that we need to convert to an int. double score = 8.6; int i1 = Convert.ToInt32(score); int i2 = (int)score; Can anyone explain me why i1 …
_________
_________
List <T> Class
https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=netcore-3.1
Useful for making arrays without knowing their initial value.
_________
_________
foreach statement
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/foreach-in
Made to iterate through all of the members of any array.
_________
_________
Add Int to a List
https://www.dotnetperls.com/list
Concise explanation of adding Ints to a list.
_________

*/
//Your code should go here:

