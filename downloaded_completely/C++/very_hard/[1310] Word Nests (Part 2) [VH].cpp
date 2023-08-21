/*
####  Word Nests (Part 2)  ####

A word nest is created by taking a starting word, and generating a new string by placing the word inside itself. This process is then repeated.
Nesting 3 times with the word "incredible":
___
start  = incredible
first  = incre(incredible)dible
second = increin(incredible)credibledible
third  = increinincr(incredible)ediblecredibledible
_____

The final nest is increinincrincredibleediblecredibledible (depth = 3)
Valid word nests can always be collapsed to show the starting word, by reversing the process above:
___
word = "incredible"
nest = "increinincrincredibleediblecredibledible"

Steps:
=> "increinincrincredibleediblecredibledible" // starting nest
=> "increinincr(incredible)ediblecredibledible" // find word in nest
=> "increinincr            ediblecredibledible" // remove word
=> "increinincrediblecredibledible" // join remaining halves
=> "increin(incredible)credibledible" // find word in nest...

... repeat steps until single word remains

=> "incredible" (return true as "incredible" = word)
_____

When invalid word nests are collapsed, the starting word isn't found:
___
word = "spring"
nest = "sprspspspringringringg"

Steps:
=> "sprspspspringringringg" // starting nest
=> "sprspsp(spring)ringringg" // find word in nest
=> "sprspsp        ringringg" // remove word
=> "sprspspringringg" // join remaining halves
=> "sprsp(spring)ringg" // find word in nest...

... repeat steps until single word remains

=> "sprg" (return false as "sprig" != "spring")
_____

Given a starting word and a final word nest, return true if the word nest is valid. Return false otherwise.


[Examples]

___
validWordNest("deep", "deep") ➞ true

validWordNest("novel", "nonnonovnovnovelelelvelovelvel") ➞ true

validWordNest("painter", "ppaintppapaipainterinternteraintererainter") ➞ false
// Doesn't show starting word after being collapsed.

validWordNest("shape", "sssshapeshapehahapehpeape") ➞ false
// Word placed outside, not inside itself.
_____



[Notes]

Valid word nests can only be created by repeatedly placing the word inside itself, so at any point when collapsing the nest, there should only be one instance of the word to be found.


[conditions] [language_fundamentals] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
string::erase
http://www.cplusplus.com/reference/string/string/erase/
Removing chars within a string, whilst appending the string together.
_________
_________
string find
https://www.geeksforgeeks.org/string-find-in-cpp/
Is used to find the first occurrence of sub-string in the specified string being called upon. It returns the index of the first occurrence of the substring in the strin …
_________

*/
//Your code should go here:

