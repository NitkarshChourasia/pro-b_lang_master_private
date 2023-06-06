/*
####  Sum of Resistance in Series Circuits  ####

When resistors are connected together in series, the same current passes through each resistor in the chain and the total resistance, RT, of the circuit must be equal to the sum of all the individual resistors added together. That is:
___
RT = R1 + R2 + R3 ...
_____

Create a function that takes an array of values resistance that are connected in series, and calculates the total resistance of the circuit in ohms. The ohm is the standard unit of electrical resistance in the International System of Units ( SI ).


[Examples]

___
seriesResistance([1, 5, 6, 3]) ➞ "15 ohms"

seriesResistance([16, 3.5, 6]) ➞ "25.5 ohms"

seriesResistance([0.5, 0.5]) ➞ "1.0 ohm"
_____



[Notes]

___
*) Round to the nearest decimal place.
*) All inputs will be valid.
*) Notice the singular ohm for values <= 1.
*) This challenge was inspired by Joshua Señoron's Python Sum of Resistance in Parallel Circuits challenge. You can find it here.
___



[arrays] [loops] [math] [physics] 



-------------------------------------------------------------------
[Resources]
_________
Resistors in Series
https://www.electronics-tutorials.ws/resistor/res_3.html
Resistors are said to be connected in series when they are daisy chained together in a single line resulting in a common current flowing through them
_________
_________
std::string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments. When pos is specified, the search only includes characters at or after positio …
_________
_________
to_string
http://www.cplusplus.com/reference/string/to_string/
Returns a string with the representation of val. The format used is the same that printf would print for the corresponding type:
_________

*/
//Your code should go here:

