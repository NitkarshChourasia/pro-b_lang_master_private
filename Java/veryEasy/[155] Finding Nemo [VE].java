/*
####  Finding Nemo  ####

You're given a string of words. You need to find the word "Nemo", and return a string like this: "I found Nemo at [the order of the word you find Nemo]!".
If you can't find Nemo, return "I can't find Nemo :(".


[Examples]

___
findNemo("I am finding Nemo !") ➞ "I found Nemo at 4!"

findNemo("Nemo is me") ➞ "I found Nemo at 1!"

findNemo("I Nemo am") ➞ "I found Nemo at 2!"
_____



[Notes]

___
*) ! , ? . are always separated from the last word.
*) Nemo will always look like Nemo, and not NeMo or other capital variations.
*) Nemo's, or anything that says Nemo with something behind it, doesn't count as Finding Nemo.
*) If there are multiple Nemo's in the sentence, only return the first one.
___



[arrays] [formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
indexOf() Method
https://beginnersbook.com/2013/12/java-string-indexof-method-example/
Used to find the index of a specified character or a substring in a given String. There are 4 variations of this method in String class:
_________
_________
Check if a String Contains a Substring
https://www.mkyong.com/java/java-check-if-a-string-contains-another-string/
In Java, we can use String.contains() to check if a String contains a substring. The idea is to convert all the strings and substring to lowercase before check with .co …
_________
_________
split() Method
https://www.tutorialspoint.com/java/java_string_split.htm
Splits contents of a string. Has two variants and splits this string around matches of the given regular expression.
_________
_________
equals() Method
https://www.tutorialspoint.com/java/java_string_equals.htm
Checks if string has given content. Compares this string to the specified object. The result is true if and only if the argument is not null and is a String object that …
_________
_________
Finding substring in a string in Java?
https://stackoverflow.com/questions/28186182/finding-substring-in-a-string-in-java
I am writing a program to find substring in the string in Java without using any Java Library. I had written a function subString(String str1, String str2) as shown bel …
_________

*/
//Your code should go here:

