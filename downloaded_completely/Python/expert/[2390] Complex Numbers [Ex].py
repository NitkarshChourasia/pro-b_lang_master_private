"""
####  Complex Numbers  ####

A complex number is a number that can be expressed in the form a + bj, where a and b are real numbers, and j is a solution of the equation x² = −1. Because no real number satisfies this equation, j is called an imaginary number. For the complex number a + bj, a is called the real part, and b is called the imaginary part.
Create a function that takes a list of real parts, a list of imaginary parts (including the imaginary number) and a desired result as an argument and returns all the possible pair of combinations of complex numbers that generate the desired result when added.


[Examples]

___
cnum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2j, 4j, 6j, 8j, 10j, 11j, 13j, 15j, 17j, 22j], '19+39j') ➞ [[(9, 17j), (10, 22j)], [(9, 22j), (10, 17j)]]

cnum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2j, 4j, 6j, 8j, 10j, 11j, 13j, 15j, 17j, 22j], '10+22j') ➞ [[(1, 11j), (9, 11j)], [(2, 11j), (8, 11j)], [(3, 11j), (7, 11j)], [(4, 11j), (6, 11j)]]

cnum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15], [2j, 4j, 6j, 8j, 10j, 11j, 13j, 15j, 17j, 22j], '90+22j')) ➞ []

cnum([0, -1, -2, -3, -4, -5, -10, 15, 20, 27, 34], [-2j, -3j, -5j, -7j, -11j, -13j, -17j, 71j, 73j, 79j, 83j, 89j, 97j], '5+80j') ➞ [[(-10, (-0-3j)), (15, 83j)], [(-10, (-0-17j)), (15, 97j)], [(-10, 83j), (15, (-0-3j))], [(-10, 97j), (15, (-0-17j))]]
_____



[Notes]

___
*) Each pair of complex numbers is created using the real parts list and the imaginary parts list. No repetitions are allowed, that is, the pair (9, 17j),(10, 22j) is equal to the pair (10, 22j),(9, 17j). In case of a repetition, you must keep the pair that has the lower real part number in the first complex number. In the case mentioned above, you must keep (9, 17j),(10, 22j) since 9 < 10.
*) Each complex number must have an unique real part and an unique imaginary part, ta
*) Take into consideration that the desired result is a string in the form a+bj.
*) The result is a list containing one nested list for each pair of complex numbers that generate the desired result when added.
*) The real parts list and the imaginary parts list contain unique numbers.
___



[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Complex Number
https://en.wikipedia.org/wiki/Complex_number
Is a number that can be expressed in the form a + bi, where a and b are real numbers, and i is a solution of the equation x2 = −1. Because no real number satisfies thi …
_________

"""
#Your code should go here:

