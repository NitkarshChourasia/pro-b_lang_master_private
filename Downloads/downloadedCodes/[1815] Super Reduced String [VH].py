"""
####  Super Reduced String  ####

Steve has a string of lowercase characters in range ascii[["a".."z"]]. He wants to reduce the string to its shortest length by doing a series of operations. In each operation, he selects a pair of adjacent lowercase letters that match, and he deletes them. For instance, the string aab could be shortened to b in one operation.
Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, return "Empty String".


[Case]

___
super_reduced_string("aaabccddd") ➞ "abd"
_____

Explanation:
___
"aaabccddd" -> "abccddd" -> "abddd" -> "abd"
_____



[Examples]

___
super_reduced_string("cccxllyyy") ➞ "cxy"

super_reduced_string("aa") ➞ "Empty String"

super_reduced_string("baab") ➞ "Empty String"

super_reduced_string("fghiiijkllmnnno") ➞ "fghijkmno"

super_reduced_string("chklssstt") ➞ "chkls"
_____



[Notes]

N/A


[algorithms] [regex] 



-------------------------------------------------------------------
[Resources]
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________
_________
Replace Strings
https://note.nkmk.me/en/python-str-replace-translate-re-sub/
Replace strings in Python using replace, translate, re.sub, re.subn methods.
_________

"""
#Your code should go here:

