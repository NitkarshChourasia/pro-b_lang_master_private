"""
####  Cleaning Project Files  ####

You are in the midst of organizing all of your coding projects. It's a mess! Every file you've ever created is located in the same folder.
To clean it up, you've decided that you will use one of two organization methods.

Create a function that takes in the current folder sorts the files according to the organization method (prefix or suffix). A folder is a grouping of files in the same list.


[Examples]

___
# Sorting by project name (ex1 and ex2)
clean_up(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "prefix") ➞ [
  ["ex1.html", "ex1.js"],
  ["ex2.html", "ex2.js"]
]

# Sorting by extension (.html and .js)
clean_up(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "suffix") ➞ [
  ["ex1.html", "ex2.html"],
  ["ex1.js", "ex2.js"]
]

clean_up(["music_app.js", "music_app.png", "music_app.wav", "tetris.png", "tetris.js"], "prefix") ➞ [
  ["music_app.js", "music_app.png", "music_app.wav"],
  ["tetris.png", "tetris.js"]
]

clean_up(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "suffix") ➞ [
  ["_1.rb", "_2.rb", "_3.rb", "_4.rb"]
]

clean_up(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "prefix") ➞ [
  ["_1.rb"], ["_2.rb"],
  ["_3.rb"], ["_4.rb"]
]
_____



[Notes]

Keep elements in the same relative order.


[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
itertools.groupby() in Python
https://www.geeksforgeeks.org/itertools-groupby-in-python/
itertools.groupby() in Python
_________
_________
split() Method
https://www.programiz.com/python-programming/methods/string/split
Breaks up a string at the specified separator and returns a list of strings.
_________
_________
startswith() Method
https://www.programiz.com/python-programming/methods/string/startswith
Returns True if a string starts with the specified prefix(string). If not, it returns False.
_________

"""
#Your code should go here:

