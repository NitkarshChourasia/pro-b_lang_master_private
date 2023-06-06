"""
####  Find Domain Name From DNS Pointer (PTR) Records Using IP Address  ####

Write a function that takes an IP address and returns the domain name using PTR DNS records.


[Example]

___
get_domain("8.8.8.8") ➞ "dns.google"

get_domain("8.8.4.4") ➞ "dns.google"
_____



[Notes]

___
*) You may want to import socket.
*) Don't cheat and just print the domain name, you need to make a real DNS request.
*) Return as a string.
___



[formatting] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Reverse DNS Lookup in a Shared Hosting
https://stackoverflow.com/questions/19867548/python-reverse-dns-lookup-in-a-shared-hosting
Is there any way to do a reverse lookup using python, to check the list of websites sharing the same IP address in a shared hosting.
_________
_________
Using Socket Import in Python to Get DNS Data
https://stackoverflow.com/questions/1857146/python-attribute-error-type-object-socketobject-has-no-attribute-gethostbyn
Best practices for importing and utilizing the socket module in Python and using its methods to call on a socket object. Note that this exercise uses a different socket …
_________
_________
Reverse DNS
https://searchnetworking.techtarget.com/definition/reverse-DNS
Reverse DNS (rDNS) is a method of resolving an IP address into a domain name, just as the domain name system (DNS) resolves domain names into associated IP addresses.
_________
_________
Socket
https://docs.python.org/3/library/socket.html
This module provides access to the BSD socket interface. It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms.
_________
_________
How to Perform DNS Reverse Lookup for Verifying Googlebot
https://www.holisticseo.digital/python-seo/dns-reverse-lookup/
DNS reverse lookup with Python for verifying Googlebot. How to clear Log File for a better Log Analysis via DNS Reverse Lookup and Python.
_________
_________
How To Find Domain Name From DNS Pointer (PTR) Records Using IP Address
https://www.youtube.com/watch?v=Z0Uh3OJCx3o
In this video I will show you How To Find Domain Name From DNS Pointer (PTR) Records Using IP Address.
_________

"""
#Your code should go here:

