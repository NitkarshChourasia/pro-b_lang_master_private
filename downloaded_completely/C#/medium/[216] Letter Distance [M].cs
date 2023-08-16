/*
####  Letter Distance  ####

Given two words, the letter distance is calculated by taking the absolute value of the difference in character codes and summing up the difference.
If one word is longer than another, add the difference in lengths towards the score.
To illustrate:
___
letterDistance("house", "fly") = dist("h", "f") + dist("o", "l") + dist("u", "y") + dist(house.Length, fly.Length)

= |104 - 102| + |111 - 108| + |117 - 121| + |5 - 3|
= 2 + 3 + 4 + 2
= 11
_____



[Examples]

___
LetterDistance("sharp", "sharq") ➞ 1

LetterDistance("abcde", "Abcde") ➞ 32

LetterDistance("abcde", "bcdef") ➞ 5
_____



[Notes]

___
*) Always start comparing the two strings from their first letter.
*) Excess letters are not counted towards distance.
*) Capital letters are included.
___



[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to Get ASCII Value of a String
https://stackoverflow.com/questions/44152329/how-to-get-ascii-value-of-a-string-in-c-sharp
I need to get the ASCII values of these individual array elements. Like for ar[0], ar[1]. I do not want to iterate through a loop.
_________
_________
Get ASCII Value of Character
https://www.delftstack.com/howto/csharp/get-ascii-value-of-a-string-in-csharp/
There are 2 main methods that can get the ASCII values of all the characters in a string in C#, the typecasting method, and the byte[] method.
_________

*/
//Your code should go here:

