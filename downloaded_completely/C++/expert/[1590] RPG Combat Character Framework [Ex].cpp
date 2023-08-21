/*
####  RPG Combat Character Framework  ####

Create classes to act as characters in a turn-based RPG. Test functions will be used to simulate player input.
___
*) Characters should start at least at level 1.
*) You've been provided with a starting point. Private variables should stay private.
*) You must replace the base class's virtual methods with your own class' implementations.
*) Players should gain an enemy's _xpReward when they win a fight.
*) Players should level up if their _xp is greater than 100.
*) Enemy _xpReward should be equal to 5 times their level plus 1/4 their attack and 1/4 their defense (rounded down).
*) Any character should be able to win and lose a fight. Don't think you'll succeed just because the player always wins!
*) Don't try to modify or implement anything in Char_base.
___



[Notes]

___
*) I've tried to lay out everything in a way that the only thing required is implementation and the structure design should be taken care of.
*) Try adding some printing to your methods with std::cout.
___



[classes] [data_structures] [games] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Classes (I) - C++ Tutorials
http://www.cplusplus.com/doc/tutorial/classes/
Learn how classes work in C++
_________
_________
Why do we need virtual functions in C++? - Stack Overflow
https://stackoverflow.com/a/2392656
How virtual functions work in classes.
_________

*/
//Your code should go here:

