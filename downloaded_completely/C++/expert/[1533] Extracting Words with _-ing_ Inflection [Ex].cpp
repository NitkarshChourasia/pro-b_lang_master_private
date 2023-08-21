/*
####  Extracting Words with "-ing" Inflection  ####

Write a function that takes a string as an argument and returns a list of all the words inflected by "-ing". Your function should also exclude all the mono-syllabic words ending in "-ing" (e.g. bing, sing, sling, ...). Although these words end in "-ing", the "-ing" is not an inflection affix.


[Examples]

___
ingExtractor("coming bringing Letting sing") ➞ ["coming", "bringing", "Letting"]

ingExtractor("going Ping, king sHrink dOing") ➞ ["going", "dOing"]

ingExtractor("zing went ring, ding wing SINk") ➞ []
_____



[Notes]

___
*) Mono-syllabic means a word containing just one syllable.
*) It's probably best to use RegEx for this challenge.
___



[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Generate substring Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the ob …
_________

*/
//Your code should go here:

