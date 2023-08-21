/*
####  Look-and-Say Sequence  ####

Create a function that takes in two positive integers start and n and returns a list of the first n terms of the look-and-say sequence starting at the given start.
Each term of the look-and-say sequence (except for the first term) is created from the previous term using the following process.
Start with a term in the sequence (for example, 111312211):
___
111312211
_____

Split it into subsequences of consecutive repeating digits:
___
111 3 1 22 11
_____

Count the number of digits in each subsequence:
___
three 1, one 3, one 1, two 2, two 1
_____

Turn everything into digits:
___
3 1, 1 3, 1 1, 2 2, 2 1
_____

Now combine everything into one number:
___
3113112221
_____

So 3113112221 is the next term in the sequence after 111312211.


[Examples]

___
lookAndSay(1, 7) ➞ {1, 11, 21, 1211, 111221, 312211, 13112221}

lookAndSay(123, 4) ➞ {123, 111213, 31121113, 1321123113}

lookAndSay(70, 5) ➞ {70, 1710, 11171110, 31173110, 132117132110
_____



[Notes]

Your output should be an array of integers in the correct sequence..


[numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Convert numerical value to string Returns a string with the representation of val.
_________
_________
std::stoi
http://www.cplusplus.com/reference/string/stoi/
Convert string to integer Parses str interpreting its content as an integral number of the specified base, which is returned as an int value. If idx is not a null poin …
_________
_________
std::string
http://www.cplusplus.com/reference/string/string/
String class Strings are objects that represent sequences of characters.
_________

*/
//Your code should go here:

