/*
####  Virtual DAC  ####

In electronics, a digital-to-analog converter (DAC, D/A, or D-to-A) is a system that converts a binary representation of that signal into an analog output. An 8 bit converter can represent a maximum of 2^8 different values, with each successive value differing by 1/256 of the full scale value, this becomes the system resolution and would be approximately 0.25% of the full range.
Create a function that takes a binary output reading and returns the analog voltage level that would create that DAC reading.
While value range is 0-1023, reference range is 0-5.00 volts. Value and reference is directly proportional.
This DAC has 10 bits of resolution and the DAC reference is at 5.00 volts.


[Examples]

___
adc(0) ➞ 0

adc(1023) ➞ 5

adc(500) ➞ 2.44

adc(400) ➞ 1.96
_____



[Notes]

You should return your value rounded to two decimal places.


[functional_programming] 



-------------------------------------------------------------------
[Resources]
_________
How does an ADC work?
https://components101.com/articles/analog-to-digital-adc-converters
For example in a 10 bit converter with 5V as the reference voltage, 1111111111 (all bits one, the highest possible 10 bit binary number) correspond to 5V and 0000000000 …
_________

*/
//Your code should go here:

