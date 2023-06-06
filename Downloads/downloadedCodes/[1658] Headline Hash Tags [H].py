"""
####  Headline Hash Tags  ####

Write a function that retrieves the top 3 longest words of a newspaper headline and transforms them into hashtags. If multiple words tie for the same length, retrieve the word that occurs first.


[Examples]

___
get_hash_tags("How the Avocado Became the Fruit of the Global Trade")
➞ ["#avocado", "#became", "#global"]

get_hash_tags("Why You Will Probably Pay More for Your Christmas Tree This Year")
➞ ["#christmas", "#probably", "#will"]

get_hash_tags("Hey Parents, Surprise, Fruit Juice Is Not Fruit")
➞ ["#surprise", "#parents", "#fruit"]

get_hash_tags("Visualizing Science")
➞ ["#visualizing", "#science"]
_____



[Notes]

___
*) If the title is less than 3 words, just order the words in the title by length in descending order (see example #4).
*) Punctuation does not count towards a word's length.
___



[regex] [sorting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Regular Expression Language
https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference
In this quick reference, learn to use regular expression patterns to match input text. A pattern has one or more character literals, operators, or constructs.
_________
_________
How to Use sorted() and sort() in Python
https://realpython.com/python-sort/
All programmers will have to write code to sort items or data at some point. Sorting can be critical to the user experience in your application, whether it’s ordering a …
_________

"""
#Your code should go here:

