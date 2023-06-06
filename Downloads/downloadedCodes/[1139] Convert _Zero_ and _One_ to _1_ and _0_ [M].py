"""
####  Convert "Zero" and "One" to "1" and "0"  ####

Create a function that takes a string as an argument. The function must return a string containing 1s and 0s based on the string argument's words. If any word in the argument is not equal to "zero" or "one" (case insensitive), you should ignore it. The returned string's length should be a multiple of 8, if the string is not a multiple of 8 you should remove the numbers in excess.


[Examples]

___
text_to_number_binary("zero one zero one zero one zero one") ➞ "01010101"

text_to_number_binary("Zero one zero ONE zero one zero one") ➞ "01010101"

text_to_number_binary("zero one zero one zero one zero one one two") ➞ "01010101"

text_to_number_binary("zero one zero one zero one zero three") ➞ ""

text_to_number_binary("one one") ➞ ""
_____



[Notes]

You must return the result as a string.


[arrays] [formatting] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.tutorialspoint.com/python/string_split.htm
Returns a list of all the words in the string, using str as the separator (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.
_________

"""
#Your code should go here:

