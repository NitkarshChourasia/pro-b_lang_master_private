/*
####  Uno (Part 1)  ####

This question is inspired by the popular Uno card game.
Write a function that takes in two arguments: (1) a player's current hand and (2) the current face-up card on the table. The function will return true if the player can make a play, or false if the player has to draw from the deck.
A player can make a play if either:
___
*) They have a card that is the same color as the face-up card.
*) They have a card that is the same number as the face-up card.
___

___
canPlay(["yellow 3", "yellow 7", "blue 8", "red 9", "red 2"], "red 1") => true
// Since the player has two red cards, and the face-up card is red.

canPlay(["yellow 3", "yellow 7"], "blue 7") => true
// Since the player has a 7, and the face-up card is a 7.
_____



[Examples]

___
canPlay(["yellow 3", "yellow 5", "red 8"], "red 2") ➞ true

canPlay(["yellow 3", "yellow 5", "red 8"], "blue 5") ➞ true

canPlay(["yellow 3", "blue 5", "red 8", "red 9"], "green 4") ➞ false

canPlay(["yellow 3", "red 8"], "green 2") ➞ false
_____



[Notes]

___
*) Return false if the player is not holding any cards (an empty array).
*) There are no special cards or wild cards in this deck.
___



[arrays] [games] 



-------------------------------------------------------------------
[Resources]
_________
std::string
http://www.cplusplus.com/reference/string/string/
Strings are objects that represent sequences of characters.
_________
_________
<string>
http://www.cplusplus.com/reference/string/
This header introduces string types, character traits and a set of converting functions.
_________
_________
std::pair
https://en.cppreference.com/w/cpp/utility/pair
Is a class template that provides a way to store two heterogeneous objects as a single unit. A pair is a specific case of a std::tuple with two elements.
_________
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Vectors are sequence containers representing arrays that can change in size.
_________

*/
//Your code should go here:

