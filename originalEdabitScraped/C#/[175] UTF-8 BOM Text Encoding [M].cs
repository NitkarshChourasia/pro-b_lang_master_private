/*
####  UTF-8 BOM Text Encoding  ####

Before Unicode became standard, text files and string data were encoded in different 8-bit based code pages, each different between Germany, Spain, Italy, Sweden, etc. Nowadays, UTF-8 is the mostly used standard for sending text in network communication and when saving text data to files.
UTF-8 encoded text files have a prefix that defines that the file is encoded in UTF-8. It is called a BOM (byte order mark). Use the .Net framework to determine the sequence for the UTF-8 BOM.


[Examples]

___
GetUTF8BOM() ➞ { 0xef, 0xbb, 0xbf } (byte array)
_____



[Notes]

Use the class UTF8Encoding in the System.Text namespace.


[strings] 



-------------------------------------------------------------------
[Resources]
_________
UTF8Encoding Class
https://docs.microsoft.com/en-us/dotnet/api/system.text.utf8encoding?view=netframework-4.8
Represents a UTF-8 encoding of Unicode characters.
_________
_________
UTF8Encoding.GetPreamble() Method
https://docs.microsoft.com/en-us/dotnet/api/system.text.utf8encoding.getpreamble?view=net-6.0
Returns a Unicode byte order mark encoded in UTF-8 format, if the UTF8Encoding encoding object is configured to supply one.
_________

*/
//Your code should go here:

