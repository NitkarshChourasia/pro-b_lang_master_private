"""
####  Reverse Sort: Lexical and Length  ####

Write a function that sorts the words in a given string lexicographically (lexical sort) and by length in reverse order.


[Examples]

___
reverse_sort("You've rocked the pragmatic world in the making!") 
 ➞ "pragmatic making! You've rocked world the the in"

reverse_sort("Tesh makes my world worth enjoying and living for.")
 ➞ "enjoying living worth world makes Tesh for. and my"

reverse_sort("Shaken by the bloody truth and crazy lies.")
 ➞ "Shaken bloody truth lies. crazy the and by"

reverse_sort("Programming in Python is a lot of fun.")
 ➞ "Programming Python fun. lot of is in a"
_____



[Notes]

___
*) Special characters, punctuation marks and symbols are part of the word that directly precedes it.
*) The space character separates each word in the given string.
*) Case insensitive sorting is required.
___



[sorting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
sorted() Method
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
String lower() Method
https://www.programiz.com/python-programming/methods/string/lower
Converts all uppercase characters in a string into lowercase characters and returns it.
_________
_________
Sort the Words in Lexicographical Order in Python
https://www.tutorialspoint.com/Sort-the-words-in-lexicographical-order-in-Python
Sorting words in lexicographical order mean that we want to arrange them first by the first letter of the word. Then for the words whose first letter is the same, we ar …
_________
_________
sort() Method
https://www.freecodecamp.org/news/the-python-sort-list-array-method-ascending-and-descending-explained-with-examples/
It's very important that you know that the sort() method modifies the list, so its original version is lost.
_________
_________
Sorting
https://docs.python.org/3/howto/sorting.html
Python lists have a built-in list.sort() method that modifies the list in-place. There is also a sorted() built-in function that builds a new sorted list from an iterable.
_________

"""
#Your code should go here:

