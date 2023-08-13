"""
####  Modified Kaprekar Numbers  ####

A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the number into two integers and sum those integers, you have the same value you started with.
Consider a positive whole number n with d digits. We square n to arrive at a number that is either 2 * d digits long or (2 * d) - 1 digits long. Split the string representation of the square into two parts, l and r. The right-hand part, r must be d digits long. The left is the remaining substring. Convert those two substrings back to integers, add them and see if you get n.
For example, if n=5, d=1, then n squared = 25 . We split that into two strings and convert them back to integers 2 and 5. We test 2+5=7=5, so this is not a modified Kaprekar number. If n=9, d=1, and n squared = 81. This gives us 1+8=9, the original n.
Note that r may have leading zeros.
Complete the kaprekar_numbers() method. It should return the list of modified Kaprekar numbers in ascending order. kaprekar_numbers() has the following parameter(s):
___
*) p: an integer representing the lower integer limit.
*) q: an integer representing the upper integer limit.
___



[Examples]

___
kaprekar_numbers(1, 10) ➞ "1 9"

kaprekar_numbers(100, 300) ➞ "297"

kaprekar_numbers(1, 100) ➞ "1 9 45 55 99"
_____



[Notes]

___
*) Upper and lower ranges should be inclusive of the limits.
*) If no modified Kaprekar numbers exist in the given range, return "INVALID RANGE".
___



[algorithms] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How To Index and Slice Strings
https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
The Python string data type is a sequence made up of one or more individual characters consisting of letters, numbers, whitespace characters, or symbols. Strings are se …
_________
_________
String to Int() and Int to String Tutorial
https://careerkarma.com/blog/python-string-to-int/#:~:text=To%20convert%20an%20integer%20to,a%20particular%20type%20of%20data.
To convert a string to integer in Python, use the int() function. This function takes two parameters: the initial string and the optional base to represent the data. Us …
_________
_________
range() Type
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
Kaprekar Numbers
https://www.numbersaplenty.com/set/Kaprekar_number/
A number $n$ whose square can be partitioned into two parts whose sum is $n$ itself is called Kaprekar number. For example, $45$ is a Kaprekar number, because $4 …
_________

"""
#Your code should go here:

