"""
####  Message from Space  ####

You have received an encrypted message from space. Your task is to decrypt the message with the following simple rules:
___
*) Message string will consist of capital letters, numbers, and brackets only.
*) When there's a block of code inside the brackets, such as [10AB], it means you need to repeat the letters AB for 10 times.
*) Message can be embedded in multiple layers of blocks.
*) Final decrypted message will only consist of capital letters.
___

Create a function that takes encrypted message txt and returns the decrypted message.


[Examples]

___
space_message("ABCD") ➞ "ABCD"

space_message("AB[3CD]") ➞ "ABCDCDCD"
# "AB" = "AB"
# "[3CD]" = "CDCDCD"

space_message("IF[2E]LG[5O]D") ➞ "IFEELGOOOOOD"
_____



[Notes]

N/A


[loops] [recursion] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python lambda
https://www.datacamp.com/community/tutorials/python-lambda?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034358&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=21452&gclid=Cj0KCQiA2af-BRDzARIsAIVQUOdc0mB3uBIKz2zK1EBQ0FYgN3pGiqdZE_aH6xKFfMFxRtvnI13Rv7caAgTREALw_wcB
You can write your very own Python functions using the def keyword, function headers, docstrings, and function bodies. However, there's a quicker way to write functions …
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________

"""
#Your code should go here:

