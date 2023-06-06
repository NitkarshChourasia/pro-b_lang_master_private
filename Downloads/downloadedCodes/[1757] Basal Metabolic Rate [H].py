"""
####  Basal Metabolic Rate  ####

Create a function that takes a dict with the size, the weight in kg, the age, how much sport the person does and whether the person is male or female:
___
dict = {
  "gender": "male",
  "height": 180,
  "weight": 80,
  "age": 20,
  "sport": 3
}
_____

Return the basal metabolic rate of the person rounded to one decimal place. The formula is:
___
*) BMR for Men: 66.47 + (13.75 weight) + (5.003 height) - (6.755 * age)
*) BMR for Women: 655.1 + (9.563 weight) + (1.85 height) - (4.676 * age)
___

Once you’ve calculated your BMR, this is then put into the Harris Benedict Formula , which calculates your total calorie intake required to maintain your current weight. This is as follows:
___
*) Little/no exercise(1): BMR * 1.2 = Total Calorie Need
*) Light exercise(2): BMR * 1.375 = Total Calorie Need
*) Moderate exercise (3): BMR * 1.55 = Total Calorie Need
*) Very active (4): BMR * 1.725 = Total Calorie Need
*) Extra active (5): BMR * 1.9 = Total Calorie Need
___



[Examples]

___
BMR({
  "gender": "female",
  "height": 170,
  "weight": 65,
  "age": 25,
  "sport": 5
}) ➞ 2801.2


BMR({
  "gender": "male",
  "height": 180,
  "weight": 80,
  "age": 20,
  "sport": 3
}) ➞ 2994.5


BMR({
  "gender": "female",
  "height": 170,
  "weight": 70,
  "age": 40,
  "sport": 2
}) ➞ 1996.5
_____



[Notes]

Round the final result to 1 decimal place.


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Dictionaries
https://realpython.com/python-dicts/
In this Python dictionaries tutorial you'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, yo …
_________
_________
round() Function
https://www.programiz.com/python-programming/methods/built-in/round
Returns a floating-point number rounded to the specified number of decimals. In this tutorial, we will learn about Python round() in detail with the help of examples.
_________
_________
Metabolism Calculator
https://www.diabetes.co.uk/bmr-calculator.html
BMR calculator calculates your basal metabolic rate is the number of calories required to keep your body functioning at rest, also known as your metabolism.
_________

"""
#Your code should go here:

