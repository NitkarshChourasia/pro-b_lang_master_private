"""
####  Grade Point Average  ####

Create a function that takes a dictionary representing student information and calculates the Grade Point Average using the formula explained below, and returns the following string:
___
sol_format  = a
a = "{student_name from dict} GPA for {student_semester from dict} is calculated_gpa"

# Formula Grade Point Average

# Quality Points :  A -> 4  B -> 3  C -> 2  D -> 1  F -> 0
# Example : grades  =["A","A"]  credit_hrs = [3,3]
# gpa = totalpoints / totalcredithrs = (4 * 3 + 4 * 3) / (3 + 3) -> 4.00
# Rounded to 2 Decimal Places
_____



[Examples]

___
gpa_calculator({"name": "Ansha Mandal", "courses": [{"name": "cal1", "credit_hours": 5, "grade": "A"}, {"name": "kin1", "credit_hours": 3, "grade": "A"}], "semester": "Spring 2018"}) ➞ "Ansha Mandal GPA for Spring 2018 is 4.00"
_____



[Notes]

GPA is rounded to two decimal places.


[arrays] [language_fundamentals] [logic] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

