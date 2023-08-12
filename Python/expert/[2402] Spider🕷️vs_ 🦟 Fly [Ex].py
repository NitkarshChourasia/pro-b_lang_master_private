"""
####  Spider🕷️vs. 🦟 Fly  ####

A spider web is defined by rings numbered from 0-4 from the center and radials labeled clock-wise from the top as A-H.
Create a function that takes the coordinates of spider and fly and returns the shortest path for the spider to get to the fly.
It's worth noting that the shortest path should be calculated "geometrically", not by counting the number of points that path goes through. We could arrange that:
___
*) Angle between every pair of radials is the same (45 degrees).
*) Distance between every pair of rings is always the same (let's say "x").
___


In the above picture, spider coordinates are "H3" and fly coordinates are "E2". The spider will follow the shortest path "H3-H2-H1-A0-E1-E2" to reach the fly.


[Examples]

___
spider_vs_fly("H3", "E2") ➞ "H3-H2-H1-A0-E1-E2"

spider_vs_fly("A4", "B2") ➞ "A4-A3-A2-B2"

spider_vs_fly("A4", "C2") ➞ "A4-A3-A2-B2-C2"
_____



[Notes]

The center of the web will always be A0.


[algorithms] [logic] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
String split() Method
https://www.programiz.com/python-programming/methods/string/split
Breaks up a string at the specified separator and returns a list of strings.
_________
_________
Dijkstra's algorithm
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
Dijkstra's algorithm (/ˈdaɪkstrəz/ DYKE-strəz) is an algorithm for finding the shortest paths between nodes in a weighted graph, which may represent, for example, road …
_________

"""
#Your code should go here:

