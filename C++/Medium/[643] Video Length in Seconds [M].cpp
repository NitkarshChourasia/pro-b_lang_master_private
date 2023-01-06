/*
####  Video Length in Seconds  ####

You are given the length of a video in minutes. The format is mm:ss (e.g.: "02:54"). Create a function that takes the video length and return it in seconds.


[Examples]

___
minutesToSeconds("01:00") ➞ 60

minutesToSeconds("13:56") ➞ 836

minutesToSeconds("10:60") ➞ -1
_____



[Notes]

___
*) The video length is given as a string.
*) If the number of seconds is 60 or over, return -1 (see example #3).
*) You may get a number of minutes over 99 (e.g. "121:49" is perfectly valid).
___



[language_fundamentals] [math] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

