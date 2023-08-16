"""
####  KixCodes in the Netherlands  ####

In The Netherlands we have PostNL, the postal company. They use KixCodes, a fast way to deliver letters and packages that can be scanned during the process.

The code is a combination of: "Postal code", "House/box/call number" and "House appendage / suffix"
If there is a character between the house number and the suffix, we need to replace that with an X. Eventually, the code will be printed in the KixCode font.


[Examples]

___
kix_code("PostNL, Postbus 30250, 2500 GG 's Gravenhage") ➞ "2500GG30250"

kix_code("Liesanne B Wilkens, Kogge 11-1, 1657 KA Abbekerk") ➞ "1657KA11X1"

kix_code("Dijk, Antwoordnummer 80430, 2130 VA Hoofddorp") ➞ "2130VA80430"
_____



[Notes]

___
*) Your function will get an address line (string) separated by comma's.
*) The input format will always be the same.
*) Watch out for the different suffixes!
___



[algorithms] [formatting] [regex] 



-------------------------------------------------------------------
[Resources]
_________
Postcodes in the Netherlands
https://nl.wikipedia.org/wiki/Postcode#Postcodes_in_Nederland
A brief explanation of postcodes in the Netherlands and how they are formatted
_________
_________
Free Online Barcode Generator
https://barcode.tec-it.com/en/KIX?data=A123456
This online barcode generator demonstrates the capabilities of the TBarCode SDK barcode components. TBarCode simplifies bar code creation in your application - e.g. in …
_________
_________
Regex Tester and Debugger
https://regex101.com
With highlighting for PHP, PCRE, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

