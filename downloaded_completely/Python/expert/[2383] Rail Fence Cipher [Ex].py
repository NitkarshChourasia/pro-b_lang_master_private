"""
####  Rail Fence Cipher  ####

In Rail Fence Cipher encoding is done by by placing each character successively in a diagonal along a set of rails.
Create a function that takes two arguments; a string and the number of rails, and returns the encoded message.
___
message = "WEAREDISCOVEREDFLEEATONCE"
rails = 3

rail_fence_cipher(message, rails) ➞ "WECRLTEERDSOEEFEAOCAIVDEN"
_____

In above example, given message to be decomposed in 3 rails:
___
W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C
    A       I       V       D       E       N
_____

Starting from upper line, encoded message will be :
___
"WECRLTEERDSOEEFEAOCAIVDEN"
_____



[Examples]

___
rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3) ➞ "WECRLTEERDSOEEFEAOCAIVDEN"

rail_fence_cipher("EDABITISAMAZING", 4) ➞ "EIIDTSZNAIAAGBM"

rail_fence_cipher("WEWILLALLDIEONEDAY", 3) ➞ "WLLOAEILLDENDYWAIE"
_____



[Notes]

Rails will be >=2


[algorithms] [cryptography] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Rail Fence Cipher
https://crypto.interactive-maths.com/rail-fence-cipher.html
Is a transposition cipher that uses a table that looks a bit like an old rail fence viewed from above.
_________
_________
map() Method
https://www.geeksforgeeks.org/python-map-function/
Returns a map object (which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple, etc)
_________
_________
str() Method
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object.
_________
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________

"""
#Your code should go here:

