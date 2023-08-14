"""
####  HTTP Requests  ####

The requests module is an HTTP library. You will be using it here to retrieve movie titles from the imdb.com website. See Resources for more details, but all you need for this challenge is get() and .text. The movie title can be easily located in the text of the web page because it is preceded by the HTML tag: <title> and followed by the tag: </title>.
The requests module is not a standard module but it can be accessed from the Edabit code editor. Improvise a function that takes an imdb.com address and returns the title of the movie at that address.


[Examples]

___
movie_title("https://www.imdb.com/title/tt0111161/") ➞ "The Shawshank Redemption (1994) - IMDb"

movie_title("https://www.imdb.com/title/tt0108052/") ➞ "Schindler"s List (1993) - IMDb"

movie_title("https://www.imdb.com/title/tt0073486/") ➞ "One Flew Over the Cuckoo"s Nest (1975) - IMDb"
_____



[Notes]

N/A


[strings] 



-------------------------------------------------------------------
[Resources]
_________
Requests: HTTP for Humans™
https://requests.readthedocs.io/en/master/
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive …
_________
_________
Using the Requests Library in Python
https://www.pythonforbeginners.com/requests/using-requests-in-python
First things first, let&rsquo;s introduce you to Requests. &nbsp; What is the Requests Resource? Requests is an Apache2 Licensed HTTP ...
_________

"""
#Your code should go here:

