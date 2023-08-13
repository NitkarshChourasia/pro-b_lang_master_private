"""
####  ASCII Charts (Part 2: Bar Chart)  ####

Given a dictionary containing quarterly sales values for a year, return a string representing a bar chart of the sales by quarter.
___
*) Quarter names (Q1, Q2, Q3, Q4) should appear on the left.
*) Quarters should be sorted in descending order by value.
*) Quarters with the same value should be shown in their yearly order (Q1 -> Q4).
*) Bars should begin with a "|".
*) Repeat the character "#" to fill the bar, with each character having a value of 50.
*) A single space comes after the bar, then the sales for that quarter.
*) If the value is 0, there should be no space after "|".
*) Use the newline character ("\n") to separate each bar in the chart.
___



[Example #1]

___
bar_chart({"Q4": 250, "Q1": 300, "Q2": 150, "Q3": 0})
➞ "Q1|###### 300\nQ4|##### 250\nQ2|### 150\nQ3|0"
_____

When printed:
___
Q1|###### 300
Q4|##### 250
Q2|### 150
Q3|0
_____



[Example #2]

___
bar_chart({"Q4": 500, "Q3": 100, "Q2": 100, "Q1": 150})
➞ "Q4|########## 500\nQ1|### 150\nQ2|## 100\nQ3|## 100"
_____

When printed:
___
Q4|########## 500
Q1|### 150
Q2|## 100
Q3|## 100
_____



[Notes]

There should be no additional whitespace after each value.


[formatting] [objects] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python Dictionaries Explained
https://www.python-course.eu/python3_dictionaries.php
In this chapter of our online Python course we will present the dictionaries and the operators and methods on dictionaries. Python programs or scripts without lists and …
_________
_________
Sorting HOW TO
https://docs.python.org/3.3/howto/sorting.html
Python lists have a built-in list.sort() method that modifies the list in-place. There is also a sorted() built-in function that builds a new sorted list from an iterab …
_________

"""
#Your code should go here:

