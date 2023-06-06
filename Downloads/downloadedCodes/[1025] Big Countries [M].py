"""
####  Big Countries  ####

A country can be said as being big if it is:
___
*) Big in terms of population.
*) Big in terms of area.
___

Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:
___
*) Population is greater than 250 million.
*) Area is larger than 3 million square km.
___

Also, create a method which compares a country's population density to another country object. Return a string in the following format:
___
{country} has a {smaller / larger} population density than {other_country}
_____



[Examples]

___
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"
_____



[Notes]

___
*) Population density is calculated by dividing the population by the area.
*) Area is given in square km.
*) The input will be in the format (name_of_country, population, size_in_km2), where name_of_country is a string and the other two inputs are integers.
___



[classes] [math] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Object-Oriented Programming (OOP) in Python
https://realpython.com/python3-object-oriented-programming/
A programming paradigm which provides a means of structuring programs so that properties and behaviors are bundled into individual objects. For instance, an object coul …
_________
_________
Python Object Oriented Programming
https://www.programiz.com/python-programming/object-oriented-programming
In this article, you’ll learn about the Object Oriented Programming (OOP) in Python and their fundamental concept with examples.
_________

"""
#Your code should go here:

