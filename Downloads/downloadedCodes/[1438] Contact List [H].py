"""
####  Contact List  ####

Write a sorting function that takes in a list of names and sorts them by last name either alphabetically (ASC) or reverse-alphabetically (DESC).


[Examples]

___
sort_contacts([
  "John Locke",
  "Thomas Aquinas",
  "David Hume",
  "Rene Descartes"
], "ASC") ➞ [
  "Thomas Aquinas",
  "Rene Descartes",
  "David Hume",
  "John Locke"
]

# Aquinas (A) < Descartes (D) < Hume (H) < Locke (L)

sort_contacts([
  "Paul Erdos",
  "Leonhard Euler",
  "Carl Gauss"
], "DESC") ➞ [
  "Carl Gauss",
  "Leonhard Euler",
  "Paul Erdos"
]

# Gauss (G) > Erdos (ER) > Euler (EU)

sort_contacts([], "DESC") ➞ []

sort_contacts(None, "DESC") ➞ []
_____



[Notes]

___
*) A list with a single name should be trivially returned.
*) An empty list, or an input of None should return an empty list.
___



[arrays] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
How to sort a list alphabetically by the second word in a string?
https://stackoverflow.com/questions/20459982/how-to-sort-a-list-alphabetically-by-the-second-word-in-a-string
If I have a list and I want to keep adding lines to it and sorting them alphabetically by their last name, how could this be done? Sorted only seems to rearrange them b …
_________

"""
#Your code should go here:

