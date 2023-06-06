"""
####  Imgur URL Parser  ####

Create a function that takes an imgur link (as a string) and extracts the unique id and type. Return an object containing the unique id, and a string indicating what type of link it is.
The link could be pointing to:
___
*) An album (e.g. http://imgur.com/a/cjh4E)
*) A gallery (e.g. http://imgur.com/gallery/59npG)
*) An image (e.g. http://imgur.com/OzZUNMM)
*) An image (direct link) (e.g. http://i.imgur.com/altd8Ld.png)
___



[Examples]

___
imgurUrlParser("http://imgur.com/a/cjh4E") ➞ { id: "cjh4E", type: "album" }

imgurUrlParser("http://imgur.com/gallery/59npG") ➞ { id: "59npG", type: "gallery" }

imgurUrlParser("http://i.imgur.com/altd8Ld.png") ➞ { id: "altd8Ld", type: "image" }
_____



[Notes]

There are a few cases where the link has some changes. Look at the additional tests in the Tests tab to know more.


[formatting] [objects] [regex] 



-------------------------------------------------------------------
[Resources]
_________
RegExr: Learn Build & Test RegEx
https://regexr.com
Regular expression tester with syntax highlighting, contextual help, video tutorial, reference, and searchable community patterns.
_________
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, PCRE, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

