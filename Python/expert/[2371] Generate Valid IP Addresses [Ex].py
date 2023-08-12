"""
####  Generate Valid IP Addresses  ####

The function is given a string consisting of digits. Create a function that generates a set of all possible valid IP-addresses using all digits. The address has four groups. Each group is a number from 0 to 255 inclusive; the number cannot have leading zeros unless it equals zero.
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses while "3.011.255.245" and "192.168.1.312" are invalid IP addresses. If no single address can be produced, return an empty set.


[Examples]

___
generate_ip_addresses("0101203") ➞ {"0.101.20.3", "0.10.120.3", "0.10.1.203"}

generate_ip_addresses("25525511135") ➞ {"255.255.11.135", "255.255.111.35"}

generate_ip_addresses("0000") ➞ {"0.0.0.0"}

generate_ip_addresses("010010") ➞ {"0.10.0.10", "0.100.1.0"}
_____



[Notes]

N/A


[algorithms] [conditions] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
IP address
https://en.wikipedia.org/wiki/IP_address
An Internet Protocol address (IP address) is a numerical label such as 192.0.2.1 that is connected to a computer network that uses the Internet Protocol for communicati …
_________

"""
#Your code should go here:

