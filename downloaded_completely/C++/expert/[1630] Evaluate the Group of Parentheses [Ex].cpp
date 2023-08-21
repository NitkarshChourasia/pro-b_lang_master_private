/*
####  Evaluate the Group of Parentheses  ####

The function is given a balanced parentheses string. Each open "(" has corresponding closed ")". Compute the total score based on the following rules:
___
*) Substring s = "()" has score 1,
*) Substring "s1s2" has total score as score of "s1" + score of "s2",
*) Substring "(s)" has total score as 2 * score of "s".
___

Calculate the total score of the given expression and return it as integer.


[Examples]

___
evalParentheses("()") ➞ 1
// 1

evalParentheses("(())") ➞ 2
// 2 * 1

evalParentheses("()()") ➞ 2
// 1 + 1

evalParentheses("((())())") ➞ 6
// 2 * (2 * 1 + 1)

evalParentheses("(()(()))") ➞ 6
// 2 * (1 + 2 * 1)

evalParentheses("()(())") ➞ 3
// 1 + 2 * 1

evalParentheses("()((()))") ➞ 5
// 1 + 2 * 2 * 1
_____



[Notes]

N/A


[algorithms] [logic] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Regex Tutorial
https://www.softwaretestinghelp.com/regex-in-cpp/
Regular Expression or regexes or regexp as they are commonly called are used to represent a particular pattern of string or text. Regexes are often used to denote a sta …
_________

*/
//Your code should go here:

