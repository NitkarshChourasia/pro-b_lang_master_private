"""
####  IPv4 Validation  ####

Create a function that takes a string (IPv4 address in standard dot-decimal format) and returns True if the IP is valid or False if it's not. For information on IPv4 formatting, please refer to the resources in the Resources tab.


[Examples]

___
is_valid("1.2.3.4") ➞ True

is_valid("1.2.3") ➞ False

is_valid("1.2.3.4.5") ➞ False

is_valid("123.45.67.89") ➞ True

is_valid("123.456.78.90") ➞ False

is_valid("123.045.067.089") ➞ False
_____



[Notes]

___
*) IPv6 addresses are not valid.
*) Leading zeros are not valid ("123.045.067.089" should return False).
*) You can expect a single string for every test case.
*) Numbers may only be between 1 and 255.
*) The last digit may not be zero, but any other might.
___



[algorithms] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
IPv4 and IPv6 Address Formatting
https://www.ibm.com/support/knowledgecenter/en/STCMML8/com.ibm.storage.ts3500.doc/opg_3584_IPv4_IPv6_addresses.html
An IPv4 address has the following format: x . x . x . x where x is called an octet and must be a decimal value between 0 and 255. Octets are separated by periods. An IP …
_________
_________
Matching IPv4 Addresses
https://www.safaribooksonline.com/library/view/regular-expressions-cookbook/9780596802837/ch07s16.html
You want to check whether a certain string represents a valid IPv4 address in 255.255.255.255 notation. Optionally, you want to convert this address into a 32-bit integer.
_________
_________
RegExr: Regex Tester
https://regexr.com/
An online tool to learn, build, & test Regular Expressions (RegEx / RegExp).
_________
_________
Textual Representation of IPv4 and IPv6 Addresses
https://tools.ietf.org/html/draft-main-ipaddr-text-rep-02#section-3.1
Official definition for the IPv4 Dotted Octet Format
_________

"""
#Your code should go here:

