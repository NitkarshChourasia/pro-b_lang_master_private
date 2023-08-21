/*
####  🦁🐱 Count Animals 🐶🐺  ####

Mubashir needs your help to find out number of animals hidden in a given string txt.
You are provided with an array of animals given below:
___
animals = ["dog", "cat", "bat", "cock", "cow", "pig",
"fox", "ant", "bird", "lion", "wolf", "deer", "bear",
"frog", "hen", "mole", "duck", "goat"]
_____

Rule: Return the maximum number of animal names. See the below example:
___
txt = "goatcode"

countAnimals(txt) ➞ 2
// First animal = "dog"
// Remaining string = "atcoe",
// Second animal = "cat".
// count = 2 (correct)

// If you got a "goat" first time
// remaining string = "code", 
// no animal will be found during next time.
// count = 1 (wrong)
_____



[Examples]

___
countAnimals("goatcode") ➞ 2
// "dog", "cat"

countAnimals("cockdogwdufrbir") ➞ 4
// "cow", "duck", "frog", "bird"

countAnimals("dogdogdogdogdog") ➞ 5
_____



[Notes]

N/A


[language_fundamentals] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

