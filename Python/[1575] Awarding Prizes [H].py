"""
####  Awarding Prizes  ####

You are given a dictionary of names and the amount of points they have. Return a dictionary with the same names, but instead of points, return what prize they get.
"Gold", "Silver", or "Bronze" to the 1st, 2nd and 3rd place respectively. For all the other names, return "Participation" for the prize.


[Examples]

___
award_prizes({
  "Joshua" : 45,
  "Alex" : 39,
  "Eric" : 43
}) ➞ {
  "Joshua" : "Gold",
  "Alex" : "Bronze",
  "Eric" : "Silver"
}

award_prizes({
  "Person A" : 1,
  "Person B" : 2,
  "Person C" : 3,
  "Person D" : 4,
  "Person E" : 102
}) ➞ {
  "Person A" : "Participation",
  "Person B" : "Participation",
  "Person C" : "Bronze",
  "Person D" : "Silver",
  "Person E" : "Gold"
}

award_prizes({
  "Mario" : 99,
  "Luigi" : 100,
  "Yoshi" : 299,
  "Toad" : 2
}) ➞ {
  "Mario" : "Bronze",
  "Luigi" : "Silver",
  "Yoshi" : "Gold",
  "Toad" : "Participation"
}
_____



[Notes]

___
*) There will always be at least three participants to recieve awards.
*) No number of points will be the same amongst participants.
___



[arrays] [numbers] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
zip() Function
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it. In this tutorial, we will learn about Python zip() in detail with the help of examples.
_________
_________
Sort a Dictionary by Value
https://thispointer.com/sort-a-dictionary-by-value-in-python-in-descending-ascending-order/
Different ways to sort a python dictionary by values in both ascending & descending order using sorted()  function by either using lambda function or itemgetter() as a …
_________

"""
#Your code should go here:

