"""
####  Burglary Series (23): Find and Remove  ####

The insurance guy calls. They were about to pay you all that fortune you've been anxiously waiting for, but they detected further irregularities; the list of stolen items is misformatted and appears to contain other entries that don't belong there. Find and remove them.
You receive a dict with nested dicts with strings as values. Convert their values to number and return a dict with entries that evaluate to type int.


[Examples]

___
find_and_remove({
    "workshop": {
      "bedsheets": "2000",
      "working": "v0g89t7t",
      "pen": "370",
      "movies": "wo1a3d5d",
    },
  }), {
    "workshop": {
      "bedsheets": 2000, 
      "pen": 370
      }
  }
_____

___
find_and_remove({
  "bedroom": {
    "slippers": "10000",
    "piano": "5500",
    "call": "vet",
    "travel": "world",
  },
}), {
  "bedroom": {
    "slippers": 10000,
    "piano": 5500,
  },
}
_____



[Notes]

___
*) This challenge was translated from Miguel Carvalho's JavaScript Burglary Series. The following are links to his Javascript series:
*) If you have suggestions on how to present or further test this challenge please leave a comment.
*) This series is part of a collection that focuses on objects. If you are interested in following the breath-taking narrative skills of yours truly or just do some object focused challenges (the challenges are ordered in ascending difficulty order), you can more easily do that here.
___



[arrays] [loops] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Dictionaries in Python
https://realpython.com/python-dicts/
In this tutorial we'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, you should have a good …
_________
_________
String isdigit() Method
https://www.programiz.com/python-programming/methods/string/isdigit
Returns True if all characters in a string are digits. If not, it returns False.
_________
_________
keys() Method
https://www.programiz.com/python-programming/methods/dictionary/keys
Returns a view object that displays a list of all the keys in the dictionary.
_________

"""
#Your code should go here:

