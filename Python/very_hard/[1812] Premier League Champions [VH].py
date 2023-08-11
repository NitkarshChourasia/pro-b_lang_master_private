"""
####  Premier League Champions  ####

Create a function that takes a list of football clubs with properties: name, wins, loss, draws, scored, conceded, and returns the team name with the highest number of points. If two teams have the same number of points, return the team with the largest goal difference.


[How to Calculate Points and Goal Difference]

___
team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }

Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
Goal Difference = scored - conceded = 88 - 20 = 68
_____



[Examples]

___
champions([
  {
    "name": "Manchester United",
    "wins": 30,
    "loss": 3,
    "draws": 5,
    "scored": 88,
    "conceded": 20,
  },
  {
    "name": "Arsenal",
    "wins": 24,
    "loss": 6,
    "draws": 8,
    "scored": 98,
    "conceded": 29,
  },
  {
    "name": "Chelsea",
    "wins": 22,
    "loss": 8,
    "draws": 8,
    "scored": 98,
    "conceded": 29,
  }
]) ➞ "Manchester United"
_____



[Notes]

Input is a list of teams.


[arrays] [objects] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
max() Method
https://www.programiz.com/python-programming/methods/built-in/max
Returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters.
_________
_________
Dictionaries in Python
https://realpython.com/python-dicts/
In this Python dictionaries tutorial we'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, you …
_________
_________
How to Use Python Lambda Functions
https://realpython.com/courses/python-lambda-functions/
In this step-by-step course, you'll learn about Python lambda functions. You'll see how they compare with regular functions and how you can use them in accordance with …
_________

"""
#Your code should go here:

