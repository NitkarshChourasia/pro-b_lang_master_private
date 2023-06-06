/*
####  Contact List  ####

Write a sorting function that takes in an array of names and sorts them by last name either alphabetically (ASC) or reverse-alphabetically (DESC).


[Examples]

___
SortContacts(new string[] {
  "John Locke",
  "Thomas Aquinas",
  "David Hume",
  "Rene Descartes"
}, "ASC") ➞ {
  "Thomas Aquinas",
  "Rene Descartes",
  "David Hume",
  "John Locke"
}

// Aquinas (A) < Descartes (D) < Hume (H) < Locke (L)

SortContacts(new string[] {
  "Paul Erdos",
  "Leonhard Euler",
  "Carl Gauss"
}, "DESC") ➞ {
  "Carl Gauss",
  "Leonhard Euler",
  "Paul Erdos"
}

// Gauss (G) > Erdos (ER) > Euler (EU)

SortContacts([], "DESC") ➞ {}

SortContacts(null, "DESC") ➞ {}
_____



[Notes]

___
*) An array with a single name should be trivially returned.
*) An empty array, or an input of null should return an empty array.
___



[arrays] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
Sorting Data
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/sorting-data
A sorting operation orders the elements of a sequence based on one or more attributes. The first sort criterion performs a primary sort on the elements. By specifying a …
_________

*/
//Your code should go here:

