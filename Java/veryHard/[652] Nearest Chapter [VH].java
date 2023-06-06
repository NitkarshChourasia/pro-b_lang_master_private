/*
####  Nearest Chapter  ####

Create a function that returns which chapter is nearest to the page you're on. If two chapters are equidistant, return the chapter with the higher page number.


[Examples]

___
nearestChapter(new Chapter[] {
  new Chapter("Chapter 1", 1),
  new Chapter("Chapter 2", 15),
  new Chapter("Chapter 3", 37)
}, 10) ➞ "Chapter 2"

nearestChapter(new Chapter[] {
  new Chapter("New Beginnings", 1),
  new Chapter("Strange Developments", 62),
  new Chapter("The End?", 194),
  new Chapter("The True Ending", 460)
}, 200) ➞ "The End?"

nearestChapter(new Chapter[] {
  new Chapter("Chapter 1a", 1),
  new Chapter("Chapter 1b", 5)
}, 3) ➞ "Chapter 1b"
_____



[Notes]

___
*) All page numbers in the dictionary will be valid integers.
*) Return the higher page number if ever two pages are equidistant (see test case #8).
*) A similar version of this challenge that uses Map-type classes instead of custom ones can be found via this link.
___



[classes] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
Reduction
https://docs.oracle.com/javase/tutorial/collections/streams/reduction.html
This collections Java tutorial describes interfaces, implementations, and algorithms in the Java Collections framework.
_________

*/
//Your code should go here:

