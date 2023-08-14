"""
####  Iterative Rotation Cipher  ####

In Iterative Rotation Cipher encoding is done by performing a series of character and substring rotations on a string input.
Create a function that takes two arguments; a positive integer and a string and returns a coded message.
___
message = `If you wish to make an apple pie from scratch, you must first invent the universe.`

iterative_ciph(10, message)➞ `10 hu fmo a,ys vi utie mr snehn rni tvte .ysushou teI fwea pmapi apfrok rei tnocsclet'
_____

There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
Step #1: Remove all spaces from the message.
___
`Ifyouwishtomakeanapplepiefromscratch,youmustfirstinventtheuniverse.`
_____

Step #2: Shift the order of string characters to the right by 10.
___
`euniverse.Ifyouwishtomakeanapplepiefromscratch,youmustfirstinventth`
_____

Step #3: Place the spaces back in their original positions.
___
`eu niv erse .I fyou wi shtom ake anap plepiefr oms crat ch,yo umustf irs tinventth`
_____

Step #4: Shift the order of characters for each space-separated substring to the right by 10:
___
`eu vni seer .I oufy wi shtom eak apan frplepie som atcr ch,yo ustfum sir htinventt`
_____

Repeat all steps 9 more times before returning the string with 10 prepended.
___
encodedMessage = `10 hu fmo a,ys vi utie mr snehn rni tvte .ysushou teI fwea pmapi apfrok rei tnocsclet`
_____

See the examples below for more understanding:


[Examples]

___
iterative_ciph(12, "Oh, Fortuna, you capricious sprite!")➞ "12 ory ,auruiec i,i OtacsuF!ht orpsnpo"

iterative_ciph(6, "Time is an illusion. Lunchtime doubly so.") ➞ "6 im.T ei no .lLnicsan iluushted imouys blo"

iterative_ciph(22, "There is nothing more atrociously cruel than an adored child.") ➞ "22 tareu oo iucnaTr dled oldthser.hg hiarm nhcn se rliyet oincoa"
_____



[Notes]

Want to decipher the encoded code ? Checkout this challenge !!


[cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String Concatenation
https://www.w3schools.com/python/python_strings_concatenate.asp
To concatenate, or combine, two strings you can use the + operator.
_________
_________
Python Strings
https://www.w3schools.com/python/python_strings.asp
Strings in python are surrounded by either single quotation marks, or double quotation marks. 'hello' is the same as "hello".
_________
_________
String join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string.
_________

"""
#Your code should go here:

