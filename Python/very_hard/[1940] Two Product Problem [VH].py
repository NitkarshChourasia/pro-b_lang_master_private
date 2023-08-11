"""
####  Two Product Problem  ####

Create a function that takes a list lst and a number N and returns a list of two integers from lst whose product equals N.


[Examples]

___
two_product([1, 2, -1, 4, 5], 20) ➞ [4, 5]

two_product([1, 2, 3, 4, 5], 10) ➞ [2, 5]

two_product([100, 12, 4, 1, 2], 15) ➞ None
_____



[Note]

___
*) Try doing this with 0(N) time complexity.
*) No duplicates.
*) In the list, there can be multiple solutions so return the solution with the lowest sum of indexes of product pairs (i.e. N = 10, solutions = [[2, 5], [10, 1]], indexes = [[600, 3000], [800, 900]], return [10, 1]).
*) If any doubts please refer to the comments section.
___



[conditions] [data_structures] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
Guide to Big-O Time Complexity
https://medium.com/@ariel.salem1989/an-easy-to-use-guide-to-big-o-time-complexity-5dcf4be8a444#:~:text=Linear%20Time%20Complexity%20describes%20an,size%20of%20the%20input%20data.&text=In%20other%20words%2C%20the%20larger,had%201%20index%20(i.e.%20array.
So your program works, but it’s running too slow. Or maybe your nice little code is working out great, but it’s not running as quickly as that other lengthier one. Welc …
_________
_________
Hash Tables
https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm
Are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the …
_________
_________
Remove Litem from List and Create New One
https://stackoverflow.com/questions/40717405/remove-an-item-in-list-and-get-a-new-list
Remove litem from list and create new one.
_________

"""
#Your code should go here:

