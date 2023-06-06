/*
####  Sort Numbers in Ascending Order  ####

Create a function that takes an array of numbers and returns a new array, sorted in ascending order (smallest to biggest).
___
*) Sort the numbers array in ascending order.
*) If the function's argument is null, an empty array, or undefined; return an empty array.
*) Return a new array of sorted numbers.
___



[Examples]

___
SortNumsAscending([1, 2, 10, 50, 5]) ➞ [1, 2, 5, 10, 50]

SortNumsAscending([80, 29, 4, -95, -24, 85]) ➞ [-95, -24, 4, 29, 80, 85]

SortNumsAscending(null) ➞ []

SortNumsAscending([]) ➞ []
_____



[Notes]

Test input can be positive or negative.


[arrays] [numbers] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
Sorting Arrays in C#
http://www.csharp-examples.net/sort-array/
To sort array of primitive types such as int, double or string use method Array.Sort(Array) with the array as a parameter. The primitive types implements interface ICom …
_________
_________
Enumerable.OrderBy Method (System.Linq)
https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.orderby?view=netframework-4.7.2
Sorts the elements of a sequence in ascending order.
_________
_________
Array.Sort() Method
https://www.geeksforgeeks.org/how-to-sort-an-array-in-c-sharp-array-sort-method-set-1/?ref=lbp#m3
Sorts the elements in a range of in an Array using the IComparable<T> generic interface implementation of each element of the Array.
_________
_________
Is there a shortcut way to return a sorted array?
https://stackoverflow.com/questions/44163242/is-there-a-shortcut-way-to-return-an-array-sorted-in-c-sharp
... other than using: Array.Copy(originalArray, newArray) to make a copy of the original one and then using: return Array.Sort (newArray) to get the sorted array -- wit …
_________

*/
//Your code should go here:

