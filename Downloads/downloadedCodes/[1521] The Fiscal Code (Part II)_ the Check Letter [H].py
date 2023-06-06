"""
####  The Fiscal Code (Part II): the Check Letter  ####

In this challenge, you must build a program that generates the last character of an Italian Codice Fiscale, an alphanumeric identifying ID code.
The last character, also called check letter or CIN (Control Internal Number), is calculated after converting every other character into a numeric value, in relation to the parity of their natural position into the string (treating so the string as a 1-indexed sequence).


When all characters will be converted accordingly to the conversion table, you have to sum these values and divide the result by 26: the remainder will give you the index of a letter, from A = 0 up to Z = 25.
Given a string code being a partial Fiscal Code, implement a function that returns the CIN as a capitalized single letter.


[Example]

___
fiscal_code("MRTMTT25D09F205") ➞ "Z"

Convert the characters in odd positions:

Pos   Char   Value
1st  -> M -> 18
3rd  -> T -> 14
5th  -> T -> 14
7th  -> 2 -> 5
9th  -> D -> 7
11th -> 9 -> 21
13th -> 2 -> 5
15th -> 5 -> 13

Convert the characters in even positions:

Pos   Char   Value
2nd  -> R -> 17
4th  -> M -> 12
6th  -> T -> 19
8th  -> 5 -> 5
10th -> 0 -> 0
12th -> F -> 5
14th -> 0 -> 0

Sum of the values:

18 + 14 + 14 + 5 + 7 + 21 + 5 + 13 +
17 + 12 + 19 + 5 + 0 + 5 + 0 = 155

The remainder (modulo) of 155 % 26 is 25

Starting from A = 0, Z is the 25th letter
_____

The following dict can be used for coding:
___
conversion_table = {
  "0": (1, 0), "I": (19, 8),
  "1": (0, 1), "J": (21, 9),
  "2": (5, 2), "K": (2, 10),
  "3": (7, 3), "L": (4, 11),
  "4": (9, 4), "M": (18, 12),
  "5": (13, 5), "N": (20, 13),
  "6": (15, 6), "O": (11, 14),
  "7": (17, 7), "P": (3, 15),
  "8": (19, 8), "Q": (6, 16),
  "9": (21, 9), "R": (8, 17),
  "A": (1, 0), "S": (12, 18),
  "B": (0, 1), "T": (14, 19),
  "C": (5, 2), "U": (16, 20),
  "D": (7, 3), "V": (10, 21),
  "E": (9, 4), "W": (22, 22),
  "F": (13, 5), "X": (25, 23),
  "G": (15, 6), "Y": (24, 24),
  "H": (17, 7), "Z": (23, 25)
}
_____



[Notes]

___
*) Remember that the positions of characters into the string are 1-indexed. On the other hand, when returning the check letter, the positions of the letters into the alphabet are 0-indexed.
*) You can expect only valid data: uppercase alpha-numeric strings made of 15 valid characters.
*) Check the Resources tab for more info on Codice Fiscale.
___



[algorithms] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Italian Fiscal Code
https://en.wikipedia.org/wiki/Italian_fiscal_code
The Italian fiscal code, officially known in Italy as Codice fiscale, is the tax code in Italy, similar to a Social Security Number (SSN) in the United States or the Na …
_________

"""
#Your code should go here:

