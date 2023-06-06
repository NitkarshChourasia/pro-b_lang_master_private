"""
####  Largest Exponential  ####

Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187. However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.
Create a function that takes Base-Exponent pairs and returns the line number which has the greatest numerical value.


[Examples]

___
largest_exponential([
  (519432,525806),
  (632382,518061),
  (78864,613712),
  (466580,530130),
  (780495,510032)
]) ➞ 5

largest_exponential([
  (375856,539061),
  (768907,510590),
  (165993,575715),
  (976327,501755),
  (898500,504795),
  (360404,540830)
]) ➞ 4

largest_exponential([
  (478714,529095),
  (694144,514472)
]) ➞ 1
_____



[Notes]

As mentioned, the actual values may contain some millions of digits. So, it's impractical to actually calculate the values and compare them.


[logic] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
max() Method
https://www.programiz.com/python-programming/methods/built-in/max
Returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters.
_________
_________
List index() Method
https://www.programiz.com/python-programming/methods/list/index
Returns the index of the specified element in the list.
_________
_________
Getting key with maximum value in dictionary
https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
You can use operator.itemgetter for that: import operator stats = {'a':1000, 'b':3000, 'c': 100} max(stats.iteritems(), key=operator.itemgetter(1))[0]
_________
_________
Which base/exponent pair in the file has the greatest numerical value?
https://www.mathblog.dk/project-euler-99-which-baseexponent-pair-in-the-file-has-the-greatest-numerical-value/
At first I thought it would be fun to see how the BigInteger class would fare in this problem. The answer is not so well. In fact calculating the first number alone tak …
_________

"""
#Your code should go here:

