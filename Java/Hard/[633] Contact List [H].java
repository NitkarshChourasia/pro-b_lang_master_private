/*
####  Contact List  ####

Write a sorting function that takes in an array of names and sorts them by last name either alphabetically (ASC) or reverse-alphabetically (DESC).


[Examples]

___
sortContacts([
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

// Aquinas (A) < Descartes (D) < Hume (H) < Locke (L)

sortContacts([
  "Paul Erdos",
  "Leonhard Euler",
  "Carl Gauss"
], "DESC") ➞ [
  "Carl Gauss",
  "Leonhard Euler",
  "Paul Erdos"
]

// Gauss (G) > Erdos (ER) > Euler (EU)

sortContacts([], "DESC") ➞ []

sortContacts(null, "DESC") ➞ []

sortContacts(undefined, "DESC") ➞ []
_____



[Notes]

___
*) An array with a single name should be trivially returned.
*) An empty array, or an input of null or undefined should return an empty array.
___



[arrays] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
collections.sort() Method
https://www.geeksforgeeks.org/collections-sort-java-examples/
java.util.Collections.sort() method is present in java.util.Collections class. It is used to sort the elements present in the specified list of Collection in ascending …
_________

*/
//Your code should go here:

