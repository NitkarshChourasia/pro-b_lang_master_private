"""
####  Pagination Class with OOP  ####

Your task is to create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

The pagination class will accept 2 parameters:

So for example we could initialize our pagination like this:
___
alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

p = Pagination(alphabetList, 4)
_____

And then use the method getVisibleItems to show the contents of the paginated list.
___
p.getVisibleItems() # ["a", "b", "c", "d"]
_____

You will have to implement various methods to go through the pages such as:
___
*) prevPage
*) nextPage
*) firstPage
*) lastPage
*) goToPage
___

Here's a continuation of the example above using nextPage and lastPage:
___
p.nextPage()

p.getVisibleItems()
# ["e", "f", "g", "h"]

p.lastPage()

p.getVisibleItems()
# ["y", "z"]
_____



[Notes]

___
*) The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
*) The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
*) Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
*) If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).
*) Please remove the comments I provided before publishing your solution.
___



[classes] [math] [numbers] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Class Methods Chaining
https://stackoverflow.com/questions/49112201/python-class-methods-chaining
Is it possible to chain somehow these methods and solve the issue of passing the argument (data) withing this methods chain?
_________
_________
Python Classes
https://docs.python.org/3/tutorial/classes.html
Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. …
_________
_________
Object-Oriented Programming (OOP) in Python
https://realpython.com/python3-object-oriented-programming/
Object-oriented Programming, or OOP for short, is a programming paradigm which provides a means of structuring programs so that properties and behaviors are bundled int …
_________

"""
#Your code should go here:

