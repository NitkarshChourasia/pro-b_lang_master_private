"""
####  Automatic Markdown  ####

In Edabit, you can surround text with asterisks, double asterisks, underscores and tildes to add formatting to certain words.
Complete the function markdown() so it takes a symbol as input, and returns a function which applies that formatting to a given word in a given sentence.


[Examples]

___
italicise = markdown("*")

italicise("Hello there!", "Hello") ➞ "*Hello* there!"

italicise("The tale of the two sparrows", "the") ➞ "*The* tale of *the* two sparrows"

italicise("Include punctuation!", "punctuation") ➞ "Include *punctuation!*"
_____

___
inline = markdown("`")

inline("Remember to return as a boolean value.", "boolean") ➞ "Remember to return as a `boolean` value."

inline("I want you to create the class Programmer...", "PROGRAMMER") ➞ "I want you to create the class `Programmer...`"

inline("Do not forget to return the value", "return") ➞ "Do not forget to `return` the value"
_____



[Notes]

___
*) The function should not be case sensitive.
*) Include punctuation in the markdown (see italicise example #3).
*) Punctuation will only include ?!.
___



[closures] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python Closures
http://www.trytoprogram.com/python-programming/python-closures/
In this article, you will learn about Python closures, understand the logic behind closures, how to create closures and their significance in programming.
_________
_________
Closures: How to Use Them and Why They Are Useful
https://www.youtube.com/watch?v=swU3c34d2NQ
Corey Schafer explains in this video how Closures work in Python and JavaScript.
_________

"""
#Your code should go here:

