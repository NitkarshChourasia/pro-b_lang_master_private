/*
####  Raucous Applause  ####

After an amazing performance, the crowd goes wild! People clap enthusiastically and most claps overlap with each other to create one homogeneous sound.
An overlapped clap is a clap which starts but doesn't finish, as in "ClaClap" (The first clap is cut short and there are overall 2 claps)
Given a string of what the overlapping claps sounded like, return how many claps were made in total.


[Examples]

___
countClaps("ClaClaClaClap!") ➞ 4

countClaps("ClClClaClaClaClap!") ➞ 6

countClaps("CCClaClClap!Clap!ClClClap!") ➞ 9
_____



[Notes]

Each clap starts with a capital "C".


[language_fundamentals] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

