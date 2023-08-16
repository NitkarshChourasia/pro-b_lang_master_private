"""
####  Maze Escape  ####

Given a two-dimensional list of maze and a list of directions. Your task is to follow the given directions.
___
*) If you can reach the endpoint before all your moves have gone, return "Finish".
*) If you hit any walls or go outside the maze border, return "Dead".
*) If you find yourself still in the maze after using all the moves, return "Lost".
___

The maze list will look like this:
___
maze = [
  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
  [1, 3, 1, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 2, 1]
]

# 0 = Safe place to walk
# 1 = Wall
# 2 = Start Point
# 3 = Finish Point
# N = North, E = East, W = West and S = South
_____

See the below examples for a better understanding:


[Examples]

___
exit_maze(maze, ["N", "E", "E"]) ➞ "Dead"
# Hitting the wall should return "Dead".

exit_maze(maze, ["N", "N", "N", "E"]) ➞ "Lost"
# Couldn't reach the finish point.

exit_maze(maze, ["N", "W", "W", "W", "N", "N", "N", "N", "W", "W", "S", "S", "S", "S", "W", "W", "N", "N", "N", "N", "N", "N", "N"]) ➞ "Finish"
_____



[Notes]

N/A


[arrays] [games] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Compass
https://www.mathsisfun.com/measure/compass-north-south-east-west.html
A Compass Bearing tells us direction. The 4 main directions are North, South, East and West (going clockwise they are NESW).
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum.
_________
_________
List Comprehesion
https://www.programiz.com/python-programming/list-comprehension
Suppose, we want to separate the letters of the word human and add the letters as items of a list. The first thing that comes in mind would be using for loop.
_________
_________
String count() Method
https://www.programiz.com/python-programming/methods/string/count
Returns the number of occurrences of a substring in the given string.
_________
_________
Modulo % Operator
https://realpython.com/python-modulo-operator/
Returns the remainder of dividing two numbers.
_________
_________
What is a common factor?
https://www.bbc.co.uk/bitesize/topics/z6j2tfr/articles/z72r97h#:~:text=A%20common%20factor%20is%20a,of%20more%20than%20two%20numbers.
Is a number that can be divided into two different numbers, without leaving a remainder.
_________

"""
#Your code should go here:

