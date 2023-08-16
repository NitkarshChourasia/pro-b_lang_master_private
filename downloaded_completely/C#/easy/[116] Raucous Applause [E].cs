/*
####  Raucous Applause  ####

After an amazing performance, the crowd goes wild! People clap enthusiastically and most claps overlap with each other to create one homogeneous sound.
An overlapped clap is a clap which starts but doesn't finish, as in "ClaClap" (the first clap is cut short and there are overall 2 claps).
Given a string of what the overlapping claps sounded like, return how many claps were made in total.


[Examples]

___
CountClaps("ClaClaClaClap!") ➞ 4

CountClaps("ClClClaClaClaClap!") ➞ 6

CountClaps("CCClaClClap!Clap!ClClClap!") ➞ 9
_____



[Notes]

Each clap starts with a capital "C".


[language_fundamentals] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Enumerable.Where Method
https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.where?view=netcore-3.1
Filters a sequence of values based on a predicate.
_________
_________
Enumerable.Count Method
https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.count?view=netcore-3.1
Returns the number of elements in a sequence.
_________

*/
//Your code should go here:

