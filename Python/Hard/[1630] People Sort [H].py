"""
####  People Sort  ####

Given a list of people objects, create a function that sorts the list by an attribute name. The attribute to sort by will be given as a string.
The Person class will only include these attributes in the following order:
___
*) firstname
*) lastname
*) age
___



[Examples]

___
p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
_____

___
people_sort([p1, p2, p3], "firstname") ➞ [p2, p1, p3]
# Alice, Michael, Zoey

people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
# Jones, Smith, Waters

people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
# 21, 29, 40
_____



[Notes]

___
*) Sort the list in ASCENDING order.
*) All objects will be valid.
___



[classes] [language_fundamentals] [objects] 



-------------------------------------------------------------------
[Resources]
_________
getattr() Method
https://www.programiz.com/python-programming/methods/built-in/getattr
Returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.
_________
_________
vars() Function
https://www.programiz.com/python-programming/methods/built-in/vars
Returns the __dict__ attribute of the given object. In this tutorial, we will learn about Python vars() with the help of an example.
_________
_________
Sort a List of Objects
https://www.techiedelight.com/sort-list-of-objects-python/#:~:text=A%20simple%20solution%20is%20to%20use%20list.sort%20%28%29,extract%20a%20comparison%20key%20from%20each%20list%20object.
In this post, we will see how to sort a list of objects using an attribute in Python.
_________

"""
#Your code should go here:

