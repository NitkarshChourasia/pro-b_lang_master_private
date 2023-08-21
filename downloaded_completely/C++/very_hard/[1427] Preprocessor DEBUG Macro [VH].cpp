/*
####  Preprocessor DEBUG Macro  ####

In this challenge you are not supposed to write a function but two C/C++ preprocessor macros. It was supposed to be just one macro, but since there is no direct access to the compiler or the source files, it was not possible.
Anyway, these macros are supposed to be simple debugging macros. The first one (DOUT) prints/streams the input it gets to std::cout. The second one (NDOUT) ignores all input and does nothing.
These macros are supposed to be function-like macros. They each receive one argument, which may include stream operators ( operator<< ). After each use of these macros there is a semicolon: DOUT( /* input */ );


[Examples]

___
DOUT( "Hello " << "World!" ); ➞ "Hello World!"

DOUT( 1 << '+' << 2 << '=' << 1+2 ); ➞ "1+2=3"

NDOUT( "Hello" << "World!" ); ➞ ""
_____



[Notes]

___
*) Remember to stream the output to std::cout. Don't use printf or anything else. Don't try to return a string.
*) To spread macro definitions over multiple lines you can use backslashes \ as the last character on a line:
___

___
#define N \
123

std::cout << N << std::endl;         // prints "123"
_____


My original plan was to conditionally compile the DOUT macro based on whether DEBUG was defined or not ( ➞ #ifdef ... ). As mentioned earlier, that was not possible, since I have no access to the source files of your code or the tests and no access to the compiler itself. That is why you have to implement two distinct macros and not just one.


[language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Macros
https://www.educba.com/macros-in-c-plus-plus/
Are nothing but a piece of code in C++ programming language represented by some given names. Therefore, whenever you are running your source code and the same name is f …
_________

*/
//Your code should go here:

