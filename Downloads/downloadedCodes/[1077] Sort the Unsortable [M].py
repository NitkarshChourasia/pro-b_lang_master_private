"""
####  Sort the Unsortable  ####

In this challenge you will be given a list similar to the following:
___
[[3], 4, [2], [5], 1, 6]
_____

In words, elements of the list are either an integer or a list containing a single integer. If you try to sort this list via sorted([[3], 4, [2], [5], 1, 6]), Python will whine about not being able to compare integers and lists.
However, us humans can clearly see that this list can reasonably be sorted according to "the content of the elements" as:
___
[1, [2], [3], 4, [5], 6]
_____

Create a function that, given a list similar to the above, sorts the list according to the "content of the elements".


[Examples]

___
sort_it([4, 1, 3]) ➞ [1, 3, 4]

sort_it([[4], [1], [3]]) ➞ [[1], [3], [4]]

sort_it([4, [1], 3]) ➞ [[1], 3, 4]

sort_it([[4], 1, [3]]) ➞ [1, [3], [4]]

sort_it([[3], 4, [2], [5], 1, 6]) ➞ [1, [2], [3], 4, [5], 6]
_____



[Notes]

To reiterate, elements of the list will be either integers or lists with a single integer.


[arrays] [language_fundamentals] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
sorted() Method
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
Ways to Sort a Zipped List by Values
https://www.geeksforgeeks.org/python-ways-to-sort-a-zipped-list-by-values/
Zipped lists are those lists where several lists are mapped together to form one list which can be used as one entity altogether. In Python Zip() function is used to ma …
_________
_________
type() Function
https://www.geeksforgeeks.org/python-type-function/
Returns class type of the argument(object) passed as parameter. type() function is mostly used for debugging purposes. Two different types of arguments can be passed t …
_________

"""
#Your code should go here:

