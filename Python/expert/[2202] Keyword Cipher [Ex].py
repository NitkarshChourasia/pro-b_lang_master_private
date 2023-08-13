"""
####  Keyword Cipher  ####

A Keyword Cipher is a monoalphabetic cipher which uses a keyword to provide encryption on given string of message.
Create a function that takes two arguments: a string message and a string key, and returns an encoded message.
For the encryption key, the keyword is placed at the beginning, followed by the rest of the characters in the alphabet in order (in other words, with the keyword characters removed):
___
A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z
K|E|Y|W|O|R|D|A|B|C|F|G|H|I|J|L|M|N|P|Q|S|T|U|V|X|Z
_____

The encrypted message substitutes each plaintext character with the encryption key character in the corresponding position.
Return the given message encrypted against the key:
___
eMessage = "KEYABC"
// A = K, B = E, C = Y, H = A, I = B, J = C
_____



[Examples]

___
keyword_cipher("keyword", "abchij") ➞ "keyabc"

keyword_cipher("purplepineapple", "abc") ➞ "pur"

keyword_cipher("mubashir", "edabit") ➞ "samucq"
_____



[Notes]

___
*) Don't forget to remove duplicates after concatenating string with keyword.
*) Non-alphabetic characters must be left as they are.
___



[cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
sorted() Method
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
String find() Method
https://www.programiz.com/python-programming/methods/string/find
Returns the index of first occurrence of the substring (if found). If not found, it returns -1.
_________
_________
maketrans() Method
https://www.w3schools.com/python/ref_string_maketrans.asp
Returns a mapping table that can be used with the translate() method to replace specified characters.
_________

"""
#Your code should go here:

