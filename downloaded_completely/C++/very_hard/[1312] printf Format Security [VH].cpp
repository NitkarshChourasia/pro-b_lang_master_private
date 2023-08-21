/*
####  printf Format Security  ####

printf is a standard C function that's a great way to easily print data to the console using format specifiers. That being said, it's common knowledge that you should NEVER give a user the ability to directly set the first parameter of a function that can take format specifiers.
To pass this challenge, you need to find out why users shouldn't be given full control of printf. A vulnerable function will take a string you provide and pass it to printf along with a value you need to modify.


[Examples]

___
// No examples! The fun is finding the exploit yourself!
_____



[Notes]

A format specifier is a character set like %s or %f. Look for one that writes to memory.


[bugs] [control_flow] [scope] 



-------------------------------------------------------------------
[Resources]
_________
printf
http://www.cplusplus.com/reference/cstdio/printf/
Writes the C string pointed by format to the standard output (stdout). If format includes format specifiers (subsequences beginning with %), the additional arguments fo …
_________
_________
Lecture on Format String Vulnerabilities
https://web.ecs.syr.edu/~wedu/Teaching/cis643/LectureNotes_New/Format_String.pdf
This lecture will show you why its a bad idea to pass the users input directly into a printf function.
_________

*/
//Your code should go here:

