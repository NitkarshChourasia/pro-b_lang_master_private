"""
####  Shiritori Game  ####

This challenge is an English twist on the Japanese word game Shiritori. The basic premise is to follow two rules:

Below is an example of a Shiritori game:
___
["word", "dowry", "yodel", "leader", "righteous", "serpent"]  #valid!

["motive", "beach"]  # invalid! - beach should start with "e"

["hive", "eh", "hive"]  # invalid! - "hive" has already been said
_____

Write a Shiritori class that has two instance variables:
___
*) words: a list of words already said.
*) game_over: a boolean that is true if the game is over.
___

and two instance methods:
___
*) play: a method that takes in a word as an argument and checks if it is valid (the word should follow rules #1 and #2 above).

If it is valid, it adds the word to the words list, and returns the words list.
If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to true.
*) restart: a method that sets the words list to an empty one [] and sets the game_over boolean to false. It should return "game restarted".
___



[Examples]

___
my_shiritori = Shiritori()

my_shiritori.play("apple") ➞ ["apple"]
my_shiritori.play("ear") ➞ ["apple", "ear"]
my_shiritori.play("rhino") ➞ ["apple", "ear", "rhino"]
my_shiritori.play("corn") ➞ "game over"

# Corn does not start with an "o".

my_shiritori.words ➞  ["apple", "ear", "rhino"]

# Words should be accessible.

my_shiritori.restart() ➞ "game restarted"
my_shiritori.words ➞ []

# Words list should be set back to empty.

my_shiritori.play("hostess") ➞ ["hostess"]
my_shiritori.play("stash") ➞ ["hostess", "stash"]
my_shiritori.play("hostess") ➞ "game over"

# Words cannot have already been said.
_____



[Notes]

___
*) Note: The play method should not add an invalid word to the words list.
*) You don't need to worry about capitalization or white spaces for the inputs for the play method.
*) The play method will only take in single arguments as inputs.
*) Read more about Shiritori in the Resources tab.
___



[classes] [control_flow] [games] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Shiritori Game
https://en.wikipedia.org/wiki/Shiritori
Shiritori (しりとり) is a Japanese word game in which the players are required to say a word which begins with the final kana of the previous word. No distinction is made b …
_________
_________
Python Classes
https://www.w3schools.com/python/python_classes.asp
The examples above are classes and objects in their simplest form, and are  not really useful in real life applications.
_________

"""
#Your code should go here:

